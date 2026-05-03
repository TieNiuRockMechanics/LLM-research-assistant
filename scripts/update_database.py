from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
UPDATE_PAPER_SCRIPT = PROJECT_ROOT / "scripts" / "update_paper_database.py"
UPDATE_WIKI_SCRIPT = PROJECT_ROOT / "scripts" / "update_wiki_database.py"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Compatibility wrapper. By default this safely updates only the PaperQA "
            "paper database. Pass --include-wiki to update the LLM Wiki too."
        )
    )
    parser.add_argument("--scan-only", action="store_true")
    parser.add_argument("--include-wiki", action="store_true")
    parser.add_argument("--model", default="")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    parser.add_argument("--zotero-dir", type=Path, default=Path.home() / "Zotero")
    parser.add_argument("--paper-directory", type=Path, default=PROJECT_ROOT / "data" / "papers")
    parser.add_argument("--manifest-path", type=Path, default=PROJECT_ROOT / "data" / "zotero-import-manifest.json")
    parser.add_argument("--index-name", default="papers")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--skip-index", action="store_true")
    parser.add_argument("--use-backup", action="store_true")
    return parser.parse_args()


def build_env(model: str = "") -> dict[str, str]:
    env = os.environ.copy()
    packages_path = str(PROJECT_ROOT / ".packages")
    existing_pythonpath = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = packages_path if not existing_pythonpath else packages_path + os.pathsep + existing_pythonpath
    env["PYTHONUTF8"] = "1"
    if model:
        env["PQA_LLM_MODEL"] = model
        env["PQA_SUMMARY_LLM_MODEL"] = model
        env["PQA_AGENT_LLM_MODEL"] = model
        env["PQA_ENRICHMENT_LLM_MODEL"] = model
    return env


def run_json(command: list[str], model: str = "", timeout_seconds: int = 7200) -> dict:
    result = subprocess.run(
        command,
        cwd=PROJECT_ROOT,
        env=build_env(model),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout_seconds,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError((result.stderr or result.stdout or "").strip() or f"Command failed: {command}")
    text = result.stdout.strip()
    start = text.find("{")
    end = text.rfind("}")
    if start >= 0 and end > start:
        return json.loads(text[start : end + 1])
    return {"stdout": text}


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    args = parse_args()

    paper_command = [
        sys.executable,
        str(UPDATE_PAPER_SCRIPT),
        "--format",
        "json",
        "--zotero-dir",
        str(args.zotero_dir),
        "--paper-directory",
        str(args.paper_directory),
        "--manifest-path",
        str(args.manifest_path),
        "--index-name",
        args.index_name,
    ]
    if args.scan_only:
        paper_command.append("--scan-only")
    if args.limit:
        paper_command.extend(["--limit", str(args.limit)])
    if args.skip_index:
        paper_command.append("--skip-index")
    if args.use_backup:
        paper_command.append("--use-backup")

    payload = {"paper_database": run_json(paper_command)}
    if args.include_wiki and not args.scan_only:
        wiki_command = [
            sys.executable,
            str(UPDATE_WIKI_SCRIPT),
            "--format",
            "json",
            "--index-name",
            args.index_name,
        ]
        if args.model:
            wiki_command.extend(["--model", args.model])
        payload["wiki_database"] = run_json(wiki_command, model=args.model)

    if args.format == "json":
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        paper = payload["paper_database"]
        print(
            f"Paper database: new={paper.get('new_imported_count', paper.get('new_count', 0))}, "
            f"indexed={len(paper.get('indexed_new_files', []))}."
        )
        if "wiki_database" in payload:
            print("LLM Wiki updated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
