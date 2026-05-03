from __future__ import annotations

import argparse
import asyncio
import hashlib
import importlib.util
import json
import logging
import os
import re
import shutil
import sqlite3
import sys
import time
import unicodedata
from dataclasses import dataclass, replace
from datetime import datetime
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = PROJECT_ROOT / "wiki"
WIKI_FOLDERS = [
    "papers",
    "concepts",
    "methods",
    "claims",
    "syntheses",
    "open-questions",
    "inbox",
]
AGGREGATE_FOLDERS = ["concepts", "methods", "claims", "syntheses", "open-questions"]
AGGREGATE_KEYS = ["concepts", "methods", "claims", "syntheses", "open_questions"]
SOURCE_ID_ALIASES = {
    "2023-gomez-a-non-parametric": "2023-g-mez-a-non-parametric-discrete-fracture-network-model",
}
PAPER_SCHEMA_VERSION = "paper-v4-2026-04-30"
AGGREGATE_SCHEMA_VERSION = "aggregate-v4-2026-04-30"
PQA_API_PATH = PROJECT_ROOT / "scripts" / "pqa-api.py"


def load_pqa_api():
    spec = importlib.util.spec_from_file_location("pqa_api", PQA_API_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {PQA_API_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


pqa_api = load_pqa_api()


@dataclass
class PaperRecord:
    file_location: str
    paper_id: str
    title: str
    citation: str
    docname: str
    source_pdf: str
    collections: list[str]
    item_type: str
    text_count: int
    text_chars: int
    source_blocks: list[str]


def configure_runtime() -> None:
    tmp_dir = PROJECT_ROOT / "tmp"
    pqa_home = PROJECT_ROOT / ".pqa"
    tmp_dir.mkdir(parents=True, exist_ok=True)
    pqa_home.mkdir(parents=True, exist_ok=True)
    os.environ["TEMP"] = str(tmp_dir)
    os.environ["TMP"] = str(tmp_dir)
    os.environ["PQA_HOME"] = str(pqa_home)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    pqa_api.configure_local_packages(PROJECT_ROOT)
    pqa_api.load_dotenv(PROJECT_ROOT / ".env")
    pqa_api.normalize_provider_env()
    logging.disable(logging.INFO)


def set_wiki_dir(path: Path) -> None:
    global WIKI_DIR
    WIKI_DIR = path if path.is_absolute() else PROJECT_ROOT / path


def ensure_wiki_dirs() -> None:
    WIKI_DIR.mkdir(parents=True, exist_ok=True)
    for folder in WIKI_FOLDERS:
        (WIKI_DIR / folder).mkdir(parents=True, exist_ok=True)
    index_path = WIKI_DIR / "index.md"
    log_path = WIKI_DIR / "log.md"
    if not index_path.exists():
        index_path.write_text("# LLM Wiki\n\nRun `python scripts/wiki_compile.py ingest` to compile papers.\n", encoding="utf-8")
    if not log_path.exists():
        log_path.write_text("# LLM Wiki Log\n", encoding="utf-8")


def clean_text(text: str, max_chars: int | None = None) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if max_chars and len(text) > max_chars:
        return text[:max_chars].rsplit(" ", 1)[0] + "..."
    return text


def clean_filename(value: str) -> str:
    normalized = unicodedata.normalize("NFKC", value)
    normalized = re.sub(r'[<>:"/\\|?*]+', " ", normalized)
    normalized = re.sub(r"[\x00-\x1f]+", " ", normalized)
    normalized = re.sub(r"\s+", " ", normalized).strip(" .")
    return normalized or "untitled"


def clean_markdown_excerpt(text: str, max_chars: int | None = None) -> str:
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    if max_chars and len(text) > max_chars:
        return text[:max_chars].rsplit("\n", 1)[0].strip() + "\n..."
    return text


def int_env(name: str, default: int) -> int:
    raw = os.environ.get(name, "").strip()
    if not raw:
        return default
    try:
        value = int(raw)
    except ValueError:
        return default
    return value if value > 0 else default


def atomic_write_text(path: Path, text: str, encoding: str = "utf-8") -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding=encoding)
    tmp.replace(path)


def atomic_write_json(path: Path, payload: dict[str, Any], encoding: str = "utf-8") -> None:
    atomic_write_text(path, json.dumps(payload, ensure_ascii=False, indent=2), encoding=encoding)


def bool_env(name: str, default: bool = False) -> bool:
    raw = os.environ.get(name, "").strip().lower()
    if not raw:
        return default
    return raw in {"1", "true", "yes", "on", "enabled"}


def aggregate_progress(message: str) -> None:
    line = f"[aggregate] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {message}"
    print(line, flush=True)
    try:
        append_log(f"aggregate: {message}")
    except Exception:
        pass


def aggregate_item_counts(payload: dict[str, Any]) -> dict[str, int]:
    return {key: len(safe_list(payload, key)) for key in AGGREGATE_KEYS}


def strip_frontmatter(content: str) -> str:
    if content.startswith("---"):
        end = content.find("\n---", 3)
        if end >= 0:
            return content[end + 4 :].lstrip()
    return content


def parse_simple_frontmatter(content: str) -> dict[str, str]:
    if not content.startswith("---"):
        return {}
    end = content.find("\n---", 3)
    if end < 0:
        return {}
    fields: dict[str, str] = {}
    for line in content[3:end].splitlines():
        if ":" not in line or line.startswith(" "):
            continue
        key, value = line.split(":", 1)
        value = value.strip().strip('"')
        if value:
            fields[key.strip()] = value
    return fields


def extract_markdown_section(content: str, heading: str) -> str:
    body = strip_frontmatter(content)
    pattern = rf"^##\s+{re.escape(heading)}\s*$\s*(.*?)(?=^##\s+|\Z)"
    match = re.search(pattern, body, flags=re.MULTILINE | re.DOTALL)
    if not match:
        return ""
    return re.sub(r"\n{3,}", "\n\n", match.group(1).strip())


def title_from_citation(citation: str, fallback: str) -> str:
    for pattern in [r"[“\"]([^”\"]{8,180})[”\"]", r"['']([^'']{8,180})['']"]:
        match = re.search(pattern, citation)
        if match:
            return clean_text(match.group(1))
    stem = Path(fallback).stem
    stem = re.sub(r"^\d{4}\s*-\s*", "", stem).strip()
    return stem or "Untitled Paper"


def author_from_citation(citation: str, fallback: str) -> str:
    first = re.split(r",|，|、| and |\s+et\s+al\.?", citation.strip(), maxsplit=1, flags=re.IGNORECASE)[0]
    first = first.strip(" .")
    if first:
        return first
    stem = Path(fallback).stem
    return re.sub(r"^\d{4}\s*-\s*", "", stem).split("-")[0].strip() or "source"


def year_from_text(*parts: str) -> str:
    match = re.search(r"(19|20)\d{2}", " ".join(parts))
    return match.group(0) if match else "unknown-year"


def slugify(text: str, *, max_len: int = 90) -> str:
    text = text.lower().strip()
    text = re.sub(r"[<>:\"/\\|?*\x00-\x1f]+", "-", text)
    text = re.sub(r"[^a-z0-9\u3400-\u9fff]+", "-", text)
    text = re.sub(r"-{2,}", "-", text).strip("-")
    return (text[:max_len].strip("-") or "untitled")


def paper_id_for(file_location: str, citation: str) -> str:
    title = title_from_citation(citation, file_location)
    author = author_from_citation(citation, file_location)
    year = year_from_text(citation, file_location)
    return slugify(f"{year}-{author}-{title}", max_len=96)


def source_pdf_for(file_location: str) -> str:
    path = Path(file_location)
    candidates: list[Path] = []
    if path.is_absolute():
        candidates.append(path)
    else:
        candidates.extend(
            [
                PROJECT_ROOT / file_location,
                PROJECT_ROOT / "data" / "papers" / file_location,
            ]
        )
    for candidate in candidates:
        if candidate.exists():
            return candidate.relative_to(PROJECT_ROOT).as_posix()
    return f"data/papers/{path.name}"


def manifest_items_by_pdf_name() -> dict[str, dict[str, Any]]:
    mapping: dict[str, dict[str, Any]] = {}
    for manifest_path in (PROJECT_ROOT / "data").glob("zotero*-manifest.json"):
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
        except json.JSONDecodeError:
            continue
        for item in manifest.get("items", []):
            if not isinstance(item, dict):
                continue
            destination = item.get("destination_pdf", "")
            if destination:
                mapping[Path(destination).name] = item
    return mapping


def zotero_items_by_pdf_name() -> dict[str, dict[str, Any]]:
    zotero_dir = Path(os.environ.get("ZOTERO_DIR", "")).expanduser() if os.environ.get("ZOTERO_DIR") else Path.home() / "Zotero"
    db_path = zotero_dir / "zotero.sqlite"
    if not db_path.exists():
        return {}
    try:
        conn = sqlite3.connect(f"file:{db_path.as_posix()}?mode=ro&immutable=1", uri=True)
    except sqlite3.Error:
        return {}
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        """
        SELECT
            itemTypes.typeName AS item_type,
            child.key AS attachment_key,
            MAX(CASE WHEN field.fieldName = 'title' THEN value.value END) AS title,
            MAX(CASE WHEN field.fieldName = 'date' THEN value.value END) AS item_date
        FROM itemAttachments AS attachment
        JOIN items AS child
            ON child.itemID = attachment.itemID
        JOIN items AS parent
            ON parent.itemID = attachment.parentItemID
        JOIN itemTypes
            ON itemTypes.itemTypeID = parent.itemTypeID
        LEFT JOIN itemData AS data
            ON data.itemID = parent.itemID
        LEFT JOIN fieldsCombined AS field
            ON field.fieldID = data.fieldID
        LEFT JOIN itemDataValues AS value
            ON value.valueID = data.valueID
        LEFT JOIN deletedItems AS deleted_parent
            ON deleted_parent.itemID = parent.itemID
        LEFT JOIN deletedItems AS deleted_child
            ON deleted_child.itemID = child.itemID
        WHERE attachment.contentType = 'application/pdf'
            AND deleted_parent.itemID IS NULL
            AND deleted_child.itemID IS NULL
        GROUP BY parent.itemID, child.key
        """
    )
    mapping: dict[str, dict[str, Any]] = {}
    for row in rows:
        title = clean_filename(row["title"] or row["attachment_key"])
        year = year_from_text(row["item_date"] or "")
        base = f"{year} - {title}.pdf"
        if len(base) > 180:
            base = f"{year} - {title[:160].rstrip()}.pdf"
        mapping[base.lower()] = {
            "title": row["title"] or "",
            "item_type": row["item_type"] or "",
            "attachment_key": row["attachment_key"] or "",
        }
    return mapping


def allowed_wiki_item_types() -> set[str]:
    raw = os.environ.get("LLM_WIKI_ALLOWED_ITEM_TYPES", "journalArticle").strip()
    if not raw or raw.lower() == "all":
        return set()
    return {part.strip() for part in raw.split(",") if part.strip()}


def json_scalar(value: Any) -> str:
    return json.dumps("" if value is None else str(value), ensure_ascii=False)


def frontmatter(fields: dict[str, Any]) -> str:
    lines = ["---"]
    for key, value in fields.items():
        if isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                if isinstance(item, dict):
                    lines.append("  -")
                    for child_key, child_value in item.items():
                        lines.append(f"    {child_key}: {json_scalar(child_value)}")
                else:
                    lines.append(f"  - {json_scalar(item)}")
        else:
            lines.append(f"{key}: {json_scalar(value)}")
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def strip_code_fence(text: str) -> str:
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json|markdown|md)?\s*", "", text, flags=re.IGNORECASE)
        text = re.sub(r"\s*```$", "", text)
    return text.strip()


def parse_json_response(text: str) -> dict[str, Any]:
    text = strip_code_fence(text)
    try:
        payload = json.loads(text, strict=False)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}")
        if start < 0 or end <= start:
            raise
        payload = json.loads(text[start : end + 1], strict=False)
    if not isinstance(payload, dict):
        raise ValueError("LLM response must be a JSON object.")
    return payload


def repair_json_response(text: str, *, stage: str, error: Exception) -> dict[str, Any]:
    system = (
        "You repair invalid JSON emitted by an LLM. Return only one valid JSON object. "
        "Do not add new facts, do not summarize, and do not wrap the result in markdown."
    )
    prompt = f"""
The following JSON-like output failed to parse during {stage}.

Parser error:
{error}

Repair only syntax issues such as missing commas, bad escaping, trailing text, or code fences.
Preserve all keys and values as much as possible. Return valid JSON only.

Invalid output:
{text}
"""
    repaired, _usage = pqa_api.call_deepseek(
        [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        temperature=0.0,
        timeout=int_env("LLM_WIKI_JSON_REPAIR_TIMEOUT", 240),
    )
    return parse_json_response(repaired)


async def load_index_records(index_name: str, limit: int | None = None) -> list[PaperRecord]:
    from paperqa.agents.search import SearchDocumentStorage, SearchIndex

    index = SearchIndex(
        index_name=index_name,
        index_directory=PROJECT_ROOT / "data" / "indexes",
        storage=SearchDocumentStorage.PICKLE_COMPRESSED,
    )
    index_files = await index.index_files
    manifest_by_pdf = manifest_items_by_pdf_name()
    zotero_by_pdf = zotero_items_by_pdf_name()
    allowed_types = allowed_wiki_item_types()
    skipped_by_type: dict[str, int] = {}
    unknown_type_count = 0
    records: list[PaperRecord] = []
    for file_location in sorted(index_files.keys()):
        file_name = Path(file_location).name
        manifest_item = manifest_by_pdf.get(file_name, {})
        zotero_item = zotero_by_pdf.get(file_name.lower(), {})
        item_type = str(
            zotero_item.get("item_type") or manifest_item.get("item_type") or "unknown"
        )
        if allowed_types and item_type != "unknown" and item_type not in allowed_types:
            skipped_by_type[item_type] = skipped_by_type.get(item_type, 0) + 1
            print(
                f"skip non-allowed Zotero item type {item_type}: {file_name}",
                file=sys.stderr,
                flush=True,
            )
            continue
        if item_type == "unknown":
            unknown_type_count += 1
        try:
            docs = await index.get_saved_object(file_location)
        except FileNotFoundError:
            print(f"skip missing saved object {file_location}", file=sys.stderr)
            continue
        if docs is None:
            continue
        doc_values = list(docs.docs.values())
        doc = doc_values[0] if doc_values else None
        citation = ""
        docname = ""
        if doc is not None:
            citation = getattr(doc, "formatted_citation", "") or getattr(doc, "citation", "")
            docname = getattr(doc, "docname", "")
        citation = citation or docname or file_location
        collections = manifest_item.get("collections", [])
        if not isinstance(collections, list):
            collections = []
        title = title_from_citation(citation, file_location)
        paper_id = paper_id_for(file_location, citation)
        source_blocks: list[str] = []
        for text_obj in docs.texts:
            label = pqa_api.citation_label(text_obj)
            excerpt = clean_text(getattr(text_obj, "text", ""))
            if not excerpt:
                continue
            block = f"[{label}]\n{excerpt}"
            source_blocks.append(block)
        records.append(
            PaperRecord(
                file_location=file_location,
                paper_id=paper_id,
                title=title,
                citation=citation,
                docname=docname,
                source_pdf=source_pdf_for(file_location),
                collections=[str(item) for item in collections],
                item_type=item_type,
                text_count=len(docs.texts),
                text_chars=sum(len(getattr(text, "text", "") or "") for text in docs.texts),
                source_blocks=source_blocks,
            )
        )
        if limit is not None and len(records) >= limit:
            break
    if skipped_by_type:
        aggregate_progress(f"skipped non-allowed Zotero item types: {skipped_by_type}")
    if unknown_type_count:
        aggregate_progress(f"indexed records with unknown Zotero item type kept for review: {unknown_type_count}")
    return records


def compile_paper_page_legacy_unused(record: PaperRecord) -> str:
    source_text = "\n\n".join(record.source_blocks)
    system = (
        "你是一个严谨的科研 LLM Wiki 编译器。你的任务是把论文索引片段整理成可长期维护的 Markdown 知识页。"
        "只能依据给定片段写作；不确定的信息必须标注为未从索引片段中确认。"
        "你的输出要服务于后续 RAG 问答：既要有人能读，也要模型能从中抽取证据、条件、限制和关系。"
    )
    prompt = f"""
请为下面论文生成一页中文 LLM Wiki Markdown。只输出 Markdown 正文，不要输出 YAML front matter，不要使用代码块。

论文 ID: {record.paper_id}
题名: {record.title}
引用: {record.citation}
PDF: {record.source_pdf}
Zotero collection tags: {", ".join(record.collections) if record.collections else "none"}
索引片段数: {record.text_count}

写作规则：
- 保留论文的真实来源，不要编造作者、结论、页码或实验细节。
- 任何非平凡结论都要在句末保留来源标签，例如 [Wang 2018, pp. 3-4]。
- 如果片段不足以判断，写“未从索引片段中确认”。
- Reusable Claims 必须是可以复用到写作中的具体 claim，不要写泛泛总结；每条尽量包含适用条件、证据和限制。
- Core Evidence Table 用 Markdown 表格，列为 Evidence / Source / Conditions / Notes。不要放没有来源标签的证据。
- Assumptions / Conditions 写清楚模型、实验、数据或场景成立的前提。
- Key Variables / Parameters 提取文中关键变量、指标、参数、公式名或控制因素；没有就写“未从索引片段中确认”。
- Connections To Other Work 只根据片段中能确认的内容写；如果没有直接关系，写可从主题上连接到哪些 Candidate Concepts/Methods，不要编造具体论文关系。
- Candidate Concepts 和 Candidate Methods 使用 Obsidian 风格双链，例如 [[fracture reservoir]]。
- Source Coverage 要说明本页依据了多少索引片段、覆盖是否偏摘要/方法/结果、哪些重要信息可能缺失。

必须使用以下标题结构：

# {record.title}

## One-line Summary

## Research Question

## Study Area / Data

## Methods

## Key Findings

## Core Evidence Table

## Limitations

## Assumptions / Conditions

## Key Variables / Parameters

## Reusable Claims

## Candidate Concepts

## Candidate Methods

## Connections To Other Work

## Open Questions

## Source Coverage

论文片段：

{source_text}
"""
    body, _usage = pqa_api.call_deepseek(
        [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        temperature=0.1,
        timeout=int(os.environ.get("LLM_WIKI_PAPER_TIMEOUT", "600")),
    )
    return strip_code_fence(body)


PAPER_STAGE_SCHEMA_VERSION = "paper-stage-v1-2026-04-30"


def paper_source_signature(record: PaperRecord) -> str:
    digest = hashlib.sha1()
    digest.update(record.file_location.encode("utf-8", errors="ignore"))
    digest.update(record.citation.encode("utf-8", errors="ignore"))
    digest.update(str(record.text_count).encode("ascii"))
    digest.update(str(record.text_chars).encode("ascii"))
    for block in record.source_blocks:
        digest.update(block.encode("utf-8", errors="ignore"))
    return digest.hexdigest()


def model_slug() -> str:
    return slugify(os.environ.get("PQA_LLM_MODEL", "model"), max_len=70)


def paper_stage_checkpoint_path(record: PaperRecord, stage_index: int, stage_count: int) -> Path:
    return (
        WIKI_DIR
        / ".staging"
        / "paper-stages"
        / model_slug()
        / record.paper_id
        / f"stage-{stage_index:03d}-of-{stage_count:03d}.json"
    )


def paper_stage_system_prompt() -> str:
    return (
        "You are a rigorous research evidence extractor for an LLM Wiki. "
        "Use only the supplied indexed fragments. Do not invent authors, pages, data, or conclusions. "
        "Facts must keep their source labels. Return valid JSON only."
    )


def paper_stage_schema_prompt() -> str:
    return """
Return exactly one JSON object with these keys:
{
  "schema_version": "paper-stage-v1-2026-04-30",
  "one_line_summary": "...",
  "research_question": "...",
  "study_area_data": ["..."],
  "methods": ["..."],
  "key_findings": ["..."],
  "evidence": [
    {"evidence": "...", "source": "[Author Year, pp. x-y]", "conditions": "...", "notes": "..."}
  ],
  "limitations": ["..."],
  "assumptions_conditions": ["..."],
  "variables_parameters": ["..."],
  "reusable_claims": [
    {"claim": "...", "source": "[Author Year, pp. x-y]", "condition": "...", "limitation": "..."}
  ],
  "candidate_concepts": ["[[concept name]]"],
  "candidate_methods": ["[[method name]]"],
  "connections": ["..."],
  "open_questions": ["..."],
  "coverage_notes": "..."
}

Rules:
- Keep concrete source labels in evidence and reusable_claims.
- Prefer precise, reusable research facts over broad summaries.
- If a field is not supported by the supplied fragments, write "not-confirmed-from-current-fragments".
- Do not include markdown fences.
"""


def load_stage_checkpoint(path: Path, *, signature: str, stage_index: int, stage_count: int) -> dict[str, Any] | None:
    if not path.exists():
        return None
    try:
        payload = json.loads(path.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError:
        return None
    meta = payload.get("_meta", {})
    if not isinstance(meta, dict):
        return None
    if (
        meta.get("source_signature") == signature
        and meta.get("stage_index") == stage_index
        and meta.get("stage_count") == stage_count
        and meta.get("model") == os.environ.get("PQA_LLM_MODEL", "")
        and payload.get("schema_version") == PAPER_STAGE_SCHEMA_VERSION
    ):
        return payload
    return None


def save_stage_checkpoint(
    path: Path,
    payload: dict[str, Any],
    *,
    record: PaperRecord,
    signature: str,
    stage_index: int,
    stage_count: int,
    source_block_count: int,
    source_chars: int,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload["_meta"] = {
        "paper_id": record.paper_id,
        "stage_index": stage_index,
        "stage_count": stage_count,
        "source_block_count": source_block_count,
        "source_chars": source_chars,
        "source_signature": signature,
        "model": os.environ.get("PQA_LLM_MODEL", ""),
        "compiled_at": datetime.now().isoformat(timespec="seconds"),
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def compile_paper_stage(
    record: PaperRecord,
    stage_blocks: list[str],
    *,
    stage_index: int,
    stage_count: int,
    signature: str,
) -> dict[str, Any]:
    source_text = "\n\n".join(stage_blocks)
    source_chars = sum(len(block) for block in stage_blocks)
    checkpoint = paper_stage_checkpoint_path(record, stage_index, stage_count)
    cached = load_stage_checkpoint(
        checkpoint,
        signature=signature,
        stage_index=stage_index,
        stage_count=stage_count,
    )
    if cached is not None:
        print(f"reuse paper stage {record.paper_id} {stage_index}/{stage_count}", flush=True)
        return cached

    prompt = f"""
Extract structured evidence for one segment of a paper.

Paper ID: {record.paper_id}
Title: {record.title}
Citation: {record.citation}
PDF: {record.source_pdf}
Zotero collection tags: {", ".join(record.collections) if record.collections else "none"}
Stage: {stage_index}/{stage_count}
Stage source fragments: {len(stage_blocks)}
Stage source characters: {source_chars}

{paper_stage_schema_prompt()}

Indexed fragments for this stage:
{source_text}
"""
    raw, _usage = pqa_api.call_deepseek(
        [
            {"role": "system", "content": paper_stage_system_prompt()},
            {"role": "user", "content": prompt},
        ],
        temperature=0.1,
        timeout=int_env("LLM_WIKI_PAPER_STAGE_TIMEOUT", 900),
    )
    try:
        payload = parse_json_response(raw)
    except Exception as exc:
        payload = repair_json_response(raw, stage=f"paper stage {record.paper_id}", error=exc)
    payload["schema_version"] = PAPER_STAGE_SCHEMA_VERSION
    save_stage_checkpoint(
        checkpoint,
        payload,
        record=record,
        signature=signature,
        stage_index=stage_index,
        stage_count=stage_count,
        source_block_count=len(stage_blocks),
        source_chars=source_chars,
    )
    return payload


def compile_paper_stage_merge(record: PaperRecord, payloads: list[dict[str, Any]], *, round_index: int) -> dict[str, Any]:
    prompt = f"""
Merge these stage-level evidence JSON objects into one consolidated paper-level evidence JSON.
Use only the supplied JSON objects. Preserve source labels, conditions, and limitations.
Return valid JSON only and keep the same schema.

Paper ID: {record.paper_id}
Title: {record.title}
Citation: {record.citation}

Schema:
{paper_stage_schema_prompt()}

Stage JSON objects:
{json.dumps(payloads, ensure_ascii=False, indent=2)}
"""
    raw, _usage = pqa_api.call_deepseek(
        [
            {"role": "system", "content": paper_stage_system_prompt()},
            {"role": "user", "content": prompt},
        ],
        temperature=0.1,
        timeout=int_env("LLM_WIKI_PAPER_MERGE_TIMEOUT", 900),
    )
    try:
        payload = parse_json_response(raw)
    except Exception as exc:
        payload = repair_json_response(raw, stage=f"paper merge {record.paper_id} round {round_index}", error=exc)
    payload["schema_version"] = PAPER_STAGE_SCHEMA_VERSION
    payload["_meta"] = {
        "paper_id": record.paper_id,
        "merge_round": round_index,
        "merged_payloads": len(payloads),
        "model": os.environ.get("PQA_LLM_MODEL", ""),
        "compiled_at": datetime.now().isoformat(timespec="seconds"),
    }
    return payload


def consolidate_paper_payloads(record: PaperRecord, payloads: list[dict[str, Any]]) -> list[dict[str, Any]]:
    merge_budget = int_env("LLM_WIKI_PAPER_MERGE_CHAR_BUDGET", 240000)
    current = payloads
    round_index = 1
    while len(json.dumps(current, ensure_ascii=False)) > merge_budget and len(current) > 1:
        cards = [json.dumps(payload, ensure_ascii=False, indent=2) for payload in current]
        batches = chunk_texts(cards, max_chars=merge_budget)
        merged: list[dict[str, Any]] = []
        for batch in batches:
            batch_payloads = [json.loads(item) for item in batch]
            merged.append(compile_paper_stage_merge(record, batch_payloads, round_index=round_index))
        current = merged
        round_index += 1
        if round_index > int_env("LLM_WIKI_PAPER_MAX_MERGE_ROUNDS", 4):
            raise RuntimeError(
                f"Paper {record.paper_id} did not converge after paper merge rounds; refusing to truncate."
            )
    return current


def compile_paper_final_markdown(
    record: PaperRecord,
    payloads: list[dict[str, Any]],
    coverage: dict[str, Any],
) -> str:
    prompt = f"""
Write one Chinese LLM Wiki Markdown page for this paper from the structured evidence JSON.
Do not output YAML front matter. Do not use markdown code fences.

Paper ID: {record.paper_id}
Title: {record.title}
Citation: {record.citation}
PDF: {record.source_pdf}
Coverage audit: {json.dumps(coverage, ensure_ascii=False)}

Writing rules:
- This page is evidence for future RAG, not a polished literature-review answer.
- Keep factual claims tied to source labels.
- Source labels must use ASCII square brackets exactly like `[Author Year, pp. x-y]`.
- Do not wrap source labels in parentheses, do not use full-width brackets, do not use `p. x`, `pp.x`, or Unicode page-range dashes.
- For a single page locator, still use `pp. x`.
- Explanations and organization may be synthesized, but unsupported facts must be marked as not confirmed.
- The required Markdown headings below are a machine-readable contract. Use them exactly as written in English.
- Do not translate, rename, number, reorder, or omit the required headings, even if the section body is Chinese.
- Reusable Claims must be concrete claims usable in scientific writing, with condition and limitation.
- Core Evidence Table must have columns: Evidence / Source / Conditions / Notes.
- Candidate Concepts and Candidate Methods should use Obsidian-style wikilinks, e.g. [[fracture reservoir]].
- Source Coverage must explicitly state the coverage ratio and whether all indexed fragments were processed.

Required headings:
# {record.title}

## One-line Summary

## Research Question

## Study Area / Data

## Methods

## Key Findings

## Core Evidence Table

## Limitations

## Assumptions / Conditions

## Key Variables / Parameters

## Reusable Claims

## Candidate Concepts

## Candidate Methods

## Connections To Other Work

## Open Questions

## Source Coverage

Structured evidence JSON:
{json.dumps(payloads, ensure_ascii=False, indent=2)}
"""
    body, _usage = pqa_api.call_deepseek(
        [
            {
                "role": "system",
                "content": (
                    "You compile structured paper evidence into durable LLM Wiki markdown. "
                    "Use only supplied evidence. Preserve source labels. Return markdown only."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.1,
        timeout=int_env("LLM_WIKI_PAPER_FINAL_TIMEOUT", 900),
    )
    return strip_code_fence(body)


def compile_paper_page(record: PaperRecord) -> tuple[str, dict[str, Any]]:
    char_budget = int_env("LLM_WIKI_PAPER_SINGLE_PASS_CHAR_BUDGET", 320000)
    if not record.source_blocks:
        raise RuntimeError(f"No indexed text fragments found for {record.paper_id}; refusing to create an empty wiki page.")
    signature = paper_source_signature(record)
    source_text = "\n\n".join(record.source_blocks)
    compiled_source_blocks = len(record.source_blocks)
    compiled_source_chars = sum(len(block) for block in record.source_blocks)
    if compiled_source_chars > char_budget:
        raise ValueError(
            f"source_chars_exceed_single_pass_budget: {compiled_source_chars} > {char_budget}"
        )
    coverage = {
        "indexed_texts": record.text_count,
        "indexed_chars": record.text_chars,
        "nonempty_source_blocks": len(record.source_blocks),
        "compiled_source_blocks": compiled_source_blocks,
        "compiled_source_chars": compiled_source_chars,
        "stage_count": 1,
        "single_pass_char_budget": char_budget,
        "coverage_ratio_by_blocks": round(compiled_source_blocks / max(len(record.source_blocks), 1), 6),
        "coverage_ratio_by_chars": round(compiled_source_chars / max(record.text_chars, 1), 6),
        "source_signature": signature,
        "coverage_status": "full-index",
        "compile_strategy": "single-pass-markdown",
    }
    prompt = f"""
Write one Chinese LLM Wiki Markdown page for this paper from all indexed fragments.
Do not output YAML front matter. Do not use markdown code fences.

Paper ID: {record.paper_id}
Title: {record.title}
Citation: {record.citation}
PDF: {record.source_pdf}
Zotero item type: {record.item_type}
Zotero collection tags: {", ".join(record.collections) if record.collections else "none"}
Coverage audit: {json.dumps(coverage, ensure_ascii=False)}

Writing rules:
- Use only the supplied indexed fragments. Do not invent authors, pages, data, or conclusions.
- This page is evidence for future RAG, not a polished literature-review answer.
- Keep factual claims tied to source labels already present in the fragments.
- Source labels must use ASCII square brackets exactly like `[Author Year, pp. x-y]`.
- Do not wrap source labels in parentheses, do not use full-width brackets, do not use `p. x`, `pp.x`, or Unicode page-range dashes.
- For a single page locator, still use `pp. x`.
- Explanations and organization may be synthesized, but unsupported facts must be marked as not confirmed.
- The required Markdown headings below are a machine-readable contract. Use them exactly as written in English.
- Do not translate, rename, number, reorder, or omit the required headings, even if the section body is Chinese.
- Reusable Claims must be concrete claims usable in scientific writing, with condition and limitation.
- Core Evidence Table must have columns: Evidence / Source / Conditions / Notes.
- Candidate Concepts and Candidate Methods should use Obsidian-style wikilinks, e.g. [[fracture reservoir]].
- Source Coverage must explicitly state that all non-empty indexed fragments were processed and include the coverage numbers.

Required headings:
# {record.title}

## One-line Summary

## Research Question

## Study Area / Data

## Methods

## Key Findings

## Core Evidence Table

## Limitations

## Assumptions / Conditions

## Key Variables / Parameters

## Reusable Claims

## Candidate Concepts

## Candidate Methods

## Connections To Other Work

## Open Questions

## Source Coverage

Indexed fragments:
{source_text}
"""
    body, _usage = pqa_api.call_deepseek(
        [
            {
                "role": "system",
                "content": (
                    "You compile complete indexed paper fragments into a durable LLM Wiki markdown page. "
                    "Use only supplied evidence. Preserve source labels. Return markdown only."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.1,
        timeout=int_env("LLM_WIKI_PAPER_SINGLE_PASS_TIMEOUT", 900),
    )
    return strip_code_fence(body), coverage


def write_paper_page(record: PaperRecord, body: str, coverage: dict[str, Any] | None = None) -> Path:
    path = WIKI_DIR / "papers" / f"{record.paper_id}.md"
    body = normalize_paper_markdown_structure(body)
    missing_sections = [section for section in PAPER_REQUIRED_SECTIONS if f"## {section}" not in body]
    if missing_sections:
        sample = ", ".join(missing_sections[:5])
        raise ValueError(
            f"paper_body_missing_required_sections for {record.paper_id}: "
            f"{sample}{'...' if len(missing_sections) > 5 else ''}"
        )
    fields = {
        "type": "paper",
        "schema_version": PAPER_SCHEMA_VERSION,
        "paper_id": record.paper_id,
        "title": record.title,
        "status": "draft",
        "source_pdf": record.source_pdf,
        "collections": record.collections,
        "citation": record.citation,
        "indexed_texts": record.text_count,
        "indexed_chars": record.text_chars,
        "nonempty_source_blocks": (coverage or {}).get("nonempty_source_blocks", record.text_count),
        "compiled_source_blocks": (coverage or {}).get("compiled_source_blocks", record.text_count),
        "compiled_source_chars": (coverage or {}).get("compiled_source_chars", record.text_chars),
        "compiled_stage_count": (coverage or {}).get("stage_count", 1),
        "single_pass_char_budget": (coverage or {}).get("single_pass_char_budget", 0),
        "compile_strategy": (coverage or {}).get("compile_strategy", ""),
        "coverage_ratio_by_blocks": (coverage or {}).get("coverage_ratio_by_blocks", 1),
        "coverage_ratio_by_chars": (coverage or {}).get("coverage_ratio_by_chars", 1),
        "coverage_status": (coverage or {}).get("coverage_status", "unknown"),
        "source_signature": (coverage or {}).get("source_signature", ""),
        "compiled_model": os.environ.get("PQA_LLM_MODEL", ""),
        "compiled_at": datetime.now().isoformat(timespec="seconds"),
    }
    atomic_write_text(path, frontmatter(fields) + body.strip() + "\n")
    return path


PAPER_REQUIRED_SECTIONS = [
    "One-line Summary",
    "Research Question",
    "Study Area / Data",
    "Methods",
    "Key Findings",
    "Core Evidence Table",
    "Limitations",
    "Assumptions / Conditions",
    "Key Variables / Parameters",
    "Reusable Claims",
    "Candidate Concepts",
    "Candidate Methods",
    "Connections To Other Work",
    "Open Questions",
    "Source Coverage",
]

PAPER_HEADING_ALIASES = {
    "一行总结": "One-line Summary",
    "一句话总结": "One-line Summary",
    "一句话摘要": "One-line Summary",
    "单行摘要": "One-line Summary",
    "研究问题": "Research Question",
    "研究区域/数据": "Study Area / Data",
    "研究区域 / 数据": "Study Area / Data",
    "研究区/数据": "Study Area / Data",
    "研究区 / 数据": "Study Area / Data",
    "研究区域与数据": "Study Area / Data",
    "方法": "Methods",
    "主要发现": "Key Findings",
    "关键发现": "Key Findings",
    "核心证据表": "Core Evidence Table",
    "局限": "Limitations",
    "局限性": "Limitations",
    "假设/条件": "Assumptions / Conditions",
    "假设 / 条件": "Assumptions / Conditions",
    "假设与条件": "Assumptions / Conditions",
    "假设/约束条件": "Assumptions / Conditions",
    "关键变量/参数": "Key Variables / Parameters",
    "关键变量 / 参数": "Key Variables / Parameters",
    "可复用声明": "Reusable Claims",
    "可复用的声明": "Reusable Claims",
    "可复用断言": "Reusable Claims",
    "可复用的断言": "Reusable Claims",
    "可重用主张": "Reusable Claims",
    "可重复使用的主张": "Reusable Claims",
    "候选概念": "Candidate Concepts",
    "候选方法": "Candidate Methods",
    "与其他工作的联系": "Connections To Other Work",
    "与其他工作的关联": "Connections To Other Work",
    "开放问题": "Open Questions",
    "待解决问题": "Open Questions",
    "未解决问题": "Open Questions",
    "来源覆盖": "Source Coverage",
    "源覆盖": "Source Coverage",
    "源文献覆盖": "Source Coverage",
}

CORE_EVIDENCE_HEADER_ALIASES = {
    "| 证据 | 来源 | 条件 | 备注 |",
    "| 证据 | 来源 | 条件 / 情境 | 附注 |",
    "| 证据 / Evidence | 来源 / Source | 条件 / Conditions | 注释 / Notes |",
    "| 证据 / Evidence | 来源 / Source | 条件 / Conditions | 备注 / Notes |",
    "| 证据（Evidence） | 来源（Source） | 条件（Conditions） | 注释（Notes） |",
}


def normalize_paper_markdown_structure(body: str) -> str:
    """Keep paper pages machine-readable even if the model localizes headings."""
    lines = body.splitlines()
    normalized: list[str] = []
    normalize_next_table_separator = False
    for line in lines:
        heading_match = re.match(r"^(##\s+)(.+?)(\s*)$", line)
        if heading_match:
            prefix, heading, suffix = heading_match.groups()
            canonical = PAPER_HEADING_ALIASES.get(heading.strip())
            if canonical:
                line = f"{prefix}{canonical}{suffix}"
            normalize_next_table_separator = line.strip() == "## Core Evidence Table"
            normalized.append(line)
            continue

        if line.strip() in CORE_EVIDENCE_HEADER_ALIASES:
            normalized.append("| Evidence | Source | Conditions | Notes |")
            normalize_next_table_separator = True
            continue

        if normalize_next_table_separator and re.match(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$", line):
            normalized.append("|----------|--------|------------|-------|")
            normalize_next_table_separator = False
            continue

        if line.strip():
            normalize_next_table_separator = False
        normalized.append(line)

    return "\n".join(normalized).strip() + "\n"


def paper_page_complete(path: Path, required_model: str = "") -> bool:
    if not path.exists():
        return False
    content = path.read_text(encoding="utf-8-sig", errors="replace")
    fields = parse_simple_frontmatter(content)
    if fields.get("schema_version") != PAPER_SCHEMA_VERSION:
        return False
    if required_model and fields.get("compiled_model") != required_model:
        return False
    if fields.get("coverage_status") != "full-index":
        return False
    return all(f"## {section}" in content for section in PAPER_REQUIRED_SECTIONS)


def record_signature(record: PaperRecord) -> tuple[Any, ...]:
    return (
        record.title,
        record.citation,
        record.text_count,
        record.text_chars,
        tuple(record.source_blocks[:3]),
    )


def unique_collision_id(record: PaperRecord, seen_ids: set[str]) -> str:
    digest = hashlib.sha1(record.file_location.encode("utf-8", errors="ignore")).hexdigest()[:8]
    candidate = f"{record.paper_id}-{digest}"
    counter = 2
    while candidate in seen_ids:
        candidate = f"{record.paper_id}-{digest}-{counter}"
        counter += 1
    return candidate


def deduplicate_records(records: list[PaperRecord]) -> list[PaperRecord]:
    unique: list[PaperRecord] = []
    seen: dict[str, PaperRecord] = {}
    for record in records:
        existing = seen.get(record.paper_id)
        if existing is None:
            seen[record.paper_id] = record
            unique.append(record)
            continue

        if record_signature(existing) == record_signature(record):
            print(
                "skip duplicate paper_id "
                f"{record.paper_id}: {Path(record.file_location).name}",
                file=sys.stderr,
            )
            continue

        new_id = unique_collision_id(record, set(seen))
        print(
            f"paper_id collision {record.paper_id}: using {new_id} for {Path(record.file_location).name}",
            file=sys.stderr,
        )
        updated = replace(record, paper_id=new_id)
        seen[new_id] = updated
        unique.append(updated)
    return unique


def load_paper_pages(active_paper_ids: set[str] | None = None) -> list[tuple[Path, str]]:
    papers_dir = WIKI_DIR / "papers"
    if not papers_dir.exists():
        return []
    pages = []
    for path in sorted(papers_dir.glob("*.md")):
        if active_paper_ids is not None and path.stem not in active_paper_ids:
            continue
        if not paper_page_complete(path, os.environ.get("PQA_LLM_MODEL", "")):
            continue
        pages.append((path, path.read_text(encoding="utf-8-sig", errors="replace")))
    return pages


def progress_paths(run_id: str) -> tuple[Path, Path]:
    progress_dir = WIKI_DIR / ".staging" / "progress"
    progress_dir.mkdir(parents=True, exist_ok=True)
    return progress_dir / f"paper-run-{run_id}.json", progress_dir / "latest-paper-run.json"


def write_progress(run_id: str, payload: dict[str, Any]) -> None:
    path, latest = progress_paths(run_id)
    shard_group = os.environ.get("LLM_WIKI_SHARD_GROUP_ID", "").strip()
    shard_count = os.environ.get("LLM_WIKI_SHARD_COUNT", "").strip()
    shard_index = os.environ.get("LLM_WIKI_SHARD_INDEX", "").strip()
    shard_payload: dict[str, Any] = {}
    if shard_group:
        shard_payload["shard_group"] = shard_group
    if shard_count:
        shard_payload["shard_count"] = int(shard_count)
    if shard_index:
        shard_payload["shard_index"] = int(shard_index)
    payload = {
        "run_id": run_id,
        "updated_at": datetime.now().isoformat(timespec="seconds"),
        **shard_payload,
        **payload,
    }
    text = json.dumps(payload, ensure_ascii=False, indent=2)
    atomic_write_text(path, text)
    atomic_write_text(latest, text)


def estimate_eta(started_at: float, completed: int, remaining: int) -> dict[str, Any]:
    if completed <= 0:
        return {"avg_seconds_per_completed": None, "eta_seconds": None, "eta_at": None}
    elapsed = max(time.time() - started_at, 0)
    avg = elapsed / completed
    eta_seconds = int(avg * remaining)
    eta_at = datetime.fromtimestamp(time.time() + eta_seconds).isoformat(timespec="seconds")
    return {
        "avg_seconds_per_completed": round(avg, 2),
        "eta_seconds": eta_seconds,
        "eta_at": eta_at,
    }


def skipped_records_path(run_id: str) -> Path:
    path = WIKI_DIR / ".staging" / "skipped-papers" / f"{run_id}.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def append_skipped_record(run_id: str, record: PaperRecord, *, reason: str, details: dict[str, Any]) -> None:
    payload = {
        "run_id": run_id,
        "paper_id": record.paper_id,
        "title": record.title,
        "file_location": record.file_location,
        "source_pdf": record.source_pdf,
        "item_type": record.item_type,
        "reason": reason,
        "details": details,
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }
    with skipped_records_path(run_id).open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=False) + "\n")


def skipped_paper_ids_by_reason(reason: str) -> set[str]:
    skipped_dir = WIKI_DIR / ".staging" / "skipped-papers"
    ids: set[str] = set()
    if not skipped_dir.exists():
        return ids
    for path in skipped_dir.glob("*.jsonl"):
        for line in path.read_text(encoding="utf-8-sig", errors="replace").splitlines():
            if not line.strip():
                continue
            try:
                payload = json.loads(line)
            except json.JSONDecodeError:
                continue
            if payload.get("reason") == reason and payload.get("paper_id"):
                ids.add(str(payload["paper_id"]))
    return ids


AGGREGATE_CARD_SECTIONS = [
    "One-line Summary",
    "Research Question",
    "Study Area / Data",
    "Methods",
    "Key Findings",
    "Core Evidence Table",
    "Limitations",
    "Assumptions / Conditions",
    "Key Variables / Parameters",
    "Reusable Claims",
    "Candidate Concepts",
    "Candidate Methods",
    "Connections To Other Work",
    "Open Questions",
    "Source Coverage",
]


def language_profile(text: str) -> dict[str, Any]:
    cjk = sum("\u4e00" <= ch <= "\u9fff" for ch in text)
    latin = sum(("a" <= ch.lower() <= "z") for ch in text)
    ratio = cjk / max(cjk + latin, 1)
    if ratio >= 0.30:
        language = "zh"
    elif ratio >= 0.08:
        language = "mixed"
    else:
        language = "en"
    return {"language": language, "cjk_chars": cjk, "latin_chars": latin, "cjk_ratio": round(ratio, 3)}


def aggregate_card(path: Path, content: str, *, max_chars: int) -> str:
    fields = parse_simple_frontmatter(content)
    paper_id = fields.get("paper_id") or path.stem
    title = fields.get("title") or path.stem
    citation = fields.get("citation", "")
    collections = fields.get("collections", "")
    body = strip_frontmatter(content)
    lang = language_profile(body)
    section_budget = max(180, max_chars // 10)
    parts = [
        f"FILE: {path.relative_to(WIKI_DIR).as_posix()}",
        f"paper_id: {paper_id}",
        f"title: {title}",
        f"content_language: {lang['language']}",
        f"cjk_ratio: {lang['cjk_ratio']}",
    ]
    if citation:
        parts.append(f"citation: {clean_text(citation, max_chars=420)}")
    if collections:
        parts.append(f"zotero_collections: {collections}")

    for heading in AGGREGATE_CARD_SECTIONS:
        section = extract_markdown_section(content, heading)
        if section:
            parts.append(f"## {heading}\n{clean_markdown_excerpt(section, max_chars=section_budget)}")

    card = "\n".join(parts)
    return clean_markdown_excerpt(card, max_chars=max_chars)


def chunk_texts(items: list[str], *, max_chars: int) -> list[list[str]]:
    batches: list[list[str]] = []
    current: list[str] = []
    used = 0
    for item in items:
        item_len = len(item) + 2
        if item_len > max_chars:
            print(
                f"Warning: single item ({item_len} chars) exceeds batch budget ({max_chars} chars); "
                "this batch may fail at the LLM layer. Consider increasing the budget or splitting the source.",
                file=sys.stderr,
                flush=True,
            )
        if current and used + item_len > max_chars:
            batches.append(current)
            current = []
            used = 0
        current.append(item)
        used += item_len
    if current:
        batches.append(current)
    return batches


def aggregate_limits(*, final: bool) -> dict[str, int]:
    if final:
        return {
            "concepts": int_env("LLM_WIKI_MAX_CONCEPTS", 60),
            "methods": int_env("LLM_WIKI_MAX_METHODS", 60),
            "claims": int_env("LLM_WIKI_MAX_CLAIMS", 120),
            "syntheses": int_env("LLM_WIKI_MAX_SYNTHESES", 40),
            "open_questions": int_env("LLM_WIKI_MAX_OPEN_QUESTIONS", 30),
        }
    return {
        "concepts": int_env("LLM_WIKI_BATCH_MAX_CONCEPTS", 20),
        "methods": int_env("LLM_WIKI_BATCH_MAX_METHODS", 20),
        "claims": int_env("LLM_WIKI_BATCH_MAX_CLAIMS", 35),
        "syntheses": int_env("LLM_WIKI_BATCH_MAX_SYNTHESES", 12),
        "open_questions": int_env("LLM_WIKI_BATCH_MAX_OPEN_QUESTIONS", 10),
    }


def aggregate_schema_prompt(limits: dict[str, int]) -> str:
    return f"""
返回一个 JSON 对象，字段必须是：

{{
  "concepts": [
    {{
      "name": "...",
      "slug": "...",
      "definition": "...",
      "aliases": ["..."],
      "boundary": "这个概念适用/不适用的边界",
      "related_methods": ["method-slug-or-name"],
      "related_claims": ["claim-slug-or-short-claim"],
      "sources": ["paper_id"]
    }}
  ],
  "methods": [
    {{
      "name": "...",
      "slug": "...",
      "aliases": ["..."],
      "purpose": "...",
      "workflow": "...",
      "inputs": ["..."],
      "outputs": ["..."],
      "assumptions": ["..."],
      "strengths": ["..."],
      "limitations": ["..."],
      "related_concepts": ["concept-slug-or-name"],
      "sources": ["paper_id"]
    }}
  ],
  "claims": [
    {{
      "claim": "...",
      "slug": "...",
      "evidence": "...",
      "condition": "...",
      "limitation": "...",
      "confidence": "low|medium|high",
      "status": "provisional|supported|contested",
      "sources": [{{"paper_id": "...", "locator": "..."}}],
      "supports": ["claim-slug-or-short-claim"],
      "contradicts": ["claim-slug-or-short-claim"]
    }}
  ],
  "syntheses": [
    {{
      "title": "...",
      "slug": "...",
      "central_question": "...",
      "summary": "...",
      "evidence_chain": ["..."],
      "disagreements": ["..."],
      "boundary_conditions": ["..."],
      "writing_uses": ["..."],
      "sources": ["paper_id"]
    }}
  ],
  "open_questions": [
    {{
      "question": "...",
      "slug": "...",
      "why_it_matters": "...",
      "current_evidence": "...",
      "needed_evidence": "...",
      "sources": ["paper_id"]
    }}
  ]
}}

数量上限：
- concepts 不超过 {limits["concepts"]} 条。
- methods 不超过 {limits["methods"]} 条。
- claims 不超过 {limits["claims"]} 条。
- syntheses 不超过 {limits["syntheses"]} 条。
- open_questions 不超过 {limits["open_questions"]} 条。

硬性规则：
- 输入 paper card 的正文可能是中文、英文或中英混合；必须同等理解，不要因为语言不同而丢弃证据。
- 输出 JSON 的解释性字段必须使用简体中文，包括 definition、boundary、purpose、workflow、claim、evidence、condition、limitation、summary、open_questions。
- 英文原始术语、方法名、缩写、变量名和公式必须保留在 aliases、括号说明或字段正文中；不要把专业术语只译成中文而丢掉英文锚点。
- name 字段优先使用中文学术名称；如果没有稳定中文译名，可用英文原名。
- aliases 必须包含重要英文原词、缩写、常见中文别名，服务于后续中英双路检索。
- slug 只能使用小写英文、数字和连字符；如果中文概念没有合适英文 slug，请翻译成简短英文 slug。
- sources 只能使用输入材料中的 paper_id，不要编造 paper_id。
- claims 必须是具体、可引用、可被支持或反驳的科研判断。
- condition 和 limitation 不能空；如果材料不足，写 "not-confirmed-from-current-pages"。
- locator 尽量使用 paper page 中已有的页码标签，例如 pp. 3-4；没有页码时写 "not-confirmed-from-current-pages"。
- 合并重复或高度相近的概念、方法和 claim，不要换一个 slug 重复写同一条知识。
- syntheses 必须体现跨论文关系，不要只写单篇论文摘要。
- 只返回 JSON，不要解释。
"""


def aggregate_category_schema_prompt(category: str, limit: int) -> str:
    schemas = {
        "concepts": """
{
  "concepts": [
    {
      "name": "...",
      "slug": "...",
      "definition": "...",
      "aliases": ["..."],
      "boundary": "...",
      "related_methods": ["method-slug-or-name"],
      "related_claims": ["claim-slug-or-short-claim"],
      "sources": ["paper_id"]
    }
  ]
}
""",
        "methods": """
{
  "methods": [
    {
      "name": "...",
      "slug": "...",
      "aliases": ["..."],
      "purpose": "...",
      "workflow": "...",
      "inputs": ["..."],
      "outputs": ["..."],
      "assumptions": ["..."],
      "strengths": ["..."],
      "limitations": ["..."],
      "related_concepts": ["concept-slug-or-name"],
      "sources": ["paper_id"]
    }
  ]
}
""",
        "claims": """
{
  "claims": [
    {
      "claim": "...",
      "slug": "...",
      "evidence": "...",
      "condition": "...",
      "limitation": "...",
      "confidence": "low|medium|high",
      "status": "provisional|supported|contested",
      "sources": [{"paper_id": "...", "locator": "..."}],
      "supports": ["claim-slug-or-short-claim"],
      "contradicts": ["claim-slug-or-short-claim"]
    }
  ]
}
""",
        "syntheses": """
{
  "syntheses": [
    {
      "title": "...",
      "slug": "...",
      "central_question": "...",
      "summary": "...",
      "evidence_chain": ["..."],
      "disagreements": ["..."],
      "boundary_conditions": ["..."],
      "writing_uses": ["..."],
      "sources": ["paper_id"]
    }
  ]
}
""",
        "open_questions": """
{
  "open_questions": [
    {
      "question": "...",
      "slug": "...",
      "why_it_matters": "...",
      "current_evidence": "...",
      "needed_evidence": "...",
      "sources": ["paper_id"]
    }
  ]
}
""",
    }
    if category not in schemas:
        raise ValueError(f"Unsupported aggregate category: {category}")
    return f"""
Return exactly one valid JSON object with exactly this top-level key: "{category}".
Do not include any other top-level keys.

Schema:
{schemas[category].strip()}

Hard limit: return no more than {limit} items in "{category}".

Rules:
- Use Simplified Chinese for explanatory fields such as definition, boundary, purpose, workflow, evidence, condition, limitation, summary, disagreements, and open questions.
- Preserve important English technical terms, abbreviations, variables, and method names in aliases or parentheses.
- Merge duplicate, near-duplicate, and synonymous items across batches.
- Keep source paper_id values exactly as supplied. Do not invent paper_id values.
- Preserve conditions, limitations, disagreements, and contested evidence instead of smoothing them away.
- Prefer reusable knowledge units that support later RAG answers, not one-paper summaries.
- Return JSON only. No markdown and no explanation.
"""


def aggregate_payload_from_cards(
    cards: list[str],
    *,
    final: bool,
    stage: str,
    checkpoint_path: Path | None = None,
) -> dict[str, Any]:
    if checkpoint_path and checkpoint_path.exists():
        try:
            payload = json.loads(checkpoint_path.read_text(encoding="utf-8"))
            aggregate_progress(
                f"reuse checkpoint stage={stage} path={checkpoint_path.relative_to(PROJECT_ROOT).as_posix()} "
                f"counts={aggregate_item_counts(payload)}"
            )
            return payload
        except (OSError, json.JSONDecodeError) as exc:
            aggregate_progress(f"ignore invalid checkpoint stage={stage} error={exc}")

    limits = aggregate_limits(final=final)
    system = (
        "你是科研 LLM Wiki 的结构化编目器。"
        "你根据已生成的 paper pages 或批次候选结果，抽取和去重概念、方法、可复用 claims、综合主题和开放问题。"
        "输入材料可能混合中文和英文；你要跨语言归并同义概念和方法。"
        "输出的知识层面向中文学术讨论，解释性内容使用简体中文，同时保留英文术语、缩写和变量作为 aliases 或括注。"
        "输出要服务于后续 RAG 问答，因此必须保留证据、条件、限制和来源关系。"
    )
    prompt = f"""
任务阶段: {stage}

处理语言规则:
- 输入 paper cards 的 content_language 只是提示；不能作为过滤条件。
- 将中文页和英文页视为同一证据池，按语义归并同义概念、同类方法和相近 claims。
- 输出统一服务中文学术讨论：解释、判断、条件、限制、综合主题、开放问题都用简体中文。
- 保留英文原术语、缩写、变量和方法名，放入 aliases 或中文后的括号说明，以便后续中英双路检索。
- 不要逐篇摘要；重点抽取能跨论文复用、比较、支持或限制的知识单元。

{aggregate_schema_prompt(limits)}

输入材料:

{chr(10).join(cards)}
"""
    char_count = sum(len(card) for card in cards)
    timeout = int_env("LLM_WIKI_AGGREGATE_TIMEOUT", 300)
    aggregate_progress(
        f"start stage={stage} final={final} cards={len(cards)} chars={char_count} timeout={timeout}s"
    )
    started = time.perf_counter()
    try:
        raw, usage = pqa_api.call_deepseek(
            [
                {"role": "system", "content": system},
                {"role": "user", "content": prompt},
            ],
            temperature=0.1,
            timeout=timeout,
        )
        elapsed = time.perf_counter() - started
        aggregate_progress(
            f"response stage={stage} elapsed={elapsed:.1f}s raw_chars={len(raw)} usage={usage}"
        )
        if checkpoint_path:
            checkpoint_path.parent.mkdir(parents=True, exist_ok=True)
            raw_path = checkpoint_path.with_name(f"{checkpoint_path.name}.raw.txt")
            raw_path.write_text(raw, encoding="utf-8")
            aggregate_progress(f"saved raw response stage={stage} path={raw_path.relative_to(PROJECT_ROOT).as_posix()}")
        try:
            payload = parse_json_response(raw)
        except Exception as parse_exc:
            aggregate_progress(f"parse failed stage={stage}; attempting json repair error={parse_exc}")
            payload = repair_json_response(raw, stage=stage, error=parse_exc)
            if checkpoint_path:
                repaired_path = checkpoint_path.with_name(f"{checkpoint_path.name}.repaired.json")
                repaired_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
                aggregate_progress(
                    f"saved repaired json stage={stage} path={repaired_path.relative_to(PROJECT_ROOT).as_posix()}"
                )
    except Exception as exc:
        elapsed = time.perf_counter() - started
        aggregate_progress(f"failed stage={stage} elapsed={elapsed:.1f}s error={exc}")
        raise

    counts = aggregate_item_counts(payload)
    aggregate_progress(f"parsed stage={stage} counts={counts}")
    if checkpoint_path:
        checkpoint_path.parent.mkdir(parents=True, exist_ok=True)
        atomic_write_json(checkpoint_path, payload)
        aggregate_progress(f"saved checkpoint stage={stage} path={checkpoint_path.relative_to(PROJECT_ROOT).as_posix()}")
    return payload


def aggregate_category_payload_from_cards(
    cards: list[str],
    *,
    category: str,
    final: bool,
    stage: str,
    checkpoint_path: Path | None = None,
) -> dict[str, Any]:
    if checkpoint_path and checkpoint_path.exists():
        try:
            payload = json.loads(checkpoint_path.read_text(encoding="utf-8"))
            count = len(safe_list(payload, category))
            aggregate_progress(
                f"reuse checkpoint stage={stage} category={category} "
                f"path={checkpoint_path.relative_to(PROJECT_ROOT).as_posix()} count={count}"
            )
            return {category: safe_list(payload, category)}
        except (OSError, json.JSONDecodeError) as exc:
            aggregate_progress(f"ignore invalid checkpoint stage={stage} category={category} error={exc}")

    limits = aggregate_limits(final=final)
    limit = limits[category]
    system = (
        "You are a structured editor for a scientific LLM Wiki. "
        "You merge and deduplicate one aggregate category at a time. "
        "The output is for Chinese academic discussion, but source terms, abbreviations, variables, "
        "and method names must be preserved where useful."
    )
    prompt = f"""
Task stage: {stage}
Category: {category}

Merge the following batch-level JSON excerpts into one clean category-level aggregate.
Understand Chinese and English source text equally. Merge synonymous items across languages.
Do not summarize batch-by-batch. Build reusable knowledge units for later evidence-grounded RAG.

{aggregate_category_schema_prompt(category, limit)}

Input materials:

{chr(10).join(cards)}
"""
    char_count = sum(len(card) for card in cards)
    timeout = int_env("LLM_WIKI_AGGREGATE_TIMEOUT", 300)
    thinking = final and bool_env("LLM_WIKI_AGGREGATE_FINAL_THINKING", True)
    reasoning_effort = os.environ.get("LLM_WIKI_AGGREGATE_FINAL_REASONING_EFFORT", "max").strip() or "max"
    max_tokens = int_env("LLM_WIKI_AGGREGATE_FINAL_MAX_TOKENS", 65536) if final else None
    aggregate_progress(
        f"start stage={stage} category={category} final={final} cards={len(cards)} "
        f"chars={char_count} timeout={timeout}s thinking={thinking} "
        f"reasoning_effort={reasoning_effort if thinking else ''} max_tokens={max_tokens or ''}"
    )
    started = time.perf_counter()
    try:
        raw, usage = pqa_api.call_deepseek(
            [
                {"role": "system", "content": system},
                {"role": "user", "content": prompt},
            ],
            temperature=0.1,
            timeout=timeout,
            thinking=thinking if final else None,
            reasoning_effort=reasoning_effort if thinking else None,
            max_tokens=max_tokens,
            response_format={"type": "json_object"},
        )
        elapsed = time.perf_counter() - started
        aggregate_progress(
            f"response stage={stage} category={category} elapsed={elapsed:.1f}s "
            f"raw_chars={len(raw)} usage={usage}"
        )
        if checkpoint_path:
            checkpoint_path.parent.mkdir(parents=True, exist_ok=True)
            raw_path = checkpoint_path.with_name(f"{checkpoint_path.name}.raw.txt")
            raw_path.write_text(raw, encoding="utf-8")
            aggregate_progress(
                f"saved raw response stage={stage} category={category} "
                f"path={raw_path.relative_to(PROJECT_ROOT).as_posix()}"
            )
        try:
            payload = parse_json_response(raw)
        except Exception as parse_exc:
            aggregate_progress(
                f"parse failed stage={stage} category={category}; attempting json repair error={parse_exc}"
            )
            payload = repair_json_response(raw, stage=f"{stage} {category}", error=parse_exc)
            if checkpoint_path:
                repaired_path = checkpoint_path.with_name(f"{checkpoint_path.name}.repaired.json")
                repaired_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
                aggregate_progress(
                    f"saved repaired json stage={stage} category={category} "
                    f"path={repaired_path.relative_to(PROJECT_ROOT).as_posix()}"
                )
    except Exception as exc:
        elapsed = time.perf_counter() - started
        aggregate_progress(f"failed stage={stage} category={category} elapsed={elapsed:.1f}s error={exc}")
        raise

    payload = {category: safe_list(payload, category)}
    aggregate_progress(f"parsed stage={stage} category={category} count={len(payload[category])}")
    if checkpoint_path:
        checkpoint_path.parent.mkdir(parents=True, exist_ok=True)
        atomic_write_json(checkpoint_path, payload)
        aggregate_progress(
            f"saved checkpoint stage={stage} category={category} "
            f"path={checkpoint_path.relative_to(PROJECT_ROOT).as_posix()}"
        )
    return payload


def aggregate_category_payload_from_partials(
    partials: list[dict[str, Any]],
    *,
    category: str,
    checkpoint_root: Path | None = None,
) -> dict[str, Any]:
    current_cards = []
    for index, payload in enumerate(partials, start=1):
        items = safe_list(payload, category)
        if not items:
            continue
        current_cards.append(
            f"PARTIAL_BATCH_{index} CATEGORY {category}\n"
            f"{json.dumps({category: items}, ensure_ascii=False, indent=2)}"
        )

    if not current_cards:
        aggregate_progress(f"category merge skipped category={category} reason=no-items")
        return {category: []}

    merge_budget = int_env(
        "LLM_WIKI_AGGREGATE_MERGE_CHAR_BUDGET",
        int_env("LLM_WIKI_AGGREGATE_BATCH_CHAR_BUDGET", 240000),
    )
    max_rounds = int_env("LLM_WIKI_AGGREGATE_MAX_MERGE_ROUNDS", 5)
    round_index = 1
    aggregate_progress(
        f"category merge input category={category} partials={len(current_cards)} "
        f"chars={sum(len(card) for card in current_cards)} merge_budget={merge_budget}"
    )

    while True:
        chunks = chunk_texts(current_cards, max_chars=merge_budget)
        if len(chunks) == 1:
            final_chars = sum(len(card) for card in chunks[0])
            aggregate_progress(
                f"category final merge input category={category} cards={len(chunks[0])} "
                f"chars={final_chars} merge_budget={merge_budget}"
            )
            return aggregate_category_payload_from_cards(
                chunks[0],
                category=category,
                final=True,
                stage=f"final {category} merge and deduplication",
                checkpoint_path=(checkpoint_root / f"final-{category}.json") if checkpoint_root else None,
            )

        if round_index > max_rounds:
            raise RuntimeError(
                "Aggregate category merge did not converge within "
                f"{max_rounds} rounds for {category}. Increase LLM_WIKI_AGGREGATE_MERGE_CHAR_BUDGET "
                "or reduce intermediate limits; refusing to truncate aggregate data."
            )

        aggregate_progress(
            f"category merge round {round_index} category={category} chunks={len(chunks)} "
            f"input_chars={sum(len(card) for card in current_cards)} merge_budget={merge_budget}"
        )
        next_payloads: list[dict[str, Any]] = []
        for index, chunk in enumerate(chunks, start=1):
            next_payloads.append(
                aggregate_category_payload_from_cards(
                    chunk,
                    category=category,
                    final=False,
                    stage=f"{category} merge round {round_index} batch {index}/{len(chunks)}",
                    checkpoint_path=(
                        checkpoint_root
                        / f"{category}-merge-r{round_index:02d}-{index:03d}-of-{len(chunks):03d}.json"
                    )
                    if checkpoint_root
                    else None,
                )
            )

        current_cards = []
        for index, payload in enumerate(next_payloads, start=1):
            current_cards.append(
                f"MERGE_ROUND_{round_index}_PARTIAL_{index} CATEGORY {category}\n"
                f"{json.dumps(payload, ensure_ascii=False, indent=2)}"
            )
        round_index += 1


def aggregate_payload_from_partials(
    partials: list[dict[str, Any]],
    *,
    checkpoint_root: Path | None = None,
) -> dict[str, Any]:
    aggregate_progress(
        f"category final merge start partials={len(partials)} "
        f"counts={aggregate_item_counts({key: [item for payload in partials for item in safe_list(payload, key)] for key in AGGREGATE_KEYS})}"
    )
    merged = {key: [] for key in AGGREGATE_KEYS}
    for category in AGGREGATE_KEYS:
        payload = aggregate_category_payload_from_partials(
            partials,
            category=category,
            checkpoint_root=checkpoint_root,
        )
        merged[category] = safe_list(payload, category)
        aggregate_progress(f"category final merge done category={category} count={len(merged[category])}")
    aggregate_progress(f"category final merge all done counts={aggregate_item_counts(merged)}")
    return merged


def aggregate_payload(paper_pages: list[tuple[Path, str]]) -> dict[str, Any]:
    card_budget = int_env("LLM_WIKI_AGGREGATE_CARD_CHAR_BUDGET", 12000)
    batch_budget = int_env("LLM_WIKI_AGGREGATE_BATCH_CHAR_BUDGET", 240000)
    cards = [aggregate_card(path, content, max_chars=card_budget) for path, content in paper_pages]
    batches = chunk_texts(cards, max_chars=batch_budget)
    run_id = os.environ.get("LLM_WIKI_AGGREGATE_RUN_ID") or datetime.now().strftime("%Y%m%d-%H%M%S")
    checkpoint_root = WIKI_DIR / ".staging" / "aggregate-checkpoints" / run_id
    checkpoint_root.mkdir(parents=True, exist_ok=True)
    metadata = {
        "run_id": run_id,
        "paper_pages": len(paper_pages),
        "cards": len(cards),
        "batches": len(batches),
        "card_budget": card_budget,
        "batch_budget": batch_budget,
        "merge_budget": int_env(
            "LLM_WIKI_AGGREGATE_MERGE_CHAR_BUDGET",
            int_env("LLM_WIKI_AGGREGATE_BATCH_CHAR_BUDGET", 240000),
        ),
        "model": os.environ.get("PQA_LLM_MODEL", ""),
        "started_at": datetime.now().isoformat(timespec="seconds"),
    }
    atomic_write_json(checkpoint_root / "metadata.json", metadata)
    aggregate_progress(
        f"prepared paper_pages={len(paper_pages)} cards={len(cards)} batches={len(batches)} "
        f"card_budget={card_budget} batch_budget={batch_budget} "
        f"checkpoint={checkpoint_root.relative_to(PROJECT_ROOT).as_posix()}"
    )
    if not batches:
        return {"concepts": [], "methods": [], "claims": [], "syntheses": [], "open_questions": []}

    partials = []
    for index, batch in enumerate(batches, start=1):
        partials.append(
            aggregate_payload_from_cards(
                batch,
                final=False,
                stage=f"batch aggregation {index}/{len(batches)}",
                checkpoint_path=checkpoint_root / f"batch-{index:03d}-of-{len(batches):03d}.json",
            )
        )
        aggregate_progress(f"completed batch {index}/{len(batches)}")
    return aggregate_payload_from_partials(partials, checkpoint_root=checkpoint_root)


def safe_list(payload: dict[str, Any], key: str) -> list[dict[str, Any]]:
    value = payload.get(key, [])
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, dict)]


def paper_page_ids() -> set[str]:
    papers_dir = WIKI_DIR / "papers"
    if not papers_dir.exists():
        return set()
    return {path.stem for path in papers_dir.glob("*.md")}


def resolve_paper_source_id(paper_id: str, paper_ids: set[str] | None = None) -> str:
    paper_id = str(paper_id or "").strip()
    if not paper_id:
        return paper_id
    ids = paper_ids if paper_ids is not None else paper_page_ids()
    if paper_id in ids:
        return paper_id
    if SOURCE_ID_ALIASES.get(paper_id) in ids:
        return SOURCE_ID_ALIASES[paper_id]

    prefix_matches = [candidate for candidate in ids if candidate.startswith(paper_id)]
    if len(prefix_matches) == 1:
        return prefix_matches[0]

    yearless = re.sub(r"^\d{4}-", "", paper_id)
    if yearless != paper_id:
        yearless_matches = [
            candidate
            for candidate in ids
            if re.sub(r"^\d{4}-", "", candidate).startswith(yearless)
        ]
        if len(yearless_matches) == 1:
            return yearless_matches[0]

    print(
        f"Warning: could not resolve paper source id '{paper_id}' to any known paper page; "
        "source links will be broken.",
        file=sys.stderr,
        flush=True,
    )
    return paper_id


def canonicalize_sources(sources: list[Any]) -> list[Any]:
    ids = paper_page_ids()
    canonical: list[Any] = []
    for source in sources:
        if isinstance(source, dict):
            item = dict(source)
            item["paper_id"] = resolve_paper_source_id(str(item.get("paper_id", "")), ids)
            canonical.append(item)
        else:
            canonical.append(resolve_paper_source_id(str(source), ids))
    return canonical


def source_links(sources: list[Any]) -> str:
    lines = []
    paper_ids = paper_page_ids()
    for source in sources:
        paper_id = source.get("paper_id") if isinstance(source, dict) else str(source)
        locator = source.get("locator", "") if isinstance(source, dict) else ""
        if not paper_id:
            continue
        paper_id = resolve_paper_source_id(paper_id, paper_ids)
        suffix = f" ({locator})" if locator else ""
        lines.append(f"- [{paper_id}](../papers/{paper_id}.md){suffix}")
    return "\n".join(lines) if lines else "- No source paper recorded."


TOPIC_TYPES = {
    "concepts": "concept",
    "methods": "method",
    "claims": "claim",
    "syntheses": "synthesis",
    "open-questions": "open-question",
}


def topic_type(folder: str) -> str:
    return TOPIC_TYPES.get(folder, folder.rstrip("s"))


def list_values(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        values = []
        for item in value:
            if isinstance(item, dict):
                values.append(json.dumps(item, ensure_ascii=False))
            else:
                text = str(item).strip()
                if text:
                    values.append(text)
        return values
    text = str(value).strip()
    return [text] if text else []


def text_section(title: str, value: Any, fallback: str = "not-confirmed-from-current-pages") -> str:
    text = str(value or "").strip()
    return f"## {title}\n\n{text or fallback}\n"


def list_section(title: str, value: Any) -> str:
    values = list_values(value)
    body = "\n".join(f"- {item}" for item in values) if values else "- not-confirmed-from-current-pages"
    return f"## {title}\n\n{body}\n"


def write_topic_page(folder: str, slug: str, fields: dict[str, Any], body: str, *, base_dir: Path | None = None) -> Path:
    root = base_dir or WIKI_DIR
    path = root / folder / f"{slugify(slug, max_len=90)}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = {
        "type": topic_type(folder),
        "schema_version": AGGREGATE_SCHEMA_VERSION,
        "status": "draft",
        "compiled_model": os.environ.get("PQA_LLM_MODEL", ""),
        "compiled_at": datetime.now().isoformat(timespec="seconds"),
        **fields,
    }
    atomic_write_text(path, frontmatter(fields) + body.strip() + "\n")
    return path


def aggregate_payload_has_items(payload: dict[str, Any]) -> bool:
    return any(safe_list(payload, key) for key in ["concepts", "methods", "claims", "syntheses", "open_questions"])


def archive_existing_aggregate_pages() -> Path:
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    archive_root = WIKI_DIR / ".archive" / "aggregates" / timestamp
    moved = 0
    aggregate_progress(f"archive existing aggregate pages start target={archive_root.relative_to(PROJECT_ROOT).as_posix()}")
    for folder in AGGREGATE_FOLDERS:
        source_dir = WIKI_DIR / folder
        if not source_dir.exists():
            continue
        destination_dir = archive_root / folder
        destination_dir.mkdir(parents=True, exist_ok=True)
        for path in source_dir.glob("*.md"):
            destination = destination_dir / path.name
            if destination.exists():
                destination = destination_dir / f"{path.stem}-{moved}{path.suffix}"
            shutil.move(str(path), str(destination))
            moved += 1
    if moved:
        append_log(f"archived {moved} aggregate pages to {archive_root.relative_to(PROJECT_ROOT).as_posix()}")
    aggregate_progress(f"archive existing aggregate pages done moved={moved}")
    return archive_root


def promote_staged_aggregate_pages(staging_root: Path) -> list[Path]:
    written: list[Path] = []
    for folder in AGGREGATE_FOLDERS:
        source_dir = staging_root / folder
        target_dir = WIKI_DIR / folder
        target_dir.mkdir(parents=True, exist_ok=True)
        if not source_dir.exists():
            continue
        for path in source_dir.glob("*.md"):
            destination = target_dir / path.name
            if destination.exists():
                destination.unlink()
            shutil.move(str(path), str(destination))
            written.append(destination)
    try:
        shutil.rmtree(staging_root)
    except OSError:
        pass
    return written


def write_aggregate_pages(payload: dict[str, Any], *, archive_existing: bool = True) -> list[Path]:
    if not aggregate_payload_has_items(payload):
        append_log("skipped aggregate page replacement because payload was empty")
        aggregate_progress("skipped aggregate page replacement because payload was empty")
        return []

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    staging_root = WIKI_DIR / ".staging" / "aggregates" / timestamp
    staging_root.mkdir(parents=True, exist_ok=True)
    aggregate_progress(
        f"write aggregate pages start staging={staging_root.relative_to(PROJECT_ROOT).as_posix()} "
        f"counts={aggregate_item_counts(payload)}"
    )
    written: list[Path] = []
    for item in safe_list(payload, "concepts"):
        name = item.get("name", "Untitled Concept")
        slug = item.get("slug") or name
        definition = item.get("definition") or item.get("summary", "")
        sources = canonicalize_sources(item.get("sources", []))
        fields = {
            "name": name,
            "aliases": item.get("aliases", []),
            "sources": sources,
        }
        body = (
            f"# {name}\n\n"
            + text_section("Definition", definition)
            + list_section("Aliases", item.get("aliases", []))
            + text_section("Boundary", item.get("boundary", ""))
            + list_section("Related Methods", item.get("related_methods", []))
            + list_section("Related Claims", item.get("related_claims", []))
            + f"## Source Papers\n\n{source_links(sources)}\n"
        )
        written.append(write_topic_page("concepts", slug, fields, body, base_dir=staging_root))

    for item in safe_list(payload, "methods"):
        name = item.get("name", "Untitled Method")
        slug = item.get("slug") or name
        sources = canonicalize_sources(item.get("sources", []))
        fields = {"name": name, "aliases": item.get("aliases", []), "sources": sources}
        body = (
            f"# {name}\n\n"
            + text_section("Purpose", item.get("purpose") or item.get("summary", ""))
            + list_section("Aliases", item.get("aliases", []))
            + text_section("Workflow", item.get("workflow", ""))
            + list_section("Inputs", item.get("inputs", []))
            + list_section("Outputs", item.get("outputs", []))
            + list_section("Assumptions", item.get("assumptions", []))
            + list_section("Strengths", item.get("strengths", []))
            + list_section("Limitations", item.get("limitations", []))
            + list_section("Related Concepts", item.get("related_concepts", []))
            + f"## Source Papers\n\n{source_links(sources)}\n"
        )
        written.append(write_topic_page("methods", slug, fields, body, base_dir=staging_root))

    for item in safe_list(payload, "claims"):
        claim = item.get("claim", "Untitled claim")
        slug = item.get("slug") or claim
        sources = canonicalize_sources(item.get("sources", []))
        fields = {
            "claim": claim,
            "confidence": item.get("confidence", "medium"),
            "claim_status": item.get("status", "provisional"),
            "sources": sources,
        }
        body = (
            f"# Claim: {claim}\n\n"
            f"## Status\n\n{item.get('status', 'provisional')}\n\n"
            f"## Confidence\n\n{item.get('confidence', 'medium')}\n\n"
            + text_section("Evidence", item.get("evidence", ""))
            + text_section("Condition", item.get("condition", ""))
            + text_section("Limitation", item.get("limitation", ""))
            + list_section("Supports", item.get("supports", []))
            + list_section("Contradicts", item.get("contradicts", []))
            + f"## Source Papers\n\n{source_links(sources)}\n"
        )
        written.append(write_topic_page("claims", slug, fields, body, base_dir=staging_root))

    for item in safe_list(payload, "syntheses"):
        title = item.get("title", "Untitled Synthesis")
        slug = item.get("slug") or title
        summary = item.get("summary", "")
        sources = canonicalize_sources(item.get("sources", []))
        body = (
            f"# {title}\n\n"
            + text_section("Central Question", item.get("central_question", ""))
            + text_section("Synthesis", summary)
            + list_section("Evidence Chain", item.get("evidence_chain", []))
            + list_section("Disagreements / Tensions", item.get("disagreements", []))
            + list_section("Boundary Conditions", item.get("boundary_conditions", []))
            + list_section("Writing Uses", item.get("writing_uses", []))
            + f"## Source Papers\n\n{source_links(sources)}\n"
        )
        written.append(write_topic_page("syntheses", slug, {"title": title, "sources": sources}, body, base_dir=staging_root))

    questions = safe_list(payload, "open_questions")
    if questions:
        lines = ["# Open Questions", ""]
        for item in questions:
            question = item.get("question", "Untitled question")
            lines.extend(
                [
                    f"## {question}",
                    "",
                    item.get("why_it_matters", ""),
                    "",
                    "### Current Evidence",
                    "",
                    item.get("current_evidence", "not-confirmed-from-current-pages"),
                    "",
                    "### Needed Evidence",
                    "",
                    item.get("needed_evidence", "not-confirmed-from-current-pages"),
                    "",
                    "### Source Papers",
                    "",
                    source_links(item.get("sources", [])),
                    "",
                ]
            )
        written.append(
            write_topic_page(
                "open-questions",
                "open-questions",
                {"title": "Open Questions"},
                "\n".join(lines),
                base_dir=staging_root,
            )
        )
    if archive_existing:
        archive_existing_aggregate_pages()
    promoted = promote_staged_aggregate_pages(staging_root)
    aggregate_progress(f"write aggregate pages done promoted={len(promoted)}")
    return promoted


def folder_counts() -> dict[str, int]:
    return {
        folder: len(list((WIKI_DIR / folder).glob("*.md"))) if (WIKI_DIR / folder).exists() else 0
        for folder in WIKI_FOLDERS
    }


def write_index() -> None:
    counts = folder_counts()
    lines = [
        "# LLM Wiki",
        "",
        f"Last compiled: {datetime.now().isoformat(timespec='seconds')}",
        "",
        "## Counts",
        "",
    ]
    for folder in WIKI_FOLDERS:
        lines.append(f"- {folder}: {counts[folder]}")
    lines.extend(["", "## Papers", ""])
    for path in sorted((WIKI_DIR / "papers").glob("*.md")):
        lines.append(f"- [{path.stem}](papers/{path.name})")
    lines.extend(["", "## Syntheses", ""])
    for path in sorted((WIKI_DIR / "syntheses").glob("*.md")):
        lines.append(f"- [{path.stem}](syntheses/{path.name})")
    atomic_write_text(WIKI_DIR / "index.md", "\n".join(lines) + "\n")


def append_log(message: str) -> None:
    log_path = WIKI_DIR / "log.md"
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(f"\n- {datetime.now().isoformat(timespec='seconds')} - {message}\n")


def lint_wiki() -> list[str]:
    problems: list[str] = []
    if not WIKI_DIR.exists():
        return ["wiki directory does not exist"]
    for folder in WIKI_FOLDERS:
        if not (WIKI_DIR / folder).exists():
            problems.append(f"missing folder: wiki/{folder}")
    lint_roots = [WIKI_DIR / folder for folder in WIKI_FOLDERS]
    for root in lint_roots:
        if not root.exists():
            continue
        for path in root.rglob("*.md"):
            relative = path.relative_to(WIKI_DIR)
            if relative.parts and relative.parts[0] in {".archive", ".obsidian", ".staging"}:
                continue
            content = path.read_text(encoding="utf-8-sig", errors="replace")
            if not content.startswith("---"):
                problems.append(f"missing front matter: {path.relative_to(PROJECT_ROOT).as_posix()}")
            if "\\ufffd" in content:
                problems.append(f"replacement character found: {path.relative_to(PROJECT_ROOT).as_posix()}")
    for path in (WIKI_DIR / "claims").glob("*.md"):
        content = path.read_text(encoding="utf-8-sig", errors="replace")
        if "sources:" not in content and "## Source Papers" not in content:
            problems.append(f"claim without sources: {path.relative_to(PROJECT_ROOT).as_posix()}")
    return problems


def quality_warnings() -> list[str]:
    warnings: list[str] = []
    paper_ids = {path.stem for path in (WIKI_DIR / "papers").glob("*.md")}
    claim_to_paths: dict[str, list[Path]] = {}
    min_aggregate_chars = int_env("LLM_WIKI_MIN_AGGREGATE_CHARS", 450)

    for folder in ["concepts", "methods", "claims", "syntheses"]:
        for path in (WIKI_DIR / folder).glob("*.md"):
            content = path.read_text(encoding="utf-8-sig", errors="replace")
            body = strip_frontmatter(content)
            if len(body.strip()) < min_aggregate_chars:
                warnings.append(f"short aggregate page: {path.relative_to(PROJECT_ROOT).as_posix()}")

            for match in re.finditer(r"\]\(\.\./papers/([^)]+)\.md\)", content):
                if match.group(1) not in paper_ids:
                    warnings.append(
                        f"source link target missing: {path.relative_to(PROJECT_ROOT).as_posix()} -> {match.group(1)}"
                    )

    for path in (WIKI_DIR / "claims").glob("*.md"):
        content = path.read_text(encoding="utf-8-sig", errors="replace")
        fields = parse_simple_frontmatter(content)
        claim = fields.get("claim", "")
        if claim:
            claim_to_paths.setdefault(claim, []).append(path)
        if "locator:" not in content:
            warnings.append(f"claim without locator: {path.relative_to(PROJECT_ROOT).as_posix()}")

    for claim, paths in claim_to_paths.items():
        if len(paths) > 1:
            names = ", ".join(path.relative_to(PROJECT_ROOT).as_posix() for path in paths)
            warnings.append(f"duplicate claim text: {claim} -> {names}")

    return warnings


def cmd_init(_args: argparse.Namespace) -> int:
    ensure_wiki_dirs()
    write_index()
    append_log("initialized wiki folders")
    print("Initialized LLM Wiki folders.")
    return 0


def cmd_status(args: argparse.Namespace) -> int:
    ensure_wiki_dirs()
    payload = {"counts": folder_counts(), "problems": lint_wiki(), "warnings": quality_warnings()}
    if args.format == "json":
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        for folder, count in payload["counts"].items():
            print(f"{folder}: {count}")
        if payload["problems"]:
            print("\nProblems:")
            for problem in payload["problems"]:
                print(f"- {problem}")
        if payload["warnings"]:
            print("\nWarnings:")
            for warning in payload["warnings"]:
                print(f"- {warning}")
    return 0


async def ingest_async(args: argparse.Namespace) -> int:
    ensure_wiki_dirs()
    run_id = os.environ.get("LLM_WIKI_RUN_ID") or datetime.now().strftime("%Y%m%d-%H%M%S")
    if args.shard_count < 1:
        raise ValueError("--shard-count must be >= 1")
    if args.shard_index < 0 or args.shard_index >= args.shard_count:
        raise ValueError("--shard-index must be >= 0 and < --shard-count")
    if args.shard_count > 1 and not args.no_aggregate:
        raise ValueError("Sharded paper compilation requires --no-aggregate. Run aggregate after all shards finish.")
    os.environ["LLM_WIKI_SHARD_COUNT"] = str(args.shard_count)
    os.environ["LLM_WIKI_SHARD_INDEX"] = str(args.shard_index)
    started_at = time.time()
    aggregate_progress(
        f"ingest start index={args.index_name} aggregate_only={args.aggregate_only} "
        f"no_aggregate={args.no_aggregate} force={args.force} resume={args.resume} "
        f"run_id={run_id} shard={args.shard_index}/{args.shard_count}"
    )
    records = await load_index_records(args.index_name, limit=None)
    aggregate_progress(f"loaded index records raw={len(records)}")
    records = deduplicate_records(records)
    aggregate_progress(f"deduplicated records count={len(records)}")
    if args.offset:
        records = records[args.offset :]
        aggregate_progress(f"applied offset={args.offset} remaining={len(records)}")
    if args.limit is not None:
        records = records[: args.limit]
        aggregate_progress(f"applied limit={args.limit} remaining={len(records)}")
    global_record_count = len(records)
    if args.shard_count > 1:
        records = [
            record
            for zero_based_index, record in enumerate(records)
            if zero_based_index % args.shard_count == args.shard_index
        ]
        aggregate_progress(
            f"applied shard index={args.shard_index} count={args.shard_count} "
            f"global_records={global_record_count} shard_records={len(records)}"
        )
    if args.dry_run:
        for record in records:
            print(f"{record.paper_id}: {record.text_count} texts, {record.text_chars} chars", flush=True)
        return 0

    active_paper_ids = {record.paper_id for record in records}

    written: list[Path] = []
    new_compiled = 0
    skipped_complete = 0
    skipped_over_budget = 0
    failed = 0
    consecutive_failures = 0
    max_consecutive_failures = int_env("LLM_WIKI_MAX_CONSECUTIVE_FAILURES", 3)
    total_records = len(records)
    write_progress(
        run_id,
        {
            "phase": "paper-pages",
            "status": "running",
            "total_records": total_records,
            "completed": 0,
            "skipped_complete": 0,
            "skipped_over_budget": 0,
            "failed": 0,
            "remaining": total_records,
            "model": os.environ.get("PQA_LLM_MODEL", ""),
            "single_pass_char_budget": int_env("LLM_WIKI_PAPER_SINGLE_PASS_CHAR_BUDGET", 320000),
            "global_record_count": global_record_count,
        },
    )
    if not args.aggregate_only:
        for index, record in enumerate(records, start=1):
            paper_path = WIKI_DIR / "papers" / f"{record.paper_id}.md"
            if args.force and args.resume and paper_page_complete(
                paper_path, os.environ.get("PQA_LLM_MODEL", "")
            ):
                print(f"resume skip complete {paper_path.relative_to(PROJECT_ROOT).as_posix()}", flush=True)
                written.append(paper_path)
                skipped_complete += 1
                remaining = total_records - index
                write_progress(
                    run_id,
                    {
                        "phase": "paper-pages",
                        "status": "running",
                        "total_records": total_records,
                        "current_index": index,
                        "current_paper": record.paper_id,
                        "completed": new_compiled,
                        "skipped_complete": skipped_complete,
                        "skipped_over_budget": skipped_over_budget,
                        "failed": failed,
                        "remaining": remaining,
                        **estimate_eta(started_at, new_compiled, remaining),
                    },
                )
                continue
            if (
                paper_path.exists()
                and not args.force
                and paper_page_complete(paper_path, os.environ.get("PQA_LLM_MODEL", ""))
            ):
                print(f"skip existing {paper_path.relative_to(PROJECT_ROOT).as_posix()}", flush=True)
                written.append(paper_path)
                continue
            if paper_path.exists() and not args.force:
                print(f"recompile stale {paper_path.relative_to(PROJECT_ROOT).as_posix()}", flush=True)
            if args.max_new and not args.force and new_compiled >= args.max_new:
                print(f"defer {record.paper_id}", flush=True)
                continue
            print(f"compile paper {record.paper_id}", flush=True)
            try:
                body, coverage = compile_paper_page(record)
            except ValueError as exc:
                if str(exc).startswith("source_chars_exceed_single_pass_budget"):
                    skipped_over_budget += 1
                    append_skipped_record(
                        run_id,
                        record,
                        reason="source_chars_exceed_single_pass_budget",
                        details={
                            "error": str(exc),
                            "compiled_source_chars": sum(len(block) for block in record.source_blocks),
                            "budget": int_env("LLM_WIKI_PAPER_SINGLE_PASS_CHAR_BUDGET", 320000),
                        },
                    )
                    print(f"skip over budget {record.paper_id}: {exc}", flush=True)
                    consecutive_failures = 0
                else:
                    failed += 1
                    consecutive_failures += 1
                    append_skipped_record(run_id, record, reason="failed", details={"error": str(exc)})
                    print(f"failed paper {record.paper_id}: {exc}", file=sys.stderr, flush=True)
            except Exception as exc:
                failed += 1
                consecutive_failures += 1
                append_skipped_record(run_id, record, reason="failed", details={"error": str(exc)})
                print(f"failed paper {record.paper_id}: {exc}", file=sys.stderr, flush=True)
            else:
                written.append(write_paper_page(record, body, coverage))
                new_compiled += 1
                consecutive_failures = 0
            if consecutive_failures >= max_consecutive_failures:
                raise RuntimeError(
                    f"Stopped after {consecutive_failures} consecutive paper failures; refusing to burn more tokens."
                )
            remaining = total_records - index
            write_progress(
                run_id,
                {
                    "phase": "paper-pages",
                    "status": "running",
                    "total_records": total_records,
                    "current_index": index,
                    "current_paper": record.paper_id,
                    "completed": new_compiled,
                    "skipped_complete": skipped_complete,
                    "skipped_over_budget": skipped_over_budget,
                    "failed": failed,
                    "remaining": remaining,
                    **estimate_eta(started_at, new_compiled, remaining),
                },
            )

    if not args.no_aggregate:
        print("compile aggregate wiki pages", flush=True)
        complete_paper_ids = {
            record.paper_id
            for record in records
            if paper_page_complete(WIKI_DIR / "papers" / f"{record.paper_id}.md", os.environ.get("PQA_LLM_MODEL", ""))
        }
        missing_paper_ids = active_paper_ids - complete_paper_ids
        over_budget_ids = skipped_paper_ids_by_reason("source_chars_exceed_single_pass_budget")
        unresolved_missing = missing_paper_ids - over_budget_ids
        if unresolved_missing:
            sample = ", ".join(sorted(unresolved_missing)[:10])
            raise RuntimeError(
                "Aggregate refused: some active papers are neither schema-v4 full-index pages "
                f"nor explicit over-budget skips ({len(unresolved_missing)} unresolved; sample: {sample})."
            )
        paper_pages = load_paper_pages(complete_paper_ids)
        aggregate_progress(
            f"loaded paper pages for aggregate count={len(paper_pages)} "
            f"complete_ids={len(complete_paper_ids)} over_budget_skips={len(missing_paper_ids & over_budget_ids)}"
        )
        if len(paper_pages) != len(complete_paper_ids):
            raise RuntimeError(
                "Aggregate refused: not every active paper has a schema-v4 full-index page "
                f"({len(paper_pages)}/{len(complete_paper_ids)}). Compile paper pages first."
            )
        write_progress(
            run_id,
            {
                "phase": "aggregate",
                "status": "running",
                "paper_pages": len(paper_pages),
                "model": os.environ.get("PQA_LLM_MODEL", ""),
            },
        )
        payload = aggregate_payload(paper_pages)
        aggregate_progress("aggregate payload ready; write pages")
        written.extend(write_aggregate_pages(payload))

    write_index()
    problems = lint_wiki()
    warnings = quality_warnings()
    append_log(
        f"ingested {len(records)} paper records; wrote {len(written)} pages; "
        f"skipped_over_budget={skipped_over_budget}; failed={failed}; "
        f"problems={len(problems)}; warnings={len(warnings)}"
    )
    write_progress(
        run_id,
        {
            "phase": "done",
            "status": "completed" if not problems else "completed_with_problems",
            "total_records": total_records,
            "completed": new_compiled,
            "skipped_complete": skipped_complete,
            "skipped_over_budget": skipped_over_budget,
            "failed": failed,
            "remaining": 0,
            "counts": folder_counts(),
            "problems": problems,
            "warnings": warnings,
        },
    )
    print(
        json.dumps(
            {
                "papers": len(records),
                "written": len(written),
                "skipped_over_budget": skipped_over_budget,
                "failed": failed,
                "run_id": run_id,
                "counts": folder_counts(),
                "problems": problems,
                "warnings": warnings,
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )
    return 0 if not problems else 1


def cmd_ingest(args: argparse.Namespace) -> int:
    return asyncio.run(ingest_async(args))


def cmd_lint(_args: argparse.Namespace) -> int:
    ensure_wiki_dirs()
    problems = lint_wiki()
    if not problems:
        print("LLM Wiki lint passed.")
        return 0
    for problem in problems:
        print(f"- {problem}")
    return 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Compile PaperQA indexed papers into an LLM Wiki.")
    parser.add_argument(
        "--wiki-dir",
        type=Path,
        default=PROJECT_ROOT / "wiki",
        help="Wiki output directory. Defaults to ./wiki.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Create wiki folders and index files.")
    init_parser.set_defaults(func=cmd_init)

    status_parser = subparsers.add_parser("status", help="Show wiki page counts.")
    status_parser.add_argument("--format", choices=["text", "json"], default="text")
    status_parser.set_defaults(func=cmd_status)

    ingest_parser = subparsers.add_parser("ingest", help="Compile indexed papers into wiki pages.")
    ingest_parser.add_argument("--index-name", default="papers")
    ingest_parser.add_argument("--limit", type=int, default=None)
    ingest_parser.add_argument(
        "--offset",
        type=int,
        default=0,
        help="Skip this many deduplicated indexed paper records before compiling.",
    )
    ingest_parser.add_argument(
        "--max-new",
        type=int,
        default=0,
        help="Maximum number of missing paper pages to compile in this run. 0 means no cap.",
    )
    ingest_parser.add_argument("--force", action="store_true", help="Regenerate existing pages.")
    ingest_parser.add_argument(
        "--resume",
        dest="resume",
        action="store_true",
        default=True,
        help="When --force is used, skip pages already compiled with the current schema.",
    )
    ingest_parser.add_argument(
        "--no-resume",
        dest="resume",
        action="store_false",
        help="When --force is used, regenerate even pages already compiled with the current schema.",
    )
    ingest_parser.add_argument("--dry-run", action="store_true")
    ingest_parser.add_argument("--no-aggregate", action="store_true", help="Only compile paper pages.")
    ingest_parser.add_argument(
        "--shard-count",
        type=int,
        default=1,
        help="Split paper-page compilation into this many non-overlapping shards. Requires --no-aggregate.",
    )
    ingest_parser.add_argument(
        "--shard-index",
        type=int,
        default=0,
        help="Zero-based shard index to compile when --shard-count is greater than 1.",
    )
    ingest_parser.add_argument(
        "--aggregate-only",
        action="store_true",
        help="Skip paper pages and regenerate only aggregate wiki pages.",
    )
    ingest_parser.set_defaults(func=cmd_ingest)

    lint_parser = subparsers.add_parser("lint", help="Check basic wiki integrity.")
    lint_parser.set_defaults(func=cmd_lint)

    return parser


def main() -> int:
    configure_runtime()
    args = build_parser().parse_args()
    set_wiki_dir(args.wiki_dir)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
