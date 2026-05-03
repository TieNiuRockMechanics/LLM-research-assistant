from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import pickle
import re
import sys
import time
import urllib.request
import zlib
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_WIKI_DIR = PROJECT_ROOT / "wiki"
DEFAULT_INDEX_DIR = PROJECT_ROOT / "data" / "indexes" / "wiki_semantic"
INDEX_FILENAME = "index.pkl.zlib"
STATUS_FILENAME = "status.json"
SUPPORTED_FOLDERS = {"papers", "concepts", "methods", "claims", "syntheses", "open-questions"}
AGGREGATE_FOLDERS = {"concepts", "methods", "claims", "syntheses", "open-questions"}


def load_dotenv(dotenv_path: Path) -> None:
    if not dotenv_path.exists():
        return
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


def int_env(name: str, default: int) -> int:
    raw_value = os.environ.get(name, "").strip()
    if not raw_value:
        return default
    try:
        value = int(raw_value)
    except ValueError:
        return default
    return value if value > 0 else default


def embedding_model_name() -> str:
    model = os.environ.get("WIKI_SEMANTIC_EMBEDDING_MODEL", "").strip()
    if not model:
        model = os.environ.get("PQA_EMBEDDING_MODEL", "openai/embedding-3").strip()
    return model.removeprefix("openai/")


def embedding_dimensions() -> int | None:
    raw_value = os.environ.get("WIKI_SEMANTIC_EMBEDDING_DIMENSIONS", "").strip()
    if not raw_value:
        raw_value = os.environ.get("PQA_EMBEDDING_DIMENSIONS", "").strip()
    if not raw_value:
        return None
    try:
        return int(raw_value)
    except ValueError:
        return None


def embedding_base_url() -> str:
    return os.environ.get("WIKI_SEMANTIC_EMBEDDING_BASE_URL", "").strip() or os.environ.get(
        "OPENAI_BASE_URL", "https://open.bigmodel.cn/api/paas/v4"
    ).strip()


def embedding_api_key() -> str:
    return os.environ.get("WIKI_SEMANTIC_EMBEDDING_API_KEY", "").strip() or os.environ.get("OPENAI_API_KEY", "").strip()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="replace")).hexdigest()


def clean_space(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if not value:
        return ""
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return value.strip('"').strip("'")


def parse_frontmatter(content: str) -> dict[str, Any]:
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
                    items.append(parse_scalar(stripped[2:]))
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
        fields[key] = parse_scalar(value)
        index += 1
    return fields


def frontmatter_list(fields: dict[str, Any], key: str) -> list[str]:
    value = fields.get(key)
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    text = str(value).strip()
    return [text] if text else []


def strip_frontmatter(content: str) -> str:
    return re.sub(r"\A---\s.*?\n---\s*", "", content, flags=re.DOTALL).strip()


def first_heading(content: str) -> str:
    match = re.search(r"^#\s+(.+?)\s*$", strip_frontmatter(content), flags=re.MULTILINE)
    return match.group(1).strip() if match else ""


def page_title(path: Path, content: str, fields: dict[str, Any]) -> str:
    candidates = frontmatter_list(fields, "title") + frontmatter_list(fields, "name") + [first_heading(content), path.stem]
    return next((candidate for candidate in candidates if candidate), path.stem)


def source_type_for_folder(folder: str) -> str:
    if folder in AGGREGATE_FOLDERS:
        return "wiki_aggregate"
    if folder == "papers":
        return "wiki_paper_page"
    return "wiki"


def iter_wiki_files(wiki_dir: Path, folders: set[str]) -> list[Path]:
    files: list[Path] = []
    for folder in sorted(folders):
        root = wiki_dir / folder
        if not root.exists():
            continue
        files.extend(sorted(path for path in root.glob("*.md") if path.is_file()))
    return files


def split_markdown_sections(content: str) -> list[tuple[str, str]]:
    body = strip_frontmatter(content)
    body = re.sub(r"## Source Papers\s+.*", "", body, flags=re.DOTALL).strip()
    matches = list(re.finditer(r"^##\s+(.+?)\s*$", body, flags=re.MULTILINE))
    if not matches:
        return [("Page", body)] if body else []
    sections: list[tuple[str, str]] = []
    preface = body[: matches[0].start()].strip()
    if preface:
        sections.append(("Page", preface))
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        heading = match.group(1).strip()
        text = body[start:end].strip()
        if text:
            sections.append((heading, text))
    return sections


def chunk_text(text: str, max_chars: int, overlap_chars: int) -> list[str]:
    text = clean_space(text)
    if not text:
        return []
    if len(text) <= max_chars:
        return [text]
    chunks: list[str] = []
    start = 0
    while start < len(text):
        end = min(start + max_chars, len(text))
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        if end >= len(text):
            break
        start = max(end - overlap_chars, start + 1)
    return chunks


def build_units(wiki_dir: Path, folders: set[str], max_chars: int, overlap_chars: int) -> list[dict[str, Any]]:
    units: list[dict[str, Any]] = []
    for path in iter_wiki_files(wiki_dir, folders):
        relative_path = path.relative_to(wiki_dir).as_posix()
        folder = relative_path.split("/", 1)[0]
        content = path.read_text(encoding="utf-8-sig", errors="replace")
        fields = parse_frontmatter(content)
        title = page_title(path, content, fields)
        aliases = frontmatter_list(fields, "aliases")
        page_hash = sha256_text(content)
        for heading, section_text in split_markdown_sections(content):
            lead = f"Title: {title}"
            if aliases:
                lead += "\nAliases: " + ", ".join(aliases[:8])
            lead += f"\nLayer: {folder}\nSection: {heading}\n"
            for chunk_index, chunk in enumerate(chunk_text(section_text, max_chars=max_chars, overlap_chars=overlap_chars)):
                text = clean_space(lead + "\n" + chunk)
                text_hash = sha256_text(text)
                unit_id = sha256_text(f"{relative_path}\n{heading}\n{chunk_index}\n{text_hash}")[:24]
                units.append(
                    {
                        "id": unit_id,
                        "relative_path": relative_path,
                        "folder": folder,
                        "source_type": source_type_for_folder(folder),
                        "title": title,
                        "aliases": aliases,
                        "heading": heading,
                        "chunk_index": chunk_index,
                        "text": text,
                        "text_hash": text_hash,
                        "page_hash": page_hash,
                        "mtime": path.stat().st_mtime,
                    }
                )
    return units


def normalize_vector(vector: list[float]) -> list[float]:
    norm = math.sqrt(sum(value * value for value in vector))
    if norm <= 0:
        return vector
    return [value / norm for value in vector]


def post_embeddings(texts: list[str], timeout: int) -> list[list[float]]:
    api_key = embedding_api_key()
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY or WIKI_SEMANTIC_EMBEDDING_API_KEY is missing.")
    payload: dict[str, Any] = {"model": embedding_model_name(), "input": texts}
    dimensions = embedding_dimensions()
    if dimensions:
        payload["dimensions"] = dimensions
    request = urllib.request.Request(
        embedding_base_url().rstrip("/") + "/embeddings",
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            data = json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"embedding HTTP {exc.code}: {detail[:500]}") from exc
    except TimeoutError as exc:
        raise RuntimeError(f"embedding timeout after {timeout}s") from exc
    except URLError as exc:
        raise RuntimeError(f"embedding connection failed: {exc.reason}") from exc
    vectors = [item["embedding"] for item in sorted(data["data"], key=lambda item: item.get("index", 0))]
    return [normalize_vector([float(value) for value in vector]) for vector in vectors]


def embed_texts(texts: list[str], batch_size: int, timeout: int) -> list[list[float]]:
    vectors: list[list[float]] = []
    total = len(texts)
    for start in range(0, total, batch_size):
        batch = texts[start : start + batch_size]
        attempts = int_env("WIKI_SEMANTIC_RETRY_ATTEMPTS", 3)
        last_error: Exception | None = None
        for attempt in range(1, attempts + 1):
            try:
                vectors.extend(post_embeddings(batch, timeout=timeout))
                break
            except RuntimeError as exc:
                last_error = exc
                if attempt >= attempts:
                    raise
                time.sleep(min(30, 3 * attempt))
        if last_error and len(vectors) < start + len(batch):
            raise RuntimeError(f"embedding batch failed: {last_error}") from last_error
        print(f"embedded {min(start + len(batch), total)}/{total}", flush=True)
    return vectors


def index_path(index_dir: Path) -> Path:
    return index_dir / INDEX_FILENAME


def status_path(index_dir: Path) -> Path:
    return index_dir / STATUS_FILENAME


def load_index(index_dir: Path) -> dict[str, Any] | None:
    path = index_path(index_dir)
    if not path.exists():
        return None
    return pickle.loads(zlib.decompress(path.read_bytes()))


def save_index(index_dir: Path, payload: dict[str, Any]) -> None:
    index_dir.mkdir(parents=True, exist_ok=True)
    data = zlib.compress(pickle.dumps(payload, protocol=pickle.HIGHEST_PROTOCOL), level=6)
    index_path(index_dir).write_bytes(data)
    status = {
        "updated_at": payload.get("updated_at"),
        "model": payload.get("model"),
        "dimensions": payload.get("dimensions"),
        "unit_count": len(payload.get("records", [])),
        "folders": payload.get("folders", []),
        "index_file": index_path(index_dir).as_posix(),
    }
    status_path(index_dir).write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")


def build_index(
    *,
    wiki_dir: Path,
    index_dir: Path,
    folders: set[str],
    dry_run: bool,
    force: bool,
    limit: int,
) -> dict[str, Any]:
    max_chars = int_env("WIKI_SEMANTIC_CHUNK_CHARS", 1800)
    overlap_chars = int_env("WIKI_SEMANTIC_CHUNK_OVERLAP_CHARS", 160)
    units = build_units(wiki_dir, folders, max_chars=max_chars, overlap_chars=overlap_chars)
    if limit > 0:
        units = units[:limit]
    old_index = load_index(index_dir) if not force else None
    old_by_id = {}
    if old_index:
        old_by_id = {
            record["id"]: record
            for record in old_index.get("records", [])
            if record.get("model") == embedding_model_name()
            and record.get("dimensions") == embedding_dimensions()
            and record.get("text_hash")
        }
    reusable = 0
    to_embed: list[dict[str, Any]] = []
    records: list[dict[str, Any]] = []
    for unit in units:
        old_record = old_by_id.get(unit["id"])
        if old_record and old_record.get("text_hash") == unit["text_hash"] and old_record.get("embedding"):
            record = dict(unit)
            record["embedding"] = old_record["embedding"]
            record["model"] = old_record.get("model")
            record["dimensions"] = old_record.get("dimensions")
            records.append(record)
            reusable += 1
        else:
            to_embed.append(unit)
    summary = {
        "wiki_dir": str(wiki_dir),
        "index_dir": str(index_dir),
        "folders": sorted(folders),
        "unit_count": len(units),
        "reusable_count": reusable,
        "to_embed_count": len(to_embed),
        "model": embedding_model_name(),
        "dimensions": embedding_dimensions(),
        "dry_run": dry_run,
    }
    if dry_run:
        return summary
    if to_embed:
        vectors = embed_texts(
            [unit["text"] for unit in to_embed],
            batch_size=int_env("WIKI_SEMANTIC_EMBEDDING_BATCH_SIZE", 16),
            timeout=int_env("WIKI_SEMANTIC_EMBEDDING_TIMEOUT", 120),
        )
        for unit, vector in zip(to_embed, vectors, strict=True):
            record = dict(unit)
            record["embedding"] = vector
            record["model"] = embedding_model_name()
            record["dimensions"] = embedding_dimensions()
            records.append(record)
    records.sort(key=lambda item: (item["relative_path"], item["heading"], item["chunk_index"]))
    payload = {
        "schema_version": "wiki-semantic-v1",
        "updated_at": datetime.now().isoformat(timespec="seconds"),
        "wiki_dir": str(wiki_dir),
        "model": embedding_model_name(),
        "dimensions": embedding_dimensions(),
        "folders": sorted(folders),
        "records": records,
    }
    save_index(index_dir, payload)
    summary["written"] = True
    summary["index_file"] = str(index_path(index_dir))
    return summary


def cosine(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def query_index(
    project_root: Path,
    query: str,
    *,
    top_k: int = 8,
    folders: set[str] | None = None,
    index_dir: Path | None = None,
) -> list[dict[str, Any]]:
    index_root = index_dir or project_root / "data" / "indexes" / "wiki_semantic"
    payload = load_index(index_root)
    if not payload:
        return []
    records = payload.get("records", [])
    if not records:
        return []
    query_vector = post_embeddings([query], timeout=int_env("WIKI_SEMANTIC_QUERY_TIMEOUT", 60))[0]
    allowed_folders = folders or SUPPORTED_FOLDERS
    hits = []
    wiki_dir = Path(payload.get("wiki_dir") or project_root / "wiki")
    for record in records:
        if record.get("folder") not in allowed_folders:
            continue
        embedding = record.get("embedding")
        if not embedding:
            continue
        score = cosine(query_vector, embedding)
        path = wiki_dir / record["relative_path"]
        hits.append(
            {
                "label": record.get("title") or record["relative_path"],
                "text": record.get("text", ""),
                "source_type": record.get("source_type", "wiki"),
                "path": str(path),
                "folder": record.get("folder", ""),
                "heading": record.get("heading", ""),
                "score": float(score),
                "semantic_score": float(score),
                "relative_path": record["relative_path"],
            }
        )
    hits.sort(key=lambda item: item["score"], reverse=True)
    return hits[:top_k]


def parse_folders(raw_value: str) -> set[str]:
    if not raw_value.strip():
        return set(SUPPORTED_FOLDERS)
    folders = {item.strip() for item in raw_value.split(",") if item.strip()}
    unknown = folders - SUPPORTED_FOLDERS
    if unknown:
        raise ValueError(f"Unsupported wiki folders: {', '.join(sorted(unknown))}")
    return folders


def cmd_status(args: argparse.Namespace) -> int:
    index = load_index(args.index_dir)
    if not index:
        payload = {"exists": False, "index_dir": str(args.index_dir)}
    else:
        payload = {
            "exists": True,
            "index_dir": str(args.index_dir),
            "updated_at": index.get("updated_at"),
            "model": index.get("model"),
            "dimensions": index.get("dimensions"),
            "folders": index.get("folders", []),
            "unit_count": len(index.get("records", [])),
        }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


def cmd_build(args: argparse.Namespace) -> int:
    summary = build_index(
        wiki_dir=args.wiki_dir,
        index_dir=args.index_dir,
        folders=parse_folders(args.folders),
        dry_run=args.dry_run,
        force=args.force,
        limit=args.limit,
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


def cmd_query(args: argparse.Namespace) -> int:
    hits = query_index(
        PROJECT_ROOT,
        args.query,
        top_k=args.top_k,
        folders=parse_folders(args.folders),
        index_dir=args.index_dir,
    )
    print(json.dumps({"hits": hits}, ensure_ascii=False, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build and query a separate semantic index for LLM Wiki Markdown.")
    parser.add_argument("--wiki-dir", type=Path, default=DEFAULT_WIKI_DIR)
    parser.add_argument("--index-dir", type=Path, default=DEFAULT_INDEX_DIR)
    subparsers = parser.add_subparsers(dest="command", required=True)

    status_parser = subparsers.add_parser("status")
    status_parser.set_defaults(func=cmd_status)

    build_parser_ = subparsers.add_parser("build")
    build_parser_.add_argument("--folders", default=",".join(sorted(SUPPORTED_FOLDERS)))
    build_parser_.add_argument("--dry-run", action="store_true")
    build_parser_.add_argument("--force", action="store_true")
    build_parser_.add_argument("--limit", type=int, default=0)
    build_parser_.set_defaults(func=cmd_build)

    query_parser = subparsers.add_parser("query")
    query_parser.add_argument("--folders", default=",".join(sorted(SUPPORTED_FOLDERS)))
    query_parser.add_argument("--top-k", type=int, default=8)
    query_parser.add_argument("query")
    query_parser.set_defaults(func=cmd_query)
    return parser


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    load_dotenv(PROJECT_ROOT / ".env")
    args = build_parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
