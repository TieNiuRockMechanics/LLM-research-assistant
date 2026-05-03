from __future__ import annotations

import argparse
import json
import os
import pickle
import re
import shutil
import subprocess
import sys
import zlib
from datetime import datetime
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PQA_SCRIPT = PROJECT_ROOT / "scripts" / "pqa-api.py"
ERROR_FILE_RE = re.compile(r"Error parsing (.+?\.pdf),\s+skipping index", re.DOTALL)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a PaperQA index and quarantine PDFs that cannot be parsed.")
    parser.add_argument("--index-name", default="papers")
    parser.add_argument("--paper-directory", type=Path, default=PROJECT_ROOT / "data" / "papers")
    parser.add_argument("--failed-directory", type=Path, default=PROJECT_ROOT / "data" / "papers" / "_failed-pdf")
    parser.add_argument("--manifest-path", type=Path, default=PROJECT_ROOT / "data" / "zotero-import-manifest.json")
    parser.add_argument(
        "--allowed-item-types",
        default="journalArticle",
        help="Comma-separated Zotero item types allowed to enter the vector index. Default: journalArticle.",
    )
    parser.add_argument("--max-retries", type=int, default=40)
    parser.add_argument("--format", choices=["text", "json"], default="text")
    return parser.parse_args()


def configure_stdout() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def build_env() -> dict[str, str]:
    env = os.environ.copy()
    packages_path = str(PROJECT_ROOT / ".packages")
    existing_pythonpath = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = packages_path if not existing_pythonpath else packages_path + os.pathsep + existing_pythonpath
    env["PYTHONUTF8"] = "1"
    return env


def run_index(index_name: str, paper_directory: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(PQA_SCRIPT),
            "--quiet",
            "index",
            "--index-name",
            index_name,
            "--paper-directory",
            str(paper_directory),
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


def clean_error_filename(raw_name: str) -> str:
    name = re.sub(r"\s+", " ", raw_name).strip()
    return name


def find_failed_pdf(output: str, paper_directory: Path) -> Path | None:
    match = ERROR_FILE_RE.search(output)
    if match:
        name = clean_error_filename(match.group(1))
        candidate = paper_directory / name
        if candidate.exists():
            return candidate
        matches = list(paper_directory.glob(name[:80] + "*.pdf"))
        if matches:
            return matches[0]

    for path in paper_directory.glob("*.pdf"):
        if path.name in output:
            return path
    return None


def quarantine_pdf(path: Path, failed_directory: Path, reason: str) -> Path:
    failed_directory.mkdir(parents=True, exist_ok=True)
    destination = failed_directory / path.name
    counter = 2
    while destination.exists():
        destination = failed_directory / f"{path.stem} ({counter}){path.suffix}"
        counter += 1
    shutil.move(str(path), str(destination))
    reason_path = destination.with_suffix(destination.suffix + ".reason.txt")
    reason_path.write_text(reason[:4000], encoding="utf-8")
    return destination


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
    return len([path for path in paper_directory.glob("*.pdf") if path.is_file()])


def parse_allowed_item_types(value: str) -> set[str]:
    value = value.strip()
    if not value or value.lower() == "all":
        return set()
    return {part.strip() for part in value.split(",") if part.strip()}


def manifest_items_by_pdf_name(manifest_path: Path) -> dict[str, dict]:
    if not manifest_path.exists():
        return {}
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError:
        return {}
    mapping: dict[str, dict] = {}
    for item in manifest.get("items", []):
        if not isinstance(item, dict):
            continue
        destination = item.get("destination_pdf", "")
        if destination:
            mapping[Path(destination).name.lower()] = item
    return mapping


def guard_index_scope(paper_directory: Path, manifest_path: Path, allowed_item_types: set[str]) -> list[str]:
    if not allowed_item_types:
        return []
    manifest_by_name = manifest_items_by_pdf_name(manifest_path)
    problems: list[str] = []
    blocked_statuses = {"excluded_non_journal", "duplicate_pdf"}
    for path in sorted(paper_directory.glob("*.pdf")):
        item = manifest_by_name.get(path.name.lower())
        if not item:
            continue
        status = item.get("status", "")
        item_type = item.get("item_type", "")
        if status in blocked_statuses:
            problems.append(f"{path.name}: manifest status is {status}")
        elif item_type and item_type not in allowed_item_types:
            problems.append(f"{path.name}: Zotero item_type={item_type!r} is not allowed")
    return problems


def main() -> int:
    configure_stdout()
    args = parse_args()
    scope_problems = guard_index_scope(
        args.paper_directory,
        args.manifest_path,
        parse_allowed_item_types(args.allowed_item_types),
    )
    if scope_problems:
        payload = {
            "status": "scope_failed",
            "message": "Refusing to build vector index with non-journal or duplicate PDFs.",
            "problems": scope_problems,
            "paper_count": count_pdfs(args.paper_directory),
            "index_documents": count_index_docs(args.index_name),
            "updated_at": datetime.now().isoformat(timespec="seconds"),
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 1
    quarantined: list[dict[str, str]] = []
    last_result: subprocess.CompletedProcess[str] | None = None

    for attempt in range(1, args.max_retries + 1):
        result = run_index(args.index_name, args.paper_directory)
        last_result = result
        if result.returncode == 0:
            payload = {
                "status": "ok",
                "attempts": attempt,
                "quarantined": quarantined,
                "paper_count": count_pdfs(args.paper_directory),
                "index_documents": count_index_docs(args.index_name),
                "updated_at": datetime.now().isoformat(timespec="seconds"),
            }
            if args.format == "json":
                print(json.dumps(payload, ensure_ascii=False, indent=2))
            else:
                print(f"Index built: {payload['index_documents']} documents; quarantined={len(quarantined)}.")
            return 0

        combined = (result.stdout or "") + "\n" + (result.stderr or "")
        failed_pdf = find_failed_pdf(combined, args.paper_directory)
        if failed_pdf is None:
            break
        destination = quarantine_pdf(failed_pdf, args.failed_directory, combined)
        quarantined.append(
            {
                "source": str(failed_pdf),
                "destination": str(destination),
                "reason": "PaperQA/PDF parser failed while indexing.",
            }
        )

    payload = {
        "status": "failed",
        "quarantined": quarantined,
        "paper_count": count_pdfs(args.paper_directory),
        "index_documents": count_index_docs(args.index_name),
        "stdout": (last_result.stdout if last_result else "")[-4000:],
        "stderr": (last_result.stderr if last_result else "")[-4000:],
        "updated_at": datetime.now().isoformat(timespec="seconds"),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
