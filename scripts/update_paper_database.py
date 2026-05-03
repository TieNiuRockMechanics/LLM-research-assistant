from __future__ import annotations

import argparse
import importlib.util
import json
import os
import pickle
import shutil
import subprocess
import sys
import zlib
from datetime import datetime
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
IMPORT_SCRIPT = PROJECT_ROOT / "scripts" / "import-zotero.py"
PQA_SCRIPT = PROJECT_ROOT / "scripts" / "pqa-api.py"


def load_import_module():
    spec = importlib.util.spec_from_file_location("import_zotero", IMPORT_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {IMPORT_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    sys.modules["import_zotero"] = module
    spec.loader.exec_module(module)
    return module


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Safely update the local PaperQA evidence database from Zotero.")
    parser.add_argument("--zotero-dir", type=Path, default=Path.home() / "Zotero")
    parser.add_argument("--paper-directory", type=Path, default=PROJECT_ROOT / "data" / "papers")
    parser.add_argument("--manifest-path", type=Path, default=PROJECT_ROOT / "data" / "zotero-import-manifest.json")
    parser.add_argument("--index-name", default="papers")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--scan-only", action="store_true")
    parser.add_argument("--skip-index", action="store_true")
    parser.add_argument("--use-backup", action="store_true")
    parser.add_argument(
        "--allowed-item-types",
        default="journalArticle",
        help="Comma-separated Zotero item types allowed into the paper database. Default: journalArticle.",
    )
    parser.add_argument("--no-content-dedup", action="store_true")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    return parser.parse_args()


def build_env() -> dict[str, str]:
    env = os.environ.copy()
    packages_path = str(PROJECT_ROOT / ".packages")
    existing_pythonpath = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = packages_path if not existing_pythonpath else packages_path + os.pathsep + existing_pythonpath
    env["PYTHONUTF8"] = "1"
    return env


def count_index_docs(index_name: str) -> int:
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


def count_pdfs(paper_directory: Path) -> int:
    if not paper_directory.exists():
        return 0
    return len([path for path in paper_directory.glob("*.pdf") if path.is_file()])


def scan_zotero(args: argparse.Namespace) -> dict[str, Any]:
    import_zotero = load_import_module()
    conn, _database_path = import_zotero.open_database(args.zotero_dir, args.use_backup)
    rows = import_zotero.load_pdf_items(conn, [])
    if args.limit > 0:
        rows = rows[: args.limit]
    allowed_item_types = import_zotero.parse_allowed_item_types(args.allowed_item_types)
    allow_all_item_types = not allowed_item_types
    manifest = import_zotero.load_manifest(args.manifest_path)
    old_items = manifest.get("items", []) if isinstance(manifest.get("items"), list) else []
    known_attachments = {item.get("attachment_key") for item in old_items if isinstance(item, dict)}
    existing_names = {path.name.lower() for path in args.paper_directory.glob("*.pdf") if path.is_file()}
    failed_dir = args.paper_directory / "_failed-pdf"
    failed_names = {path.name.lower() for path in failed_dir.glob("*.pdf") if path.is_file()}
    existing_hashes: set[str] = set()
    if not args.no_content_dedup:
        for path in sorted(args.paper_directory.glob("*.pdf")):
            try:
                existing_hashes.add(import_zotero.sha256_file(path))
            except OSError:
                continue
    new_rows = []
    excluded_non_journal = []
    duplicate_rows = []
    for row in rows:
        item_type = row["item_type"] or ""
        if not allow_all_item_types and item_type not in allowed_item_types:
            excluded_non_journal.append(row)
            continue
        base_name = import_zotero.base_destination_name(row).lower()
        if row["attachment_key"] in known_attachments or base_name in existing_names or base_name in failed_names:
            continue
        if not args.no_content_dedup:
            try:
                source_pdf = import_zotero.resolve_source_pdf(args.zotero_dir, row)
                if import_zotero.sha256_file(source_pdf) in existing_hashes:
                    duplicate_rows.append(row)
                    continue
            except OSError:
                pass
        new_rows.append(row)
    paper_count = count_pdfs(args.paper_directory)
    index_documents = count_index_docs(args.index_name)
    return {
        "scanned_count": len(rows),
        "eligible_count": len(rows) - len(excluded_non_journal),
        "new_count": len(new_rows),
        "excluded_non_journal_count": len(excluded_non_journal),
        "duplicate_pdf_count": len(duplicate_rows),
        "existing_count": len(rows) - len(new_rows) - len(excluded_non_journal) - len(duplicate_rows),
        "paper_count": paper_count,
        "index_documents": index_documents,
        "index_stale": index_documents != paper_count,
    }


def make_staging_dir() -> Path:
    base = PROJECT_ROOT / "tmp" / "incremental-index"
    base.mkdir(parents=True, exist_ok=True)
    staging = base / datetime.now().strftime("%Y%m%d-%H%M%S")
    staging.mkdir(parents=True, exist_ok=False)
    return staging


def cleanup_staging(path: Path) -> None:
    resolved = path.resolve()
    allowed_root = (PROJECT_ROOT / "tmp" / "incremental-index").resolve()
    if allowed_root not in resolved.parents and resolved != allowed_root:
        raise RuntimeError(f"Refusing to cleanup unexpected path: {resolved}")
    shutil.rmtree(resolved, ignore_errors=True)


def index_new_pdfs(index_name: str, new_items: list[dict[str, Any]]) -> dict[str, Any]:
    staging = make_staging_dir()
    try:
        staged_files: list[str] = []
        for item in new_items:
            source = Path(item["destination_pdf"])
            if not source.exists():
                continue
            destination = staging / source.name
            shutil.copy2(source, destination)
            staged_files.append(source.name)

        if not staged_files:
            return {"returncode": 0, "staged_files": [], "stdout": "", "stderr": ""}

        result = subprocess.run(
            [
                sys.executable,
                str(PQA_SCRIPT),
                "--quiet",
                "index",
                "--index-name",
                index_name,
                "--paper-directory",
                str(staging),
                "--no-sync",
            ],
            cwd=PROJECT_ROOT,
            env=build_env(),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=7200,
            check=False,
        )
        return {
            "returncode": result.returncode,
            "staged_files": staged_files,
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
        }
    finally:
        cleanup_staging(staging)


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    args = parse_args()

    if args.scan_only:
        payload = scan_zotero(args)
        if args.format == "json":
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            print(f"Scanned {payload['scanned_count']} Zotero PDFs; new={payload['new_count']}.")
        return 0

    import_zotero = load_import_module()
    index_documents_before = count_index_docs(args.index_name)
    paper_count_before = count_pdfs(args.paper_directory)
    stale_before = index_documents_before != paper_count_before

    manifest = import_zotero.import_pdfs(
        zotero_dir=args.zotero_dir,
        paper_directory=args.paper_directory,
        manifest_path=args.manifest_path,
        limit=args.limit,
        use_backup=args.use_backup,
        collection="",
        include_child_collections=True,
        skip_existing=True,
        allowed_item_types=import_zotero.parse_allowed_item_types(args.allowed_item_types),
        dedupe_by_content=not args.no_content_dedup,
    )
    new_items = [
        item
        for item in manifest.get("items", [])
        if isinstance(item, dict) and item.get("status") == "imported" and item.get("destination_pdf")
    ]

    index_step: dict[str, Any] | None = None
    index_warning = ""
    if new_items and not args.skip_index:
        if stale_before:
            index_warning = (
                "Index was already stale before this update. "
                "Newly imported PDFs have been indexed, but stale records remain. "
                "Use Advanced Maintenance to repair/rebuild the full index if needed."
            )
        index_step = index_new_pdfs(args.index_name, new_items)
        if index_step["returncode"] != 0:
                payload = {
                    "updated_at": datetime.now().isoformat(timespec="seconds"),
                    "manifest": manifest,
                    "new_imported_count": len(new_items),
                    "paper_count": count_pdfs(args.paper_directory),
                    "index_documents": count_index_docs(args.index_name),
                    "index_step": index_step,
                    "index_warning": index_warning,
                }
                print(json.dumps(payload, ensure_ascii=False, indent=2))
                return 1

    payload = {
        "updated_at": datetime.now().isoformat(timespec="seconds"),
        "new_imported_count": len(new_items),
        "skipped_existing_count": manifest["skipped_existing_count"],
        "missing_count": manifest["missing_count"],
        "excluded_non_journal_count": manifest.get("excluded_non_journal_count", 0),
        "duplicate_pdf_count": manifest.get("duplicate_pdf_count", 0),
        "total_imported_count": manifest["imported_count"],
        "paper_count": count_pdfs(args.paper_directory),
        "index_documents": count_index_docs(args.index_name),
        "index_was_stale": stale_before,
        "ran_index": bool(index_step),
        "indexed_new_files": index_step.get("staged_files", []) if index_step else [],
        "index_warning": index_warning,
    }
    if args.format == "json":
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(
            f"Paper database update complete: new={payload['new_imported_count']}, "
            f"indexed={len(payload['indexed_new_files'])}, "
            f"excluded_non_journal={payload['excluded_non_journal_count']}, "
            f"duplicate_pdf={payload['duplicate_pdf_count']}, missing={payload['missing_count']}."
        )
        if index_warning:
            print(index_warning)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
