from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_WIKI_DIR = PROJECT_ROOT / "wiki"

DASHES = "\u2010\u2011\u2012\u2013\u2014\u2212"
SOURCE_WORD = "\u6765\u6e90"
FULLWIDTH_COLON = "\uff1a"
FULLWIDTH_OPEN = "\uff08"
FULLWIDTH_CLOSE = "\uff09"
FULLWIDTH_SQUARE_OPEN = "\u3010"
FULLWIDTH_SQUARE_CLOSE = "\u3011"


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    fields: dict[str, str] = {}
    for line in text[3:end].splitlines():
        if ":" not in line or line.startswith(" "):
            continue
        key, value = line.split(":", 1)
        value = value.strip().strip('"')
        fields[key.strip()] = value
    return fields


def year_from_fields(fields: dict[str, str], stem: str) -> str:
    for value in (fields.get("paper_id", ""), stem, fields.get("citation", ""), fields.get("title", "")):
        match = re.search(r"\b(19|20)\d{2}\b", value)
        if match:
            return match.group(0)
    return "unknown-year"


def author_from_fields(fields: dict[str, str], stem: str) -> str:
    citation = fields.get("citation", "").strip()
    if citation:
        first = re.split(r"[,，]", citation, maxsplit=1)[0].strip()
        first = re.sub(r"^[\"'“”‘’]+|[\"'“”‘’]+$", "", first).strip()
        first = first.split()[0] if first and re.match(r"^[A-Za-z]+$", first) else first
        if first and not re.match(r"^(19|20)\d{2}$", first):
            return normalize_author_token(first)

    paper_id = fields.get("paper_id") or stem
    match = re.match(r"(?:(?:19|20)\d{2}|unknown-year)-(.+?)(?:-|$)", paper_id)
    if match:
        return normalize_author_token(match.group(1))
    return "Unknown"


def normalize_author_token(author: str) -> str:
    author = author.strip().replace("_", " ").replace("-", " ")
    if not author:
        return "Unknown"
    if re.match(r"^[A-Za-z ]+$", author):
        return " ".join(part.capitalize() for part in author.split())
    return author


def fallback_label(fields: dict[str, str], stem: str) -> str:
    return f"{author_from_fields(fields, stem)} {year_from_fields(fields, stem)}"


def normalize_page_syntax(text: str, *, convert_single_p: bool = False) -> str:
    text = re.sub(rf"(?i)\b(pp?\.\s*\d+)\s*[{DASHES}]\s*(\d+)", r"\1-\2", text)
    text = re.sub(r"(?i)(?<![A-Za-z])pp\.\s*(\d)", r"pp. \1", text)
    if convert_single_p:
        text = re.sub(r"(?i)\bp\.\s*(\d)", r"pp. \1", text)
    text = re.sub(r"(?i)\bpp\.?\s+pp\.", "pp.", text)
    return text


PAGE_LOCATOR_RE = re.compile(
    r"(?i)\bpp?\.\s*"
    r"(?P<pages>\d+(?:\s*-\s*\d+)?(?:\s*,\s*(?:pp?\.\s*)?\d+(?:\s*-\s*\d+)?)*)"
)


def clean_pages(pages: str) -> str:
    pages = normalize_page_syntax(pages, convert_single_p=True)
    pages = re.sub(r"(?i)\bpp?\.\s*", "", pages)
    pages = re.sub(r"\s+", " ", pages)
    pages = re.sub(r"\s*-\s*", "-", pages)
    pages = re.sub(r"\s*,\s*", ", ", pages)
    return pages.strip()


def looks_like_author_year_locator(text: str) -> bool:
    return bool(re.search(r"\b(?:19|20)\d{2}|unknown-year\b", text)) and bool(PAGE_LOCATOR_RE.search(text))


def normalize_bracket_inner(inner: str) -> str:
    inner = normalize_page_syntax(inner.strip(), convert_single_p=True)
    inner = re.sub(r"(?i)\bsource\s*:\s*", "", inner)
    inner = re.sub(rf"^{SOURCE_WORD}\s*[:{FULLWIDTH_COLON}]\s*", "", inner)
    return inner.strip()


def normalize_wrapper_inner(inner: str, label: str) -> str:
    inner = normalize_bracket_inner(inner)
    if not inner:
        return inner

    if inner.startswith("[") and inner.endswith("]"):
        return normalize_page_syntax(inner, convert_single_p=True)

    if "[" in inner and "]" in inner:
        # Parentheses like "(source: [A 2020, pp. 1-2]; [A 2020, pp. 3-4])".
        return normalize_page_syntax(inner, convert_single_p=True)

    if looks_like_author_year_locator(inner):
        return f"[{inner}]"

    locator = PAGE_LOCATOR_RE.search(inner)
    if locator:
        page_parts = [clean_pages(match.group("pages")) for match in PAGE_LOCATOR_RE.finditer(inner)]
        pages = ", ".join(dict.fromkeys(part for part in page_parts if part))
        citation = f"[{label}, pp. {pages}]"
        extra = PAGE_LOCATOR_RE.sub(" ", inner).strip()
        extra = re.sub(r"\s+", " ", extra)
        extra = extra.strip(" ,，;；:：()[]")
        if extra:
            return f"{FULLWIDTH_OPEN}{extra}{FULLWIDTH_CLOSE}{citation}"
        return citation

    return inner


def normalize_inline_citations(text: str, label: str) -> tuple[str, dict[str, int]]:
    stats = {
        "fullwidth_square": 0,
        "fullwidth_paren": 0,
        "ascii_paren": 0,
        "raw_source_pp": 0,
        "loose_pp_format": 0,
    }

    before = text
    text = normalize_page_syntax(text, convert_single_p=False)
    if text != before:
        stats["loose_pp_format"] += 1

    def fullwidth_square_repl(match: re.Match[str]) -> str:
        stats["fullwidth_square"] += 1
        inner = normalize_bracket_inner(match.group(1))
        return f"[{inner}]"

    text = re.sub(rf"{FULLWIDTH_SQUARE_OPEN}([^{FULLWIDTH_SQUARE_CLOSE}\n]+){FULLWIDTH_SQUARE_CLOSE}", fullwidth_square_repl, text)

    def paren_repl(match: re.Match[str]) -> str:
        inner = match.group(1)
        if not re.search(r"(?i)\bpp?\.", inner):
            return match.group(0)
        replacement = normalize_wrapper_inner(inner, label)
        inner_stripped = inner.strip()
        strip_wrapper = (
            "[" in inner_stripped
            and "]" in inner_stripped
            and ("pp." in inner_stripped.lower() or "p." in inner_stripped.lower())
        )
        if replacement == inner and not strip_wrapper:
            return match.group(0)
        stats["fullwidth_paren" if match.group(0).startswith(FULLWIDTH_OPEN) else "ascii_paren"] += 1
        return replacement

    text = re.sub(rf"{FULLWIDTH_OPEN}([^{FULLWIDTH_CLOSE}\n]+){FULLWIDTH_CLOSE}", paren_repl, text)
    text = re.sub(r"\(([^\)\n]+)\)", paren_repl, text)

    raw_source_re = re.compile(
        rf"(?i)(?P<prefix>(?:{SOURCE_WORD}|source)\s*[:{FULLWIDTH_COLON}]\s*)"
        rf"(?P<loc>pp?\.\s*\d+(?:\s*[-{DASHES}]\s*\d+)?"
        rf"(?:\s*,\s*(?:pp?\.\s*)?\d+(?:\s*[-{DASHES}]\s*\d+)?)*)"
    )

    def raw_source_repl(match: re.Match[str]) -> str:
        stats["raw_source_pp"] += 1
        pages = clean_pages(match.group("loc"))
        return f"{match.group('prefix')}[{label}, pp. {pages}]"

    text = raw_source_re.sub(raw_source_repl, text)
    return text, stats


def normalize_file(path: Path) -> tuple[str, dict[str, int]]:
    original = path.read_text(encoding="utf-8", errors="replace")
    fields = parse_frontmatter(original)
    label = fallback_label(fields, path.stem)
    normalized, stats = normalize_inline_citations(original, label)
    stats["changed"] = int(normalized != original)
    return normalized, stats


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize citation labels in LLM Wiki paper pages.")
    parser.add_argument("--wiki-dir", type=Path, default=DEFAULT_WIKI_DIR)
    parser.add_argument("--apply", action="store_true", help="Write normalized files.")
    parser.add_argument("--report", type=Path, default=None)
    args = parser.parse_args()

    papers_dir = args.wiki_dir / "papers"
    files = sorted(papers_dir.glob("*.md"))
    totals: dict[str, int] = {}
    changed_files: list[str] = []
    for path in files:
        normalized, stats = normalize_file(path)
        for key, value in stats.items():
            totals[key] = totals.get(key, 0) + value
        if stats.get("changed"):
            changed_files.append(path.relative_to(PROJECT_ROOT).as_posix())
            if args.apply:
                path.write_text(normalized, encoding="utf-8")

    report = {
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "apply": args.apply,
        "files_scanned": len(files),
        "files_changed": len(changed_files),
        "totals": totals,
        "changed_files": changed_files,
    }
    report_path = args.report
    if report_path is None:
        report_dir = args.wiki_dir / ".staging" / "audits"
        report_dir.mkdir(parents=True, exist_ok=True)
        suffix = "apply" if args.apply else "dry-run"
        report_path = report_dir / f"citation-normalization-{suffix}-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("apply", "files_scanned", "files_changed", "totals")}, ensure_ascii=False, indent=2))
    print(f"report={report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
