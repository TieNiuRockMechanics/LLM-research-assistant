from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
WIKI_SCRIPT = PROJECT_ROOT / "scripts" / "wiki_compile.py"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Update the LLM Wiki knowledge layer from the PaperQA index.")
    parser.add_argument("--index-name", default="papers")
    parser.add_argument("--wiki-dir", type=Path, default=PROJECT_ROOT / "wiki")
    parser.add_argument("--limit", type=int, default=None, help="Optional max indexed papers to process. Omit for all.")
    parser.add_argument(
        "--offset",
        type=int,
        default=0,
        help="Skip this many deduplicated indexed paper records before compiling.",
    )
    parser.add_argument("--max-new", type=int, default=0, help="Max missing paper pages to compile. 0 means no cap.")
    parser.add_argument("--force-papers", action="store_true", help="Regenerate existing paper pages too.")
    parser.add_argument("--aggregate-only", action="store_true", help="Regenerate only aggregate wiki pages.")
    parser.add_argument("--no-aggregate", action="store_true", help="Do not regenerate aggregate wiki pages.")
    parser.add_argument(
        "--resume",
        dest="resume",
        action="store_true",
        default=True,
        help="When forcing, skip only pages already rewritten with the current schema and requested model.",
    )
    parser.add_argument("--no-resume", dest="resume", action="store_false", help="Regenerate current-schema paper pages too.")
    parser.add_argument("--model", default="", help="Optional DeepSeek model override.")
    parser.add_argument("--format", choices=["text", "json"], default="text")
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


def count_pages(wiki_dir: Path, folder: str) -> int:
    path = wiki_dir / folder
    if not path.exists():
        return 0
    return len([item for item in path.glob("*.md") if item.is_file()])


def wiki_counts(wiki_dir: Path) -> dict[str, int]:
    return {
        folder: count_pages(wiki_dir, folder)
        for folder in ["papers", "concepts", "methods", "claims", "syntheses", "open-questions", "inbox"]
    }


def run_wiki_compile(args: argparse.Namespace) -> dict[str, Any]:
    command = [
        sys.executable,
        str(WIKI_SCRIPT),
        "--wiki-dir",
        str(args.wiki_dir),
        "ingest",
        "--index-name",
        args.index_name,
        "--max-new",
        str(args.max_new),
    ]
    if args.limit is not None:
        command.extend(["--limit", str(args.limit)])
    if args.offset:
        command.extend(["--offset", str(args.offset)])
    if args.force_papers:
        command.append("--force")
    if args.resume:
        command.append("--resume")
    else:
        command.append("--no-resume")
    if args.aggregate_only:
        command.append("--aggregate-only")
    if args.no_aggregate:
        command.append("--no-aggregate")
    result = subprocess.run(
        command,
        cwd=PROJECT_ROOT,
        env=build_env(args.model),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=43200 if args.force_papers else 7200,
        check=False,
    )
    payload: dict[str, Any] = {
        "command": command,
        "returncode": result.returncode,
        "stdout": result.stdout.strip(),
        "stderr": result.stderr.strip(),
    }
    return payload


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    args = parse_args()
    before = wiki_counts(args.wiki_dir)
    step = run_wiki_compile(args)
    after = wiki_counts(args.wiki_dir)
    payload = {
        "updated_at": datetime.now().isoformat(timespec="seconds"),
        "model": args.model or os.environ.get("PQA_LLM_MODEL", ""),
        "force_papers": args.force_papers,
        "aggregate_only": args.aggregate_only,
        "no_aggregate": args.no_aggregate,
        "resume": args.resume,
        "counts_before": before,
        "counts_after": after,
        "step": step,
    }
    if args.format == "json":
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(f"LLM Wiki update complete: returncode={step['returncode']}")
        print(json.dumps(after, ensure_ascii=False))
    return 0 if step["returncode"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
