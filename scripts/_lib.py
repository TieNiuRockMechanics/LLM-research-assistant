from __future__ import annotations

import hashlib
import json
import os
import pickle
import re
import sys
import zlib
from pathlib import Path
from typing import Any


def load_dotenv(dotenv_path: Path, *, missing_ok: bool = True) -> None:
    """Load .env into os.environ. Uses setdefault to preserve existing values."""
    if not dotenv_path.exists():
        if missing_ok:
            return
        raise FileNotFoundError(f"Missing .env file at {dotenv_path}")
    for raw_line in dotenv_path.read_text(encoding="utf-8-sig").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        os.environ.setdefault(key, value)


def int_env(name: str, default: int, *, allow_zero: bool = True) -> int:
    raw = os.environ.get(name, "").strip()
    if not raw:
        return default
    try:
        value = int(raw)
    except ValueError:
        return default
    if not allow_zero and value <= 0:
        return default
    return value


def float_env(name: str, default: float) -> float:
    try:
        return float(os.environ.get(name, default))
    except (TypeError, ValueError):
        return default


def build_env(
    project_root: Path,
    *,
    model: str = "",
    packages_dir: str | None = None,
) -> dict[str, str]:
    env = os.environ.copy()
    pkg = packages_dir or str(project_root / ".packages")
    existing = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = pkg if not existing else pkg + os.pathsep + existing
    env["PYTHONUTF8"] = "1"
    if model:
        env["PQA_LLM_MODEL"] = model
        env["PQA_SUMMARY_LLM_MODEL"] = model
        env["PQA_AGENT_LLM_MODEL"] = model
        env["PQA_ENRICHMENT_LLM_MODEL"] = model
    return env


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


def count_index_docs(index_name: str, project_root: Path | None = None) -> int:
    root = project_root or Path(__file__).resolve().parents[1]
    index_dir = root / "data" / "indexes" / index_name
    files_zip = index_dir / "files.zip"
    docs_dir = index_dir / "docs"
    if files_zip.exists():
        try:
            return len(pickle.loads(zlib.decompress(files_zip.read_bytes())))
        except Exception:
            pass
    if docs_dir.exists():
        return len([p for p in docs_dir.glob("*") if p.is_file()])
    return 0


def count_pdfs(paper_directory: Path) -> int:
    if not paper_directory.exists():
        return 0
    return len([p for p in paper_directory.glob("*.pdf") if p.is_file()])


def parse_frontmatter_scalar(value: str) -> Any:
    value = value.strip()
    if not value:
        return ""
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return value.strip('"').strip("'")


def parse_simple_frontmatter(content: str) -> dict[str, Any]:
    if not content.startswith("---"):
        return {}
    end = content.find("\n---", 3)
    if end < 0:
        return {}
    fields: dict[str, Any] = {}
    lines = content[3:end].splitlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        if ":" not in line or line.startswith(" "):
            index += 1
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not value:
            items: list[Any] = []
            cursor = index + 1
            while cursor < len(lines):
                child = lines[cursor]
                stripped = child.strip()
                if not stripped:
                    cursor += 1
                    continue
                if stripped.startswith("- "):
                    items.append(parse_frontmatter_scalar(stripped[2:]))
                    cursor += 1
                    continue
                if child.startswith(" ") or child.startswith("\t"):
                    cursor += 1
                    continue
                break
            if items:
                fields[key] = items
                index = cursor
                continue
            index = cursor
            continue
        fields[key] = parse_frontmatter_scalar(value)
        index += 1
    return fields


def frontmatter_strings(fields: dict[str, Any], key: str) -> list[str]:
    value = fields.get(key)
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    text = str(value).strip()
    return [text] if text else []


def strip_frontmatter(content: str) -> str:
    return re.sub(r"\A---\s.*?\n---\s*", "", content, flags=re.DOTALL)


def clean_excerpt(text: str, max_chars: int = 1600) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= max_chars:
        return text
    return text[:max_chars].rsplit(" ", 1)[0] + "..."


def extract_markdown_section(content: str, heading: str) -> str:
    pattern = rf"^##\s+{re.escape(heading)}\s*$\s*(.*?)(?=^##\s+|\Z)"
    match = re.search(pattern, content, flags=re.MULTILINE | re.DOTALL)
    if not match:
        return ""
    section = match.group(1).strip()
    section = re.sub(r"\n{2,}", "\n", section)
    section = re.sub(r"^\s*[-*]\s+", "", section, flags=re.MULTILINE)
    return clean_excerpt(section, max_chars=220)


def markdown_headings(content: str) -> list[str]:
    body = strip_frontmatter(content)
    return [m.group(1).strip() for m in re.finditer(r"^##+\s+(.+?)\s*$", body, flags=re.MULTILINE)]


def configure_stdout() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def configure_runtime(project_root: Path) -> None:
    tmp_dir = project_root / "tmp"
    pqa_home = project_root / ".pqa"
    tmp_dir.mkdir(parents=True, exist_ok=True)
    pqa_home.mkdir(parents=True, exist_ok=True)
    os.environ["TEMP"] = str(tmp_dir)
    os.environ["TMP"] = str(tmp_dir)
    os.environ["PQA_HOME"] = str(pqa_home)
