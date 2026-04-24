from __future__ import annotations

import argparse
import json
import re
import shutil
import sqlite3
import sys
import unicodedata
from pathlib import Path


def parse_args() -> argparse.Namespace:
    project_root = Path(__file__).resolve().parents[1]
    default_zotero_dir = Path.home() / "Zotero"
    parser = argparse.ArgumentParser(
        description="Import Zotero PDF attachments into PaperQA2 data/papers."
    )
    parser.add_argument(
        "--zotero-dir",
        type=Path,
        default=default_zotero_dir,
        help=f"Zotero data directory (default: {default_zotero_dir})",
    )
    parser.add_argument(
        "--paper-directory",
        type=Path,
        default=project_root / "data" / "papers",
        help="Destination directory for copied PDFs.",
    )
    parser.add_argument(
        "--manifest-path",
        type=Path,
        default=project_root / "data" / "zotero-import-manifest.json",
        help="Where to write the import manifest JSON.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Optional max number of PDFs to import. 0 means all.",
    )
    parser.add_argument(
        "--use-backup",
        action="store_true",
        help="Read zotero.sqlite.bak instead of zotero.sqlite.",
    )
    return parser.parse_args()


def open_database(zotero_dir: Path, use_backup: bool) -> tuple[sqlite3.Connection, Path]:
    candidates = []
    if use_backup:
        candidates.append(zotero_dir / "zotero.sqlite.bak")
    else:
        candidates.extend(
            [zotero_dir / "zotero.sqlite", zotero_dir / "zotero.sqlite.bak"]
        )

    last_error: Exception | None = None
    for candidate in candidates:
        if not candidate.exists():
            continue
        try:
            conn = sqlite3.connect(
                f"file:{candidate.as_posix()}?mode=ro&immutable=1", uri=True
            )
            conn.row_factory = sqlite3.Row
            conn.execute("SELECT 1")
            return conn, candidate
        except Exception as exc:  # pragma: no cover
            last_error = exc

    if last_error:
        raise RuntimeError(f"Unable to open Zotero database: {last_error}") from last_error
    raise FileNotFoundError(f"No Zotero database found under {zotero_dir}")


def clean_filename(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    normalized = re.sub(r'[<>:"/\\\\|?*]+', " ", normalized)
    normalized = re.sub(r"[^A-Za-z0-9 .,_()\.-]+", " ", normalized)
    normalized = re.sub(r"\s+", " ", normalized).strip(" .")
    return normalized or "untitled"


def extract_year(date_value: str | None) -> str:
    if not date_value:
        return "unknown-year"
    match = re.search(r"(19|20)\d{2}", date_value)
    return match.group(0) if match else "unknown-year"


def load_pdf_items(conn: sqlite3.Connection) -> list[sqlite3.Row]:
    query = """
    SELECT
        parent.itemID AS parent_item_id,
        parent.key AS parent_key,
        child.key AS attachment_key,
        attachment.path AS attachment_path,
        MAX(CASE WHEN field.fieldName = 'title' THEN value.value END) AS title,
        MAX(CASE WHEN field.fieldName = 'date' THEN value.value END) AS item_date,
        MAX(CASE WHEN field.fieldName = 'DOI' THEN value.value END) AS doi,
        MAX(CASE WHEN field.fieldName = 'publicationTitle' THEN value.value END) AS publication_title
    FROM itemAttachments AS attachment
    JOIN items AS child
        ON child.itemID = attachment.itemID
    JOIN items AS parent
        ON parent.itemID = attachment.parentItemID
    LEFT JOIN itemData AS data
        ON data.itemID = parent.itemID
    LEFT JOIN fieldsCombined AS field
        ON field.fieldID = data.fieldID
    LEFT JOIN itemDataValues AS value
        ON value.valueID = data.valueID
    LEFT JOIN deletedItems AS deleted_parent
        ON deleted_parent.itemID = parent.itemID
    LEFT JOIN deletedItems AS deleted_child
        ON deleted_child.itemID = child.itemID
    WHERE attachment.contentType = 'application/pdf'
        AND deleted_parent.itemID IS NULL
        AND deleted_child.itemID IS NULL
    GROUP BY parent.itemID, parent.key, child.key, attachment.path
    ORDER BY parent.itemID
    """
    return list(conn.execute(query))


def resolve_source_pdf(zotero_dir: Path, row: sqlite3.Row) -> Path:
    storage_dir = zotero_dir / "storage" / row["attachment_key"]
    attachment_path = row["attachment_path"] or ""
    filename = ""
    if attachment_path.startswith("storage:"):
        filename = attachment_path.split("storage:", 1)[1]
    if filename:
        candidate = storage_dir / filename
        if candidate.exists():
            return candidate
    pdfs = sorted(storage_dir.glob("*.pdf"))
    if not pdfs:
        raise FileNotFoundError(f"No PDF found in {storage_dir}")
    return pdfs[0]


def build_destination_name(row: sqlite3.Row, existing_names: set[str]) -> str:
    year = extract_year(row["item_date"])
    title = clean_filename(row["title"] or row["attachment_key"])
    base = f"{year} - {title}.pdf"
    if len(base) > 180:
        base = f"{year} - {title[:160].rstrip()}.pdf"

    candidate = base
    if candidate.lower() in existing_names:
        return candidate

    existing_names.add(candidate.lower())
    return candidate


def import_pdfs(
    zotero_dir: Path,
    paper_directory: Path,
    manifest_path: Path,
    limit: int,
    use_backup: bool,
) -> int:
    paper_directory.mkdir(parents=True, exist_ok=True)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)

    conn, database_path = open_database(zotero_dir, use_backup)
    rows = load_pdf_items(conn)
    if limit > 0:
        rows = rows[:limit]

    if not rows:
        print("No PDF attachments found in Zotero.", file=sys.stderr)
        return 1

    existing_names = {path.name.lower() for path in paper_directory.glob("*.pdf")}
    imported: list[dict[str, str]] = []

    for row in rows:
        source_pdf = resolve_source_pdf(zotero_dir, row)
        dest_name = build_destination_name(row, existing_names)
        destination = paper_directory / dest_name
        shutil.copy2(source_pdf, destination)
        imported.append(
            {
                "title": row["title"] or "",
                "year": extract_year(row["item_date"]),
                "doi": row["doi"] or "",
                "publication_title": row["publication_title"] or "",
                "parent_key": row["parent_key"],
                "attachment_key": row["attachment_key"],
                "source_pdf": str(source_pdf),
                "destination_pdf": str(destination),
                "database": str(database_path),
            }
        )

    manifest = {
        "database": str(database_path),
        "imported_count": len(imported),
        "items": imported,
    }
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"Imported {len(imported)} PDF(s) from {database_path.name}:")
    for item in imported:
        print(f"- {item['year']} | {item['title']} -> {Path(item['destination_pdf']).name}")
    print(f"Manifest written to: {manifest_path}")
    return 0


def main() -> int:
    args = parse_args()
    try:
        return import_pdfs(
            zotero_dir=args.zotero_dir,
            paper_directory=args.paper_directory,
            manifest_path=args.manifest_path,
            limit=args.limit,
            use_backup=args.use_backup,
        )
    except Exception as exc:
        print(f"Import failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
