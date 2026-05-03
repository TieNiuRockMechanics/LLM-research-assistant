from __future__ import annotations

import argparse
import importlib.util
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
IMPORT_SCRIPT = PROJECT_ROOT / "scripts" / "import-zotero.py"
INDEX_SCRIPT = PROJECT_ROOT / "scripts" / "index_with_quarantine.py"


def load_import_module():
    spec = importlib.util.spec_from_file_location("import_zotero", IMPORT_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {IMPORT_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    sys.modules["import_zotero"] = module
    spec.loader.exec_module(module)
    return module


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Archive the current local paper database and rebuild a clean journal-article-only PaperQA index."
    )
    parser.add_argument("--zotero-dir", type=Path, default=Path.home() / "Zotero")
    parser.add_argument("--paper-directory", type=Path, default=PROJECT_ROOT / "data" / "papers")
    parser.add_argument("--manifest-path", type=Path, default=PROJECT_ROOT / "data" / "zotero-import-manifest.json")
    parser.add_argument("--index-name", default="papers")
    parser.add_argument("--allowed-item-types", default="journalArticle")
    parser.add_argument("--use-backup", action="store_true")
    parser.add_argument("--skip-index", action="store_true")
    parser.add_argument("--yes", action="store_true", help="Actually archive and rebuild. Without this, print a dry-run plan.")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    return parser.parse_args()


def build_env() -> dict[str, str]:
    env = os.environ.copy()
    packages_path = str(PROJECT_ROOT / ".packages")
    existing_pythonpath = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = packages_path if not existing_pythonpath else packages_path + os.pathsep + existing_pythonpath
    env["PYTHONUTF8"] = "1"
    return env


def safe_project_child(path: Path) -> Path:
    resolved = path.resolve()
    root = PROJECT_ROOT.resolve()
    if resolved != root and root not in resolved.parents:
        raise RuntimeError(f"Refusing to operate outside project root: {resolved}")
    return resolved


def archive_existing(paths: list[Path], archive_dir: Path, *, apply: bool) -> list[dict[str, str]]:
    moves: list[dict[str, str]] = []
    archive_dir = safe_project_child(archive_dir)
    for path in paths:
        resolved = safe_project_child(path)
        if not resolved.exists():
            continue
        target = archive_dir / resolved.relative_to(PROJECT_ROOT.resolve())
        moves.append({"source": str(resolved), "destination": str(target)})
        if apply:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(resolved), str(target))
    return moves


def run_index(args: argparse.Namespace) -> dict[str, Any]:
    result = subprocess.run(
        [
            sys.executable,
            str(INDEX_SCRIPT),
            "--index-name",
            args.index_name,
            "--paper-directory",
            str(args.paper_directory),
            "--manifest-path",
            str(args.manifest_path),
            "--allowed-item-types",
            args.allowed_item_types,
            "--format",
            "json",
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
    try:
        parsed = json.loads(result.stdout)
    except json.JSONDecodeError:
        parsed = {"stdout": result.stdout.strip(), "stderr": result.stderr.strip()}
    parsed["returncode"] = result.returncode
    return parsed


def main() -> int:
    args = parse_args()
    import_zotero = load_import_module()
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    archive_dir = PROJECT_ROOT / "data" / ".archive" / f"paper-database-{stamp}"
    index_dir = PROJECT_ROOT / "data" / "indexes" / args.index_name
    paths_to_archive = [args.paper_directory, index_dir, args.manifest_path]

    moves = archive_existing(paths_to_archive, archive_dir, apply=args.yes)
    payload: dict[str, Any] = {
        "applied": args.yes,
        "archive_dir": str(archive_dir),
        "planned_moves": moves,
    }
    if not args.yes:
        payload["message"] = "Dry run only. Re-run with --yes to archive and rebuild."
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0

    args.paper_directory.mkdir(parents=True, exist_ok=True)
    args.manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest = import_zotero.import_pdfs(
        zotero_dir=args.zotero_dir,
        paper_directory=args.paper_directory,
        manifest_path=args.manifest_path,
        limit=0,
        use_backup=args.use_backup,
        collection="",
        include_child_collections=True,
        skip_existing=False,
        allowed_item_types=import_zotero.parse_allowed_item_types(args.allowed_item_types),
        dedupe_by_content=True,
    )
    payload["manifest"] = {
        "scanned_count": manifest.get("scanned_count", 0),
        "eligible_count": manifest.get("eligible_count", 0),
        "imported_count": manifest.get("imported_count", 0),
        "new_imported_count": manifest.get("new_imported_count", 0),
        "excluded_non_journal_count": manifest.get("excluded_non_journal_count", 0),
        "duplicate_pdf_count": manifest.get("duplicate_pdf_count", 0),
        "missing_count": manifest.get("missing_count", 0),
    }
    if not args.skip_index:
        payload["index_step"] = run_index(args)
        if payload["index_step"].get("returncode") != 0:
            print(json.dumps(payload, ensure_ascii=False, indent=2))
            return 1
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
