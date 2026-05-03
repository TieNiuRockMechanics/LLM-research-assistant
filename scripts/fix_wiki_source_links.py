from __future__ import annotations

import argparse
import json
import re
from difflib import SequenceMatcher
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = PROJECT_ROOT / "wiki"
AGGREGATE_FOLDERS = ["concepts", "methods", "claims", "syntheses", "open-questions"]
SOURCE_ID_ALIASES = {
    "2023-gomez-a-non-parametric": "2023-g-mez-a-non-parametric-discrete-fracture-network-model",
}


def normalize_for_match(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def resolve_paper_id(paper_id: str, paper_ids: set[str]) -> tuple[str | None, str]:
    if paper_id in paper_ids:
        return paper_id, "exact"
    if SOURCE_ID_ALIASES.get(paper_id) in paper_ids:
        return SOURCE_ID_ALIASES[paper_id], "alias"

    prefix = [candidate for candidate in paper_ids if candidate.startswith(paper_id)]
    if len(prefix) == 1:
        return prefix[0], "unique-prefix"
    if len(prefix) > 1:
        return None, "ambiguous-prefix"

    yearless = re.sub(r"^\d{4}-", "", paper_id)
    if yearless != paper_id:
        yearless_matches = [
            candidate
            for candidate in paper_ids
            if re.sub(r"^\d{4}-", "", candidate).startswith(yearless)
        ]
        if len(yearless_matches) == 1:
            return yearless_matches[0], "unique-title-prefix"
        if len(yearless_matches) > 1:
            return None, "ambiguous-title-prefix"

    needle = normalize_for_match(paper_id)
    scored = []
    for candidate in paper_ids:
        score = SequenceMatcher(None, needle, normalize_for_match(candidate)).ratio()
        if score >= 0.86:
            scored.append((score, candidate))
    scored.sort(reverse=True)
    if scored and (len(scored) == 1 or scored[0][0] - scored[1][0] >= 0.04):
        return scored[0][1], f"fuzzy-{scored[0][0]:.3f}"

    return None, "unresolved"


def replacement_patterns(old: str, new: str) -> list[tuple[re.Pattern[str], str]]:
    old_re = re.escape(old)
    return [
        (
            re.compile(rf"\[{old_re}\]\(\.\./papers/{old_re}\.md\)"),
            f"[{new}](../papers/{new}.md)",
        ),
        (
            re.compile(rf'(^\s*-\s*)"{old_re}"(\s*$)', re.MULTILINE),
            rf'\1"{new}"\2',
        ),
        (
            re.compile(rf'(^\s*paper_id:\s*)"{old_re}"(\s*$)', re.MULTILINE),
            rf'\1"{new}"\2',
        ),
    ]


def apply_replacements(content: str, mapping: dict[str, str]) -> tuple[str, int]:
    changed = 0
    for old, new in sorted(mapping.items(), key=lambda item: len(item[0]), reverse=True):
        for pattern, replacement in replacement_patterns(old, new):
            content, count = pattern.subn(replacement, content)
            changed += count
    return content, changed


def main() -> int:
    parser = argparse.ArgumentParser(description="Fix aggregate wiki source links that point to truncated paper ids.")
    parser.add_argument("--apply", action="store_true", help="Write fixes. Default is dry-run.")
    args = parser.parse_args()

    paper_ids = {path.stem for path in (WIKI_DIR / "papers").glob("*.md")}
    missing: dict[str, set[str]] = {}
    for folder in AGGREGATE_FOLDERS:
        for path in (WIKI_DIR / folder).glob("*.md"):
            content = path.read_text(encoding="utf-8-sig", errors="replace")
            for match in re.finditer(r"\]\(\.\./papers/([^)]+)\.md\)", content):
                paper_id = match.group(1)
                if paper_id not in paper_ids:
                    missing.setdefault(paper_id, set()).add(path.relative_to(PROJECT_ROOT).as_posix())

    mapping: dict[str, str] = {}
    unresolved: dict[str, dict[str, object]] = {}
    methods: dict[str, str] = {}
    for paper_id in sorted(missing):
        resolved, method = resolve_paper_id(paper_id, paper_ids)
        if resolved:
            mapping[paper_id] = resolved
            methods[paper_id] = method
        else:
            unresolved[paper_id] = {
                "reason": method,
                "files": sorted(missing[paper_id]),
            }

    changed_files: list[dict[str, object]] = []
    total_replacements = 0
    if mapping:
        for folder in AGGREGATE_FOLDERS:
            for path in (WIKI_DIR / folder).glob("*.md"):
                content = path.read_text(encoding="utf-8-sig", errors="replace")
                new_content, replacements = apply_replacements(content, mapping)
                if replacements:
                    changed_files.append(
                        {
                            "path": path.relative_to(PROJECT_ROOT).as_posix(),
                            "replacements": replacements,
                        }
                    )
                    total_replacements += replacements
                    if args.apply:
                        path.write_text(new_content, encoding="utf-8")

    audit_dir = WIKI_DIR / ".staging" / "audits"
    audit_dir.mkdir(parents=True, exist_ok=True)
    audit_path = audit_dir / "source-link-fix-latest.json"
    audit = {
        "mode": "apply" if args.apply else "dry-run",
        "missing_unique_ids": len(missing),
        "resolved_ids": len(mapping),
        "unresolved_ids": len(unresolved),
        "total_replacements": total_replacements,
        "changed_files": changed_files,
        "mapping": {key: {"to": value, "method": methods[key]} for key, value in mapping.items()},
        "unresolved": unresolved,
    }
    audit_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps(audit, ensure_ascii=False, indent=2))
    return 1 if unresolved else 0


if __name__ == "__main__":
    raise SystemExit(main())
