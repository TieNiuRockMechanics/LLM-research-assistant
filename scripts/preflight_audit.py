from __future__ import annotations

import argparse
import hashlib
import json
import pickle
import sqlite3
import zlib
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Preflight audit before expensive vector or LLM Wiki rebuilds.")
    parser.add_argument("--zotero-dir", type=Path, default=Path.home() / "Zotero")
    parser.add_argument("--paper-directory", type=Path, default=PROJECT_ROOT / "data" / "papers")
    parser.add_argument("--manifest-path", type=Path, default=PROJECT_ROOT / "data" / "zotero-import-manifest.json")
    parser.add_argument("--index-name", default="papers")
    parser.add_argument("--wiki-dir", type=Path, default=PROJECT_ROOT / "wiki")
    parser.add_argument("--allowed-item-types", default="journalArticle")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    return parser.parse_args()


def parse_allowed_item_types(raw: str) -> set[str]:
    raw = raw.strip()
    if not raw or raw.lower() == "all":
        return set()
    return {part.strip() for part in raw.split(",") if part.strip()}


def open_zotero(zotero_dir: Path) -> sqlite3.Connection | None:
    db = zotero_dir / "zotero.sqlite"
    if not db.exists():
        return None
    conn = sqlite3.connect(f"file:{db.as_posix()}?mode=ro&immutable=1", uri=True)
    conn.row_factory = sqlite3.Row
    return conn


def zotero_type_counts(zotero_dir: Path) -> dict[str, int]:
    conn = open_zotero(zotero_dir)
    if conn is None:
        return {}
    rows = conn.execute(
        """
        SELECT itemTypes.typeName AS item_type, COUNT(*) AS pdf_count
        FROM itemAttachments AS attachment
        JOIN items AS child ON child.itemID = attachment.itemID
        JOIN items AS parent ON parent.itemID = attachment.parentItemID
        JOIN itemTypes ON itemTypes.itemTypeID = parent.itemTypeID
        LEFT JOIN deletedItems AS deleted_parent ON deleted_parent.itemID = parent.itemID
        LEFT JOIN deletedItems AS deleted_child ON deleted_child.itemID = child.itemID
        WHERE attachment.contentType = 'application/pdf'
          AND deleted_parent.itemID IS NULL
          AND deleted_child.itemID IS NULL
        GROUP BY itemTypes.typeName
        ORDER BY pdf_count DESC, itemTypes.typeName
        """
    )
    return {str(row["item_type"]): int(row["pdf_count"]) for row in rows}


def load_manifest(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError:
        return {}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def duplicate_pdf_groups(paper_directory: Path) -> list[dict[str, Any]]:
    groups: dict[str, list[str]] = defaultdict(list)
    for path in sorted(paper_directory.glob("*.pdf")):
        groups[sha256_file(path)].append(path.name)
    return [
        {"hash": digest, "count": len(names), "files": names}
        for digest, names in groups.items()
        if len(names) > 1
    ]


def index_document_count(index_name: str) -> int:
    files_zip = PROJECT_ROOT / "data" / "indexes" / index_name / "files.zip"
    if files_zip.exists():
        try:
            return len(pickle.loads(zlib.decompress(files_zip.read_bytes())))
        except Exception:
            pass
    docs_dir = PROJECT_ROOT / "data" / "indexes" / index_name / "docs"
    if not docs_dir.exists():
        return 0
    return len([path for path in docs_dir.iterdir() if path.is_file()])


def wiki_coverage(wiki_dir: Path) -> dict[str, Any]:
    papers_dir = wiki_dir / "papers"
    pages = list(papers_dir.glob("*.md")) if papers_dir.exists() else []
    coverage_counter = Counter()
    schema_counter = Counter()
    partial_pages: list[str] = []
    for path in pages:
        content = path.read_text(encoding="utf-8-sig", errors="replace")
        fields: dict[str, str] = {}
        if content.startswith("---"):
            end = content.find("\n---", 3)
            if end >= 0:
                for line in content[3:end].splitlines():
                    if ":" in line and not line.startswith(" "):
                        key, value = line.split(":", 1)
                        fields[key.strip()] = value.strip().strip('"')
        schema_counter[fields.get("schema_version", "missing")] += 1
        status = fields.get("coverage_status", "missing")
        coverage_counter[status] += 1
        if status != "full-index":
            partial_pages.append(path.name)
    return {
        "paper_pages": len(pages),
        "schema_versions": dict(schema_counter),
        "coverage_statuses": dict(coverage_counter),
        "non_full_coverage_examples": partial_pages[:20],
    }


def audit(args: argparse.Namespace) -> dict[str, Any]:
    allowed_item_types = parse_allowed_item_types(args.allowed_item_types)
    manifest = load_manifest(args.manifest_path)
    manifest_items = manifest.get("items", []) if isinstance(manifest.get("items"), list) else []
    by_status = Counter(str(item.get("status", "")) for item in manifest_items if isinstance(item, dict))
    manifest_missing_item_type = [
        Path(str(item.get("destination_pdf", ""))).name
        for item in manifest_items
        if isinstance(item, dict) and item.get("destination_pdf") and not item.get("item_type")
    ]
    non_allowed_manifest = [
        Path(str(item.get("destination_pdf", ""))).name
        for item in manifest_items
        if isinstance(item, dict)
        and item.get("destination_pdf")
        and allowed_item_types
        and item.get("item_type")
        and item.get("item_type") not in allowed_item_types
    ]
    pdf_count = len(list(args.paper_directory.glob("*.pdf"))) if args.paper_directory.exists() else 0
    duplicates = duplicate_pdf_groups(args.paper_directory) if args.paper_directory.exists() else []
    index_count = index_document_count(args.index_name)

    problems: list[str] = []
    if manifest_missing_item_type:
        problems.append(f"Manifest lacks Zotero item_type for indexed PDFs: {len(manifest_missing_item_type)}")
    if non_allowed_manifest:
        problems.append(f"Manifest still maps non-allowed item types into PDFs: {len(non_allowed_manifest)}")
    if duplicates:
        problems.append(f"Duplicate PDF content groups exist in paper directory: {len(duplicates)}")
    if index_count != pdf_count:
        problems.append(f"Vector index document count ({index_count}) differs from paper PDF count ({pdf_count})")
    wiki_report = wiki_coverage(args.wiki_dir)
    if wiki_report["paper_pages"] and wiki_report["coverage_statuses"].get("full-index", 0) != wiki_report["paper_pages"]:
        problems.append("LLM Wiki paper pages are not all schema-v3 full-index pages")

    return {
        "allowed_item_types": sorted(allowed_item_types) if allowed_item_types else ["all"],
        "zotero_pdf_item_types": zotero_type_counts(args.zotero_dir),
        "manifest_status_counts": dict(by_status),
        "manifest_counts": {
            "scanned_count": manifest.get("scanned_count", 0),
            "eligible_count": manifest.get("eligible_count", 0),
            "imported_count": manifest.get("imported_count", 0),
            "excluded_non_journal_count": manifest.get("excluded_non_journal_count", 0),
            "duplicate_pdf_count": manifest.get("duplicate_pdf_count", 0),
        },
        "manifest_missing_item_type_examples": manifest_missing_item_type[:20],
        "paper_directory_pdf_count": pdf_count,
        "index_document_count": index_count,
        "duplicate_pdf_groups": duplicates[:20],
        "wiki": wiki_report,
        "settings": {
            "pqa_reader_chunk_chars_default": 5000,
            "pqa_reader_overlap_chars_default": 250,
            "pqa_page_size_limit_chars_default": 1_280_000,
            "llm_wiki_paper_stage_char_budget_default": 320000,
            "llm_wiki_paper_stage_char_budget_max_default": 600000,
            "llm_wiki_aggregate_card_char_budget_default": 12000,
            "llm_wiki_aggregate_batch_char_budget_default": 240000,
        },
        "problems": problems,
    }


def main() -> int:
    args = parse_args()
    payload = audit(args)
    if args.format == "json":
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0 if not payload["problems"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
