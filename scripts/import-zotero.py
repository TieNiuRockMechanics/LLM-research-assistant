from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sqlite3
import sys
import unicodedata
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    project_root = Path(__file__).resolve().parents[1]
    default_zotero_dir = Path.home() / "Zotero"
    parser = argparse.ArgumentParser(
        description="Import Zotero PDF attachments into the local paper database."
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
        "--collection",
        default="",
        help="Optional Zotero collection name or collectionID to import from.",
    )
    parser.add_argument(
        "--no-child-collections",
        action="store_true",
        help="When --collection is set, do not include child collections.",
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip attachments already present in the manifest.",
    )
    parser.add_argument(
        "--allowed-item-types",
        default="journalArticle",
        help=(
            "Comma-separated Zotero parent item types allowed into the paper database. "
            "Default: journalArticle. Use 'all' to disable this filter."
        ),
    )
    parser.add_argument(
        "--no-content-dedup",
        action="store_true",
        help="Do not skip PDFs whose SHA256 content hash already exists in the paper database.",
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
        candidates.extend([zotero_dir / "zotero.sqlite", zotero_dir / "zotero.sqlite.bak"])

    last_error: Exception | None = None
    for candidate in candidates:
        if not candidate.exists():
            continue
        try:
            conn = sqlite3.connect(
                f"file:{candidate.as_posix()}?mode=ro&immutable=1",
                uri=True,
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
    normalized = unicodedata.normalize("NFKC", value)
    normalized = re.sub(r'[<>:"/\\|?*]+', " ", normalized)
    normalized = re.sub(r"[\x00-\x1f]+", " ", normalized)
    normalized = re.sub(r"\s+", " ", normalized).strip(" .")
    return normalized or "untitled"


def extract_year(date_value: str | None) -> str:
    if not date_value:
        return "unknown-year"
    match = re.search(r"(19|20)\d{2}", date_value)
    return match.group(0) if match else "unknown-year"


def split_group_concat(value: str | None) -> list[str]:
    if not value:
        return []
    return [part.strip() for part in value.split("||") if part.strip()]


def parse_allowed_item_types(value: str | None) -> set[str]:
    if value is None:
        return {"journalArticle"}
    value = value.strip()
    if not value:
        return {"journalArticle"}
    if value.lower() == "all":
        return set()
    return {part.strip() for part in value.split(",") if part.strip()}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def collection_descendants(conn: sqlite3.Connection, collection_id: int) -> list[int]:
    collection_ids = [collection_id]
    queue = [collection_id]
    while queue:
        current = queue.pop(0)
        rows = conn.execute(
            "SELECT collectionID FROM collections WHERE parentCollectionID = ?",
            (current,),
        )
        for row in rows:
            child_id = int(row["collectionID"])
            if child_id not in collection_ids:
                collection_ids.append(child_id)
                queue.append(child_id)
    return collection_ids


def resolve_collection_ids(
    conn: sqlite3.Connection,
    collection: str,
    include_children: bool,
) -> list[int]:
    collection = collection.strip()
    if not collection:
        return []

    if collection.isdigit():
        row = conn.execute(
            "SELECT collectionID FROM collections WHERE collectionID = ?",
            (int(collection),),
        ).fetchone()
    else:
        row = conn.execute(
            "SELECT collectionID FROM collections WHERE collectionName = ?",
            (collection,),
        ).fetchone()

    if row is None:
        raise ValueError(f"Zotero collection not found: {collection}")

    collection_id = int(row["collectionID"])
    if include_children:
        return collection_descendants(conn, collection_id)
    return [collection_id]


def load_pdf_items(
    conn: sqlite3.Connection,
    collection_ids: list[int] | None = None,
) -> list[sqlite3.Row]:
    collection_join = ""
    collection_where = ""
    params: list[int] = []
    if collection_ids:
        placeholders = ",".join("?" for _ in collection_ids)
        collection_join = "JOIN collectionItems AS collection_item ON collection_item.itemID = parent.itemID"
        collection_where = f"AND collection_item.collectionID IN ({placeholders})"
        params.extend(collection_ids)

    query = f"""
    SELECT
        parent.itemID AS parent_item_id,
        parent.key AS parent_key,
        item_type.typeName AS item_type,
        child.key AS attachment_key,
        attachment.path AS attachment_path,
        MAX(CASE WHEN field.fieldName = 'title' THEN value.value END) AS title,
        MAX(CASE WHEN field.fieldName = 'date' THEN value.value END) AS item_date,
        MAX(CASE WHEN field.fieldName = 'DOI' THEN value.value END) AS doi,
        MAX(CASE WHEN field.fieldName = 'publicationTitle' THEN value.value END) AS publication_title,
        (
            SELECT GROUP_CONCAT(collectionName, '||')
            FROM (
                SELECT DISTINCT collections.collectionName AS collectionName
                FROM collectionItems AS all_collection_items
                JOIN collections
                    ON collections.collectionID = all_collection_items.collectionID
                WHERE all_collection_items.itemID = parent.itemID
                ORDER BY collections.collectionName
            )
        ) AS collections,
        (
            SELECT GROUP_CONCAT(collectionID, '||')
            FROM (
                SELECT DISTINCT collections.collectionID AS collectionID
                FROM collectionItems AS all_collection_items
                JOIN collections
                    ON collections.collectionID = all_collection_items.collectionID
                WHERE all_collection_items.itemID = parent.itemID
                ORDER BY collections.collectionID
            )
        ) AS collection_ids
    FROM itemAttachments AS attachment
    JOIN items AS child
        ON child.itemID = attachment.itemID
    JOIN items AS parent
        ON parent.itemID = attachment.parentItemID
    JOIN itemTypes AS item_type
        ON item_type.itemTypeID = parent.itemTypeID
    {collection_join}
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
        {collection_where}
    GROUP BY parent.itemID, parent.key, child.key, attachment.path
    ORDER BY parent.itemID
    """
    return list(conn.execute(query, params))


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

    base_path = Path(base)
    candidate = base
    counter = 2
    while candidate.lower() in existing_names:
        candidate = f"{base_path.stem} ({counter}){base_path.suffix}"
        counter += 1

    existing_names.add(candidate.lower())
    return candidate


def base_destination_name(row: sqlite3.Row) -> str:
    year = extract_year(row["item_date"])
    title = clean_filename(row["title"] or row["attachment_key"])
    base = f"{year} - {title}.pdf"
    if len(base) > 180:
        base = f"{year} - {title[:160].rstrip()}.pdf"
    return base


def load_manifest(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError:
        return {}


def row_to_manifest_item(
    row: sqlite3.Row,
    *,
    source_pdf: Path | None,
    destination: Path | None,
    database_path: Path,
    status: str,
    content_sha256: str = "",
    duplicate_of: str = "",
    status_reason: str = "",
) -> dict[str, Any]:
    item = {
        "title": row["title"] or "",
        "year": extract_year(row["item_date"]),
        "doi": row["doi"] or "",
        "publication_title": row["publication_title"] or "",
        "item_type": row["item_type"] or "",
        "collections": split_group_concat(row["collections"]),
        "collection_ids": split_group_concat(row["collection_ids"]),
        "parent_key": row["parent_key"],
        "attachment_key": row["attachment_key"],
        "source_pdf": str(source_pdf) if source_pdf is not None else "",
        "destination_pdf": str(destination) if destination is not None else "",
        "database": str(database_path),
        "status": status,
    }
    if content_sha256:
        item["content_sha256"] = content_sha256
    if duplicate_of:
        item["duplicate_of"] = duplicate_of
    if status_reason:
        item["status_reason"] = status_reason
    return item


def import_pdfs(
    zotero_dir: Path,
    paper_directory: Path,
    manifest_path: Path,
    limit: int,
    use_backup: bool,
    collection: str = "",
    include_child_collections: bool = True,
    skip_existing: bool = False,
    failed_directory: Path | None = None,
    allowed_item_types: set[str] | None = None,
    dedupe_by_content: bool = True,
) -> dict[str, Any]:
    paper_directory.mkdir(parents=True, exist_ok=True)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    failed_directory = failed_directory or paper_directory / "_failed-pdf"

    conn, database_path = open_database(zotero_dir, use_backup)
    collection_ids = resolve_collection_ids(conn, collection, include_child_collections)
    rows = load_pdf_items(conn, collection_ids)
    if limit > 0:
        rows = rows[:limit]
    allowed_item_types = {"journalArticle"} if allowed_item_types is None else allowed_item_types
    allow_all_item_types = not allowed_item_types

    old_manifest = load_manifest(manifest_path)
    old_items = old_manifest.get("items", []) if isinstance(old_manifest.get("items"), list) else []
    old_by_attachment = {
        item.get("attachment_key"): item
        for item in old_items
        if item.get("attachment_key") and item.get("destination_pdf")
    }

    existing_names = {path.name.lower() for path in paper_directory.glob("*.pdf")}
    known_hashes: dict[str, str] = {}
    if dedupe_by_content:
        for path in sorted(paper_directory.glob("*.pdf")):
            try:
                known_hashes[sha256_file(path)] = str(path)
            except OSError:
                continue
    failed_by_name = {
        path.name.lower(): path
        for path in failed_directory.glob("*.pdf")
        if failed_directory.exists()
    }
    manifest_items: list[dict[str, Any]] = []
    imported: list[dict[str, Any]] = []
    skipped: list[dict[str, Any]] = []
    missing: list[dict[str, Any]] = []
    excluded: list[dict[str, Any]] = []
    duplicates: list[dict[str, Any]] = []

    for row in rows:
        item_type = row["item_type"] or ""
        if not allow_all_item_types and item_type not in allowed_item_types:
            item = row_to_manifest_item(
                row,
                source_pdf=None,
                destination=None,
                database_path=database_path,
                status="excluded_non_journal",
                status_reason=f"Zotero item type {item_type!r} is not allowed.",
            )
            manifest_items.append(item)
            excluded.append(item)
            continue

        old_item = old_by_attachment.get(row["attachment_key"])
        if skip_existing and old_item:
            destination = Path(old_item["destination_pdf"])
            if destination.exists():
                content_sha256 = old_item.get("content_sha256", "")
                if not content_sha256:
                    try:
                        content_sha256 = sha256_file(destination)
                    except OSError:
                        content_sha256 = ""
                if content_sha256 and dedupe_by_content:
                    known_hashes.setdefault(content_sha256, str(destination))
                old_item = dict(old_item)
                old_item["status"] = "existing"
                old_item["item_type"] = item_type
                if content_sha256:
                    old_item["content_sha256"] = content_sha256
                manifest_items.append(old_item)
                skipped.append(old_item)
                existing_names.add(destination.name.lower())
                continue

        base_destination = paper_directory / base_destination_name(row)
        if skip_existing and base_destination.exists():
            source_pdf = resolve_source_pdf(zotero_dir, row)
            try:
                content_sha256 = sha256_file(base_destination)
            except OSError:
                content_sha256 = ""
            if content_sha256 and dedupe_by_content:
                known_hashes.setdefault(content_sha256, str(base_destination))
            item = row_to_manifest_item(
                row,
                source_pdf=source_pdf,
                destination=base_destination,
                database_path=database_path,
                status="existing",
                content_sha256=content_sha256,
            )
            manifest_items.append(item)
            skipped.append(item)
            existing_names.add(base_destination.name.lower())
            continue

        failed_destination = failed_by_name.get(base_destination.name.lower())
        if skip_existing and failed_destination is not None:
            source_pdf = resolve_source_pdf(zotero_dir, row)
            item = row_to_manifest_item(
                row,
                source_pdf=source_pdf,
                destination=failed_destination,
                database_path=database_path,
                status="failed_existing",
                status_reason="PDF is already in the failed/quarantine directory.",
            )
            manifest_items.append(item)
            skipped.append(item)
            existing_names.add(base_destination.name.lower())
            continue

        try:
            source_pdf = resolve_source_pdf(zotero_dir, row)
        except FileNotFoundError as exc:
            missing_item = {
                "title": row["title"] or "",
                "parent_key": row["parent_key"],
                "attachment_key": row["attachment_key"],
                "error": str(exc),
                "status": "missing_pdf",
            }
            missing.append(missing_item)
            manifest_items.append(missing_item)
            continue

        content_sha256 = ""
        if dedupe_by_content:
            try:
                content_sha256 = sha256_file(source_pdf)
            except OSError as exc:
                missing_item = {
                    "parent_key": row["parent_key"],
                    "attachment_key": row["attachment_key"],
                    "error": str(exc),
                    "status": "unreadable_pdf",
                }
                missing.append(missing_item)
                manifest_items.append(missing_item)
                continue
            duplicate_of = known_hashes.get(content_sha256)
            if duplicate_of:
                item = row_to_manifest_item(
                    row,
                    source_pdf=source_pdf,
                    destination=None,
                    database_path=database_path,
                    status="duplicate_pdf",
                    content_sha256=content_sha256,
                    duplicate_of=duplicate_of,
                    status_reason="Exact PDF content hash already exists in the paper database.",
                )
                manifest_items.append(item)
                duplicates.append(item)
                skipped.append(item)
                continue

        dest_name = build_destination_name(row, existing_names)
        destination = paper_directory / dest_name
        shutil.copy2(source_pdf, destination)
        if dedupe_by_content and content_sha256:
            known_hashes.setdefault(content_sha256, str(destination))
        item = row_to_manifest_item(
            row,
            source_pdf=source_pdf,
            destination=destination,
            database_path=database_path,
            status="imported",
            content_sha256=content_sha256,
        )
        manifest_items.append(item)
        imported.append(item)

    manifest = {
        "database": str(database_path),
        "collection": collection,
        "collection_ids": collection_ids,
        "allowed_item_types": sorted(allowed_item_types) if allowed_item_types else ["all"],
        "paper_directory": str(paper_directory),
        "scanned_count": len(rows),
        "eligible_count": len(rows) - len(excluded),
        "imported_count": len(
            [
                item
                for item in manifest_items
                if item.get("status") in {"imported", "existing", "failed_existing"}
            ]
        ),
        "new_imported_count": len(imported),
        "skipped_existing_count": len(skipped),
        "missing_count": len(missing),
        "excluded_non_journal_count": len(excluded),
        "duplicate_pdf_count": len(duplicates),
        "updated_at": __import__("datetime").datetime.now().isoformat(timespec="seconds"),
        "items": manifest_items,
    }
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return manifest


def print_summary(manifest: dict[str, Any], manifest_path: Path) -> None:
    collection_note = f" collection={manifest.get('collection')!r}" if manifest.get("collection") else ""
    print(
        f"Scanned {manifest['scanned_count']} Zotero PDF attachment(s){collection_note}; "
        f"eligible={manifest.get('eligible_count', 0)}, new={manifest['new_imported_count']}, "
        f"existing/duplicate skipped={manifest['skipped_existing_count']}, "
        f"excluded_non_journal={manifest.get('excluded_non_journal_count', 0)}, "
        f"duplicate_pdf={manifest.get('duplicate_pdf_count', 0)}, missing={manifest['missing_count']}."
    )
    for item in manifest.get("items", []):
        if item.get("status") == "imported":
            print(f"- {item.get('year', '')} | {item.get('title', '')} -> {Path(item['destination_pdf']).name}")
    print(f"Manifest written to: {manifest_path}")


def main() -> int:
    args = parse_args()
    try:
        manifest = import_pdfs(
            zotero_dir=args.zotero_dir,
            paper_directory=args.paper_directory,
            manifest_path=args.manifest_path,
            limit=args.limit,
            use_backup=args.use_backup,
            collection=args.collection,
            include_child_collections=not args.no_child_collections,
            skip_existing=args.skip_existing,
            allowed_item_types=parse_allowed_item_types(args.allowed_item_types),
            dedupe_by_content=not args.no_content_dedup,
        )
    except Exception as exc:
        print(f"Import failed: {exc}", file=sys.stderr)
        return 1
    print_summary(manifest, args.manifest_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
