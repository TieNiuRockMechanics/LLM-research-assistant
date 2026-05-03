from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_WIKI_DIR = PROJECT_ROOT / "wiki"
GENERATED_ENTRIES = [
    "papers",
    "concepts",
    "methods",
    "claims",
    "syntheses",
    "open-questions",
    "inbox",
    "topics",
    ".staging",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Archive generated LLM Wiki data and recreate empty folders.")
    parser.add_argument("--wiki-dir", type=Path, default=DEFAULT_WIKI_DIR)
    parser.add_argument("--archive-root", type=Path, default=DEFAULT_WIKI_DIR / ".archive")
    parser.add_argument("--yes", action="store_true", help="Actually move files. Without this, print a dry-run plan.")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    return parser.parse_args()


def safe_child(path: Path, parent: Path) -> Path:
    resolved = path.resolve()
    parent_resolved = parent.resolve()
    if resolved != parent_resolved and parent_resolved not in resolved.parents:
        raise RuntimeError(f"Refusing to operate outside {parent_resolved}: {resolved}")
    return resolved


def archive_wiki(wiki_dir: Path, archive_root: Path, *, apply: bool) -> dict:
    wiki_dir = safe_child(wiki_dir, PROJECT_ROOT)
    archive_root = safe_child(archive_root, wiki_dir)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    destination = archive_root / f"llmwiki-abandoned-{stamp}"
    plan = []

    for name in GENERATED_ENTRIES:
        source = wiki_dir / name
        if source.exists():
            plan.append({"source": str(source), "destination": str(destination / name)})

    if apply:
        destination.mkdir(parents=True, exist_ok=False)
        for item in plan:
            source = Path(item["source"])
            target = Path(item["destination"])
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(source), str(target))
        for name in ["papers", "concepts", "methods", "claims", "syntheses", "open-questions", "inbox"]:
            (wiki_dir / name).mkdir(parents=True, exist_ok=True)
        index_path = wiki_dir / "index.md"
        log_path = wiki_dir / "log.md"
        if not index_path.exists():
            index_path.write_text("# LLM Wiki\n\nGenerated wiki data has been archived.\n", encoding="utf-8")
        if not log_path.exists():
            log_path.write_text("# LLM Wiki Log\n", encoding="utf-8")

    return {
        "applied": apply,
        "archive_dir": str(destination),
        "planned_moves": plan,
        "moved_count": len(plan) if apply else 0,
    }


def main() -> int:
    args = parse_args()
    payload = archive_wiki(args.wiki_dir, args.archive_root, apply=args.yes)
    if args.format == "json":
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        verb = "Archived" if payload["applied"] else "Would archive"
        print(f"{verb} {len(payload['planned_moves'])} generated LLM Wiki entries to {payload['archive_dir']}")
        if not payload["applied"]:
            print("Run again with --yes to apply.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
