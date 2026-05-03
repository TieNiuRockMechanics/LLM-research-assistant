from __future__ import annotations

import argparse
import asyncio
import importlib.util
import inspect
import json
import logging
import os
import re
import time
import sys
import urllib.request
import pickle
import zlib
from pathlib import Path
from typing import Any
from urllib.parse import quote
from urllib.error import HTTPError, URLError

from _lib import (
    clean_excerpt,
    extract_markdown_section,
    float_env,
    frontmatter_strings,
    int_env,
    load_dotenv,
    markdown_headings,
    parse_simple_frontmatter,
    strip_frontmatter,
)


DEFAULT_LLM_MODEL = "deepseek/deepseek-v4-flash"
DEFAULT_EMBEDDING_MODEL = "openai/embedding-3"
DEFAULT_SYSTEM_PROMPT = (
    "你是一个科研写作与文献分析助手，回答应像和研究者讨论问题，而不是复述资料卡片。"
    "如果提供了本地知识库上下文，你要把它当作证据和背景材料：事实性陈述必须有资料支撑，"
    "但解释、比较、判断和写作组织应由你综合完成。不要编造引用，"
    "也不要把没有来源的推断写成论文结论。上下文不足时，明确区分“论文证据显示”和“我的推断”。"
)

CJK_RE = re.compile(r"[\u3400-\u9fff\uf900-\ufaff]|[\U00020000-\U0002A6DF]")
PROJECT_ROOT = Path(__file__).resolve().parents[1]
WIKI_ROOT = PROJECT_ROOT / "wiki"
WIKI_SEMANTIC_INDEX_SCRIPT = PROJECT_ROOT / "scripts" / "wiki_semantic_index.py"
WIKI_AGGREGATE_FOLDERS = {"syntheses", "concepts", "methods", "claims", "open-questions"}
WIKI_PAPER_FOLDERS = {"papers"}
OPEN_QUESTION_QUERY_RE = re.compile(
    r"开放问题|未解决|研究空白|未来方向|后续研究|局限|不足|open questions?|research gaps?|future work|limitations?",
    re.IGNORECASE,
)
QUESTION_COMPARISON_RE = re.compile(
    r"比较|对比|区别|差异|异同|优缺点|哪种更|哪个更|compare|comparison|versus|\bvs\.?\b",
    re.IGNORECASE,
)
QUESTION_METHOD_RE = re.compile(
    r"方法|流程|步骤|怎么做|如何做|表征|建模|反演|测量|实验设计|workflow|protocol|method|methods|"
    r"modeling|modelling|inversion|characterization",
    re.IGNORECASE,
)
QUESTION_CONCEPT_RE = re.compile(
    r"是什么|什么是|定义|如何理解|概念|含义|meaning|define|definition|concept",
    re.IGNORECASE,
)
QUESTION_CLAIM_RE = re.compile(
    r"结论|发现|结果|影响|机制|原因|是否|规律|证据|supports?|contradicts?|effect|relationship|why|how does",
    re.IGNORECASE,
)
INTENT_FOLDER_WEIGHTS = {
    "overview": {"syntheses": 6, "claims": 5, "methods": 4, "concepts": 4, "papers": 3, "open-questions": 1},
    "comparison": {"syntheses": 7, "claims": 6, "methods": 5, "concepts": 4, "papers": 4, "open-questions": 2},
    "method": {"methods": 7, "concepts": 5, "claims": 3, "syntheses": 3, "papers": 4, "open-questions": 1},
    "concept": {"concepts": 7, "methods": 5, "claims": 3, "syntheses": 3, "papers": 3, "open-questions": 1},
    "claim": {"claims": 7, "syntheses": 5, "methods": 3, "concepts": 3, "papers": 5, "open-questions": 2},
    "open_question": {"open-questions": 7, "syntheses": 6, "claims": 3, "methods": 2, "concepts": 2, "papers": 3},
}


def normalize_provider_env() -> None:
    openai_key = os.environ.get("OPENAI_API_KEY")
    openai_base = os.environ.get("OPENAI_BASE_URL", "")
    if openai_base:
        os.environ.setdefault("OPENAI_API_BASE", openai_base)
    if openai_key and "dashscope.aliyuncs.com" in openai_base:
        os.environ.setdefault("DASHSCOPE_API_KEY", openai_key)
        os.environ.setdefault("DASHSCOPE_API_BASE", openai_base)
    if openai_key and "api.deepseek.com" in openai_base:
        os.environ.setdefault("DEEPSEEK_API_KEY", openai_key)
        os.environ.setdefault("DEEPSEEK_BASE_URL", openai_base)
    if os.environ.get("DEEPSEEK_API_KEY"):
        os.environ.setdefault("PQA_LLM_MODEL", DEFAULT_LLM_MODEL)
        os.environ.setdefault("PQA_SUMMARY_LLM_MODEL", DEFAULT_LLM_MODEL)


def load_json_env(name: str) -> dict:
    raw_value = os.environ.get(name, "").strip()
    if not raw_value:
        return {}
    try:
        payload = json.loads(raw_value)
    except json.JSONDecodeError as exc:
        raise ValueError(f"{name} is not valid JSON: {exc}") from exc
    if not isinstance(payload, dict):
        raise ValueError(f"{name} must be a JSON object.")
    return payload


def merge_dict(base: dict, override: dict) -> dict:
    merged = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = merge_dict(merged[key], value)
        else:
            merged[key] = value
    return merged


def maybe_await(value):
    if inspect.isawaitable(value):
        return asyncio.run(value)
    return value


def configure_logging(quiet: bool) -> None:
    if quiet:
        logging.disable(logging.INFO)


def configure_local_packages(project_root: Path) -> None:
    packages_dir = project_root / ".packages"
    if packages_dir.exists():
        package_path = str(packages_dir)
        if package_path not in sys.path:
            sys.path.insert(0, package_path)


def patch_embedding_factory_for_ndim() -> None:
    import paperqa.settings as paperqa_settings

    if getattr(paperqa_settings, "_zpa_ndim_factory_patched", False):
        return

    original_factory = paperqa_settings.embedding_model_factory

    def embedding_model_factory_with_ndim(embedding: str, **kwargs):
        ndim = kwargs.pop("ndim", None)
        model = original_factory(embedding, **kwargs)
        if ndim is not None:
            model.ndim = int(ndim)
        return model

    paperqa_settings.embedding_model_factory = embedding_model_factory_with_ndim
    paperqa_settings._zpa_ndim_factory_patched = True


def make_settings(
    project_root: Path,
    index_name: str,
    rebuild_index: bool,
    paper_directory: Path | None = None,
    sync_with_paper_directory: bool = True,
):
    from paperqa.settings import Settings

    patch_embedding_factory_for_ndim()

    llm = os.environ.get("PQA_LLM_MODEL", DEFAULT_LLM_MODEL)
    summary_llm = os.environ.get("PQA_SUMMARY_LLM_MODEL", llm)
    agent_llm = os.environ.get("PQA_AGENT_LLM_MODEL", llm)
    enrichment_llm = os.environ.get("PQA_ENRICHMENT_LLM_MODEL", llm)
    embedding = os.environ.get("PQA_EMBEDDING_MODEL", DEFAULT_EMBEDDING_MODEL)
    embedding_kwargs = {}
    encoding_format = os.environ.get("PQA_EMBEDDING_ENCODING_FORMAT", "").strip()
    dimensions = os.environ.get("PQA_EMBEDDING_DIMENSIONS", "").strip()
    if encoding_format:
        embedding_kwargs["encoding_format"] = encoding_format
    if dimensions:
        embedding_kwargs["allowed_openai_params"] = ["dimensions"]

    default_embedding_config = {"batch_size": 10}
    if embedding_kwargs:
        default_embedding_config["kwargs"] = embedding_kwargs
    if dimensions:
        default_embedding_config["ndim"] = int(dimensions)

    llm_config = load_json_env("PQA_LLM_CONFIG_JSON")
    embedding_config = merge_dict(
        default_embedding_config,
        load_json_env("PQA_EMBEDDING_CONFIG_JSON"),
    )
    reader_config = merge_dict(
        {
            "chunk_chars": int_env("PQA_READER_CHUNK_CHARS", 5000),
            "overlap": int_env("PQA_READER_OVERLAP_CHARS", 250),
        },
        load_json_env("PQA_READER_CONFIG_JSON"),
    )

    return Settings(
        llm=llm,
        llm_config=llm_config,
        summary_llm=summary_llm,
        summary_llm_config=load_json_env("PQA_SUMMARY_LLM_CONFIG_JSON") or llm_config,
        embedding=embedding,
        embedding_config=embedding_config,
        parsing={
            "page_size_limit": int_env("PQA_PAGE_SIZE_LIMIT_CHARS", 1_280_000),
            "reader_config": reader_config,
            "multimodal": False,
            "use_doc_details": False,
            "enrichment_llm": enrichment_llm,
            "enrichment_llm_config": load_json_env("PQA_ENRICHMENT_LLM_CONFIG_JSON") or llm_config,
        },
        agent={
            "agent_llm": agent_llm,
            "agent_llm_config": load_json_env("PQA_AGENT_LLM_CONFIG_JSON") or llm_config,
            "rebuild_index": rebuild_index,
            "index": {
                "name": index_name,
                "paper_directory": paper_directory or project_root / "data" / "papers",
                "index_directory": project_root / "data" / "indexes",
                "concurrency": 1,
                "batch_size": 1,
                "recurse_subdirectories": False,
                "sync_with_paper_directory": sync_with_paper_directory,
            },
        },
    )


def deepseek_model_name() -> str:
    model = os.environ.get("PQA_LLM_MODEL", DEFAULT_LLM_MODEL)
    return model.removeprefix("deepseek/")


def apply_llm_model_override(model: str | None) -> None:
    if not model:
        return
    os.environ["PQA_LLM_MODEL"] = model
    os.environ["PQA_SUMMARY_LLM_MODEL"] = model
    os.environ["PQA_AGENT_LLM_MODEL"] = model
    os.environ["PQA_ENRICHMENT_LLM_MODEL"] = model


def post_json(url: str, headers: dict[str, str], payload: dict, timeout: int) -> dict:
    request = urllib.request.Request(
        url,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers=headers,
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code}: {detail[:500]}") from exc
    except TimeoutError as exc:
        raise RuntimeError(f"Read timed out after {timeout}s") from exc
    except URLError as exc:
        raise RuntimeError(f"Connection failed: {exc.reason}") from exc


def call_deepseek(
    messages: list[dict[str, str]],
    *,
    temperature: float = 0.2,
    timeout: int = 120,
    thinking: bool | None = None,
    reasoning_effort: str | None = None,
    max_tokens: int | None = None,
    response_format: dict[str, str] | None = None,
) -> tuple[str, dict]:
    api_key = os.environ.get("DEEPSEEK_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("DEEPSEEK_API_KEY is missing in .env.")

    attempts = int(os.environ.get("DEEPSEEK_RETRY_ATTEMPTS", "3"))
    last_error: Exception | None = None
    for attempt in range(1, max(attempts, 1) + 1):
        try:
            payload: dict[str, Any] = {
                "model": deepseek_model_name(),
                "messages": messages,
            }
            if thinking is True:
                payload["thinking"] = {"type": "enabled"}
                payload["reasoning_effort"] = reasoning_effort or "high"
            elif thinking is False:
                payload["thinking"] = {"type": "disabled"}
            elif reasoning_effort:
                payload["reasoning_effort"] = reasoning_effort
            if max_tokens:
                payload["max_tokens"] = max_tokens
            if response_format:
                payload["response_format"] = response_format
            # DeepSeek thinking mode ignores temperature. Keep it off explicit
            # thinking calls so logs and requests match the API contract.
            if thinking is not True:
                payload["temperature"] = temperature
            response = post_json(
                os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com").rstrip("/")
                + "/chat/completions",
                {
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                },
                payload,
                timeout,
            )
            break
        except RuntimeError as exc:
            last_error = exc
            if attempt >= max(attempts, 1) or str(exc).startswith("HTTP 4"):
                raise
            wait_seconds = min(60, 2**attempt)
            print(
                f"DeepSeek request failed on attempt {attempt}/{attempts}: {exc}; retrying in {wait_seconds}s",
                file=sys.stderr,
                flush=True,
            )
            time.sleep(wait_seconds)
    else:
        raise RuntimeError(f"DeepSeek request failed: {last_error}") from last_error
    content = response["choices"][0]["message"].get("content", "")
    return content, response.get("usage", {})


def merge_usage(*usages: dict) -> dict:
    merged: dict = {}
    for usage in usages:
        if not isinstance(usage, dict):
            continue
        for key, value in usage.items():
            if isinstance(value, (int, float)) and isinstance(merged.get(key), (int, float)):
                merged[key] += value
            elif isinstance(value, (int, float)):
                merged[key] = value
            elif isinstance(value, dict) and isinstance(merged.get(key), dict):
                merged[key] = merge_usage(merged[key], value)
            elif key not in merged:
                merged[key] = value
    return merged


def contains_cjk(text: str) -> bool:
    return bool(CJK_RE.search(text))


def paper_directory_for_index(project_root: Path, index_name: str) -> Path:
    topic_dir = project_root / "data" / "papers" / index_name
    if topic_dir.exists():
        return topic_dir
    return project_root / "data" / "papers"


def manifest_for_index(project_root: Path, index_name: str) -> Path:
    topic_manifest = project_root / "data" / f"zotero-{index_name}-manifest.json"
    if topic_manifest.exists():
        return topic_manifest
    return project_root / "data" / "zotero-import-manifest.json"


def library_status(project_root: Path, index_name: str = "papers") -> dict:
    papers_dir = paper_directory_for_index(project_root, index_name)
    index_dir = project_root / "data" / "indexes" / index_name
    docs_dir = index_dir / "docs"
    wiki_root = project_root / "wiki"
    topic_wiki_dir = wiki_root / "topics" / index_name
    wiki_dir = topic_wiki_dir if topic_wiki_dir.exists() else wiki_root
    manifest_path = manifest_for_index(project_root, index_name)

    manifest = {}
    if manifest_path.exists():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
        except json.JSONDecodeError:
            manifest = {}

    imported_count = manifest.get("imported_count")
    if imported_count is None and isinstance(manifest.get("imported"), list):
        imported_count = len(manifest["imported"])

    index_files_zip = index_dir / "files.zip"
    index_document_count = 0
    if index_files_zip.exists():
        try:
            index_document_count = len(pickle.loads(zlib.decompress(index_files_zip.read_bytes())))
        except Exception:
            index_document_count = 0
    if not index_document_count:
        index_files = [path for path in docs_dir.glob("*") if path.is_file()] if docs_dir.exists() else []
        index_document_count = len(index_files)
    wiki_files = list(iter_wiki_markdown(wiki_dir)) if wiki_dir.exists() else []
    wiki_papers = wiki_paper_files(wiki_dir) if wiki_dir.exists() else []
    return {
        "index_name": index_name,
        "paper_count": len(list(papers_dir.glob("*.pdf"))) if papers_dir.exists() else 0,
        "index_document_count": index_document_count,
        "wiki_paper_page_count": len(wiki_papers),
        "wiki_note_count": len(wiki_files),
        "recent_import_count": imported_count or 0,
        "manifest_database": manifest.get("database", ""),
        "index_exists": index_dir.exists() and (index_dir / "files.zip").exists(),
    }


def iter_wiki_markdown(wiki_dir: Path):
    for path in wiki_dir.rglob("*.md"):
        if not path.is_file():
            continue
        try:
            relative = path.relative_to(wiki_dir)
        except ValueError:
            relative = path
        if relative.parts and relative.parts[0] == "topics":
            continue
        yield path


def wiki_paper_files(wiki_dir: Path) -> list[Path]:
    papers_dir = wiki_dir / "papers"
    if not papers_dir.exists():
        return []
    return sorted(path for path in papers_dir.glob("*.md") if path.is_file())


def wiki_terms(text: str) -> set[str]:
    terms = {term.lower() for term in re.findall(r"[A-Za-z][A-Za-z0-9_-]{2,}", text)}
    cjk = "".join(CJK_RE.findall(text))
    terms.update(cjk[i : i + 2] for i in range(max(len(cjk) - 1, 0)))
    return {term for term in terms if len(term) >= 2}


def normalize_search_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def infer_question_intent(text: str) -> str:
    if OPEN_QUESTION_QUERY_RE.search(text):
        return "open_question"
    if QUESTION_COMPARISON_RE.search(text):
        return "comparison"
    if QUESTION_METHOD_RE.search(text):
        return "method"
    if QUESTION_CLAIM_RE.search(text):
        return "claim"
    if QUESTION_CONCEPT_RE.search(text):
        return "concept"
    return "overview"


def build_query_package(question: str, english_query: str) -> dict[str, Any]:
    variants: list[str] = []
    seen: set[str] = set()
    for candidate in [question.strip(), english_query.strip()]:
        normalized = normalize_search_text(candidate)
        if not normalized or normalized in seen:
            continue
        seen.add(normalized)
        variants.append(candidate)
    intent = infer_question_intent("\n".join(variants))
    folder_weights = dict(INTENT_FOLDER_WEIGHTS.get(intent, INTENT_FOLDER_WEIGHTS["overview"]))
    preferred_folders = [
        folder for folder, _weight in sorted(folder_weights.items(), key=lambda item: (-item[1], item[0])) if _weight > 0
    ]
    paper_search_query = english_query.strip() or question.strip()
    if contains_cjk(question) and english_query.strip() and english_query.strip() != question.strip():
        paper_search_query = question.strip() + "\n" + english_query.strip()
    return {
        "question": question,
        "english_query": english_query.strip(),
        "variants": variants,
        "terms": sorted(wiki_terms("\n".join(variants))),
        "intent": intent,
        "folder_weights": folder_weights,
        "preferred_folders": preferred_folders,
        "paper_search_query": paper_search_query,
    }


def wiki_source_type(path: Path, wiki_dir: Path) -> str:
    try:
        relative = path.relative_to(wiki_dir)
    except ValueError:
        return "wiki"
    folder = relative.parts[0] if relative.parts else ""
    if folder in WIKI_AGGREGATE_FOLDERS:
        return "wiki_aggregate"
    if folder in WIKI_PAPER_FOLDERS:
        return "wiki_paper_page"
    return "wiki"


def wiki_label_prefix(source_type: str) -> str:
    if source_type == "wiki_aggregate":
        return "Wiki aggregate"
    if source_type == "wiki_paper_page":
        return "Wiki paper page"
    return "Wiki"


def result_identity_key(item: dict) -> str:
    path = str(item.get("path") or item.get("relative_path") or "").strip()
    heading = str(item.get("heading") or "").strip()
    method = str(item.get("retrieval_method") or "").strip()
    if path and method == "semantic" and heading:
        return f"{path}::{heading}"
    if path:
        return path
    return str(item.get("label") or id(item))


def result_rank_score(item: dict) -> float:
    try:
        return float(item.get("rank_score", item.get("score", 0)) or 0)
    except (TypeError, ValueError):
        return 0.0


def merge_ranked_results(*groups: list[dict], limit: int = 0) -> list[dict]:
    merged: list[dict] = []
    seen: set[str] = set()
    for group in groups:
        for item in group:
            key = result_identity_key(item)
            if key in seen:
                continue
            seen.add(key)
            merged.append(item)
            if limit > 0 and len(merged) >= limit:
                return merged
    return merged


def load_wiki_semantic_module():
    if not WIKI_SEMANTIC_INDEX_SCRIPT.exists():
        return None
    spec = importlib.util.spec_from_file_location("wiki_semantic_index", WIKI_SEMANTIC_INDEX_SCRIPT)
    if spec is None or spec.loader is None:
        return None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def semantic_wiki_enabled() -> bool:
    return os.environ.get("PQA_WIKI_SEMANTIC", "1").strip().lower() not in {"0", "false", "no", "off"}


def semantic_wiki_hits(project_root: Path, query_package: dict[str, Any]) -> list[dict]:
    if not semantic_wiki_enabled():
        return []
    query = "\n".join(query_package.get("variants", [])) or query_package.get("question", "")
    if not query.strip():
        return []
    try:
        module = load_wiki_semantic_module()
        if module is None:
            return []
        hits = module.query_index(
            project_root,
            query,
            top_k=int_env("PQA_WIKI_SEMANTIC_CANDIDATE_TOP_K", 80),
        )
    except Exception as exc:
        if os.environ.get("PQA_WIKI_SEMANTIC_STRICT", "0").strip().lower() in {"1", "true", "yes"}:
            raise
        print(f"Wiki semantic retrieval unavailable; falling back to keyword search: {exc}", file=sys.stderr)
        return []
    selected: list[dict] = []
    per_path_counts: dict[str, int] = {}
    per_path_limit = int_env("PQA_WIKI_SEMANTIC_MAX_PER_PATH", 3)
    top_k = int_env("PQA_WIKI_SEMANTIC_TOP_K", 40)
    group_limits = {
        "wiki_aggregate": int_env("PQA_WIKI_SEMANTIC_AGGREGATE_TOP_K", 10),
        "wiki_paper_page": int_env("PQA_WIKI_SEMANTIC_PAPER_PAGE_TOP_K", 15),
        "paper_evidence": 0,
        "wiki_other": int_env("PQA_WIKI_SEMANTIC_OTHER_TOP_K", 4),
    }
    group_counts = {group: 0 for group in CONTEXT_GROUP_ORDER}
    for hit in hits:
        path_key = str(hit.get("path") or hit.get("relative_path") or hit.get("label"))
        if per_path_counts.get(path_key, 0) >= per_path_limit:
            continue
        group = context_role_info(hit.get("source_type")).get("group", "wiki_other")
        if group_counts.get(group, 0) >= group_limits.get(group, 0):
            continue
        semantic_score = float(hit.get("semantic_score", hit.get("score", 0.0)) or 0.0)
        hit["retrieval_method"] = "semantic"
        hit["semantic_score"] = semantic_score
        hit["rank_score"] = semantic_score * int_env("PQA_WIKI_SEMANTIC_SCORE_SCALE", 1000)
        hit["score"] = hit["rank_score"]
        selected.append(hit)
        per_path_counts[path_key] = per_path_counts.get(path_key, 0) + 1
        group_counts[group] = group_counts.get(group, 0) + 1
        if len(selected) >= top_k:
            break
    return selected


def retrieval_counts_by_group(hits: list[dict]) -> dict[str, int]:
    counts = {group: 0 for group in CONTEXT_GROUP_ORDER}
    for hit in hits:
        group = context_role_info(hit.get("source_type")).get("group", "wiki_other")
        counts[group] = counts.get(group, 0) + 1
    return {group: count for group, count in counts.items() if count}


def retrieval_counts_by_method(hits: list[dict]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for hit in hits:
        method = str(hit.get("retrieval_method") or "keyword")
        counts[method] = counts.get(method, 0) + 1
    return counts


def retrieve_wiki_contexts(project_root: Path, query_package: dict[str, Any]) -> tuple[list[dict], dict[str, Any]]:
    hits = semantic_wiki_hits(project_root, query_package)
    return hits, {
        "semantic_hit_count": len(hits),
        "keyword_hit_count": 0,
        "wiki_combined_count": len(hits),
        "semantic_counts": retrieval_counts_by_group(hits),
        "keyword_counts": {},
        "wiki_combined_counts": retrieval_counts_by_group(hits),
        "wiki_retrieval_methods": retrieval_counts_by_method(hits),
        "layer_order": ["wiki_aggregate", "wiki_paper_page", "paper_evidence", "wiki_other"],
    }


async def build_search_query(question: str) -> str:
    if not contains_cjk(question):
        return question

    prompt = (
        "Translate this research question into a concise English search query for finding "
        "relevant academic paper passages. Preserve technical terms, names, years, and places. "
        "Return only the query.\n\n"
        f"{question}"
    )
    try:
        answer, _ = call_deepseek(
            [{"role": "user", "content": prompt}],
            temperature=0,
            timeout=60,
        )
    except Exception:
        return question
    return answer.strip() or question


def merge_docs(target, source) -> None:
    target.docs.update(source.docs)
    target.texts.extend(source.texts)
    target.docnames.update(source.docnames)




def extract_page_range(name: str) -> str:
    page_match = re.search(
        r"(?:pages?|pp\.?)\s*([0-9ivxlcdmIVXLCDM]+(?:\s*[-–—]\s*[0-9ivxlcdmIVXLCDM]+)?)",
        name,
        re.IGNORECASE,
    )
    if not page_match:
        return ""
    return re.sub(r"\s*[–—]\s*", "-", page_match.group(1).strip())


def normalize_author(raw_author: str) -> str:
    raw_author = raw_author.strip(" .,:;[]()")
    if not raw_author:
        return ""
    first = re.split(r"\s+and\s+|\s*&\s*|,|，|、|;|；", raw_author, maxsplit=1)[0]
    first = re.sub(r"\bet\s+al\.?$", "", first, flags=re.IGNORECASE).strip(" .")
    return first or raw_author


def extract_author_year(name: str, citation: str, docname: str) -> tuple[str, str]:
    haystacks = [name, citation, docname]

    for text in haystacks:
        compact = re.search(r"\b([A-Z][A-Za-z'’.-]{1,40})(19|20)\d{2}\b", text)
        if compact:
            return compact.group(1), re.search(r"(19|20)\d{2}", compact.group(0)).group(0)

    for text in haystacks:
        match = re.search(
            r"\b([A-Z][A-Za-z'’.-]{1,40})(?:\s+et\s+al\.?)?[, ]+\s*((?:19|20)\d{2})\b",
            text,
            re.IGNORECASE,
        )
        if match:
            return normalize_author(match.group(1)), match.group(2)

    year_match = re.search(r"(19|20)\d{2}", " ".join(haystacks))
    year = year_match.group(0) if year_match else "unknown-year"
    author = normalize_author(citation) or normalize_author(docname) or "Source"
    return author, year


def citation_label(text_obj) -> str:
    name = getattr(text_obj, "name", "") or ""
    doc = getattr(text_obj, "doc", None)
    citation = ""
    docname = ""
    if doc is not None:
        citation = getattr(doc, "formatted_citation", "") or getattr(doc, "citation", "")
        docname = getattr(doc, "docname", "")

    author, year = extract_author_year(name, citation, docname)
    pages = extract_page_range(name)
    locator = f", pp. {pages}" if pages else ""
    return f"{author} {year}{locator}"


def source_label_from_context(context: dict) -> str:
    label = context.get("label", "")
    return re.sub(r", pp\..*$", "", label).strip() or label


def text_context(text_obj) -> dict:
    doc = getattr(text_obj, "doc", None)
    return {
        "label": citation_label(text_obj),
        "text": clean_excerpt(text_obj.text),
        "source_type": "paper",
        "citation": (
            getattr(doc, "formatted_citation", "") or getattr(doc, "citation", "")
            if doc is not None
            else ""
        ),
        "docname": getattr(doc, "docname", "") if doc is not None else "",
        "name": getattr(text_obj, "name", ""),
    }


async def retrieve_paper_contexts(
    project_root: Path,
    index_name: str,
    search_query: str,
    settings,
    *,
    top_k: int,
    doc_top_n: int,
    broad_collection: bool = False,
) -> list[dict]:
    from paperqa.agents.search import SearchDocumentStorage, SearchIndex
    from paperqa.docs import Docs

    index = SearchIndex(
        index_name=index_name,
        index_directory=project_root / "data" / "indexes",
        storage=SearchDocumentStorage.PICKLE_COMPRESSED,
    )
    combined = Docs(name=index_name)
    loaded_locations: set[str] = set()
    index_files = await index.index_files

    if broad_collection and len(index_files) <= int(os.environ.get("PQA_FALLBACK_ALL_DOC_LIMIT", "25")):
        contexts = []
        for file_location in index_files.keys():
            docs = await index.get_saved_object(file_location)
            if docs is None:
                continue
            merge_docs(combined, docs)
            loaded_locations.add(file_location)
            if docs.texts:
                contexts.append(text_context(docs.texts[0]))
        if contexts:
            return contexts[:top_k]
    else:
        try:
            search_results = await index.query(
                query=search_query,
                top_n=doc_top_n,
                keep_filenames=True,
            )
        except Exception as exc:
            if os.environ.get("PQA_STRICT", "0").strip().lower() in {"1", "true", "yes"}:
                raise
            print(f"PaperQA index search failed, continuing without paper evidence: {exc}", file=sys.stderr, flush=True)
            search_results = []

        for docs, file_location in search_results:
            merge_docs(combined, docs)
            loaded_locations.add(file_location)

    if not loaded_locations and len(index_files) <= int(os.environ.get("PQA_FALLBACK_ALL_DOC_LIMIT", "25")):
        for file_location in index_files.keys():
            docs = await index.get_saved_object(file_location)
            if docs is None:
                continue
            merge_docs(combined, docs)
            loaded_locations.add(file_location)

    if not combined.texts:
        return []

    matches = await combined.retrieve_texts(search_query, top_k, settings=settings)
    contexts = []
    seen: set[str] = set()
    for rank, text_obj in enumerate(matches, start=1):
        context = text_context(text_obj)
        context["score"] = max(top_k - rank + 1, 1)
        key = context["label"] + context["text"][:80]
        if key in seen:
            continue
        seen.add(key)
        contexts.append(context)
    return contexts


def obsidian_uri_for(path: Path) -> str:
    vault = os.environ.get("OBSIDIAN_VAULT_ID", "").strip() or os.environ.get("OBSIDIAN_VAULT_NAME", "").strip()
    if not vault:
        return ""
    try:
        relative = path.resolve().relative_to(WIKI_ROOT.resolve())
        file_target = relative.with_suffix("").as_posix()
        return (
            "obsidian://open?"
            + "vault="
            + quote(vault, safe="")
            + "&file="
            + quote(file_target, safe="")
        )
    except (OSError, ValueError):
        return "obsidian://open?path=" + quote(str(path), safe="")


def source_preview(text: str, max_chars: int = 700) -> str:
    text = re.sub(r"\A---\s.*?\n---\s*", "", text.strip(), flags=re.DOTALL)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= max_chars:
        return text
    return text[:max_chars].rsplit(" ", 1)[0] + "..."


def _wiki_page_meta(path: Path) -> tuple[list[dict], str]:
    """Extract structured paper references and source PDF path.
    For paper pages: returns its own title+citation+links, and empty refs.
    For aggregate pages: resolves each source paper_id to title+citation+links.
    Returns (refs, pdf_path) where each ref is {title, citation, obsidian_uri, pdf_uri}."""
    try:
        content = path.read_text(encoding="utf-8-sig", errors="replace")
    except OSError:
        return [], ""
    fields = parse_simple_frontmatter(content)
    pdf_path = str(fields.get("source_pdf", "")).strip()
    refs: list[dict] = []

    source_type = wiki_source_type(path, WIKI_ROOT)
    if source_type == "wiki_paper_page":
        # Paper page is itself a reference — return its own metadata, not nested refs
        return [], pdf_path

    # Aggregate page: resolve source paper_ids to titles
    sources = fields.get("sources", [])
    if isinstance(sources, list):
        for src in sources:
            src_str = str(src).strip()
            if not src_str:
                continue
            paper_path = WIKI_ROOT / "papers" / f"{src_str}.md"
            title = src_str  # fallback
            citation = ""
            src_pdf = ""
            obs_uri = obsidian_uri_for(paper_path) if paper_path.exists() else ""
            if paper_path.exists():
                try:
                    pc = paper_path.read_text(encoding="utf-8-sig", errors="replace")
                    pf = parse_simple_frontmatter(pc)
                    title = str(pf.get("title", src_str)).strip() or src_str
                    citation = str(pf.get("citation", "")).strip()
                    src_pdf = str(pf.get("source_pdf", "")).strip()
                except OSError:
                    pass
            pdf_uri = _find_pdf_uri(src_pdf) if src_pdf else ""
            refs.append({
                "title": title,
                "citation": citation,
                "obsidian_uri": obs_uri,
                "pdf_uri": pdf_uri,
            })
    return refs, pdf_path


def _find_pdf_uri(source_pdf: str) -> str:
    """Given a relative source_pdf path like 'data/papers/paper.pdf', return an API URI."""
    if not source_pdf:
        return ""
    pdf_path = PROJECT_ROOT / source_pdf
    if pdf_path.exists():
        return "/api/pdfs/" + pdf_path.name
    return ""


CONTEXT_ROLE_INFO = {
    "wiki_aggregate": {
        "group": "wiki_aggregate",
        "title": "A. 概念与方法（LLM Wiki 汇总层）",
        "role": "跨论文综合（概念、方法、结论的提炼与比较）",
        "kind": "wiki aggregate structure",
        "instruction": "用于建立回答框架、概念关系、方法脉络和跨论文综合判断。它概括了多篇论文，不要把它当作唯一事实依据。",
    },
    "wiki_paper_page": {
        "group": "wiki_paper_page",
        "title": "B. 论文解读（LLM Wiki 论文页）",
        "role": "单篇论文的完整解读（研究问题、方法、结论、限制）",
        "kind": "wiki paper note",
        "instruction": "用于理解单篇论文的全貌，并帮助定位需要追溯的原文证据。它是对原文的转述和解读，不是原文本身。",
    },
    "paper": {
        "group": "paper_evidence",
        "title": "C. 原文验证（PaperQA 检索的原始片段）",
        "role": "论文原文片段，用于验证关键事实和精确引用",
        "kind": "paper evidence",
        "instruction": "事实性判断和引用优先以这一层为准；如果它与 Wiki 层不一致，优先说明原文证据。注意：其他层涉及的论文可能远多于这里列出的原文片段。",
    },
    "wiki": {
        "group": "wiki_other",
        "title": "D. 补充线索（其他 Wiki 页面）",
        "role": "补充线索",
        "kind": "wiki structure",
        "instruction": "作为补充线索使用，必要时再追溯到论文证据。",
    },
}


CONTEXT_GROUP_ORDER = ["wiki_aggregate", "wiki_paper_page", "paper_evidence", "wiki_other"]


def context_role_info(source_type: str | None) -> dict[str, str]:
    return CONTEXT_ROLE_INFO.get(source_type or "", CONTEXT_ROLE_INFO["wiki"])


def context_group_counts(contexts: list[dict]) -> dict[str, int]:
    counts = {group: 0 for group in CONTEXT_GROUP_ORDER}
    for context in contexts:
        group = context_role_info(context.get("source_type")).get("group", "wiki_other")
        counts[group] = counts.get(group, 0) + 1
    return {group: count for group, count in counts.items() if count}


def context_size(context: dict) -> int:
    return len(context.get("label", "")) + len(context.get("text", ""))


def fit_context_to_budget(context: dict, max_size: int) -> dict | None:
    if max_size <= 160:
        return None
    if context_size(context) <= max_size:
        return context
    trimmed = dict(context)
    text_budget = max(120, max_size - len(trimmed.get("label", "")) - 80)
    trimmed["text"] = clean_excerpt(trimmed.get("text", ""), max_chars=text_budget)
    trimmed["truncated_for_context_budget"] = True
    if context_size(trimmed) > max_size:
        trimmed["text"] = trimmed["text"][: max(80, text_budget - (context_size(trimmed) - max_size))]
    return trimmed if context_size(trimmed) <= max_size else None


def budget_contexts(contexts: list[dict]) -> tuple[list[dict], dict[str, Any]]:
    if not contexts:
        return [], {"raw_counts": {}, "selected_counts": {}, "selected_chars": 0, "total_char_budget": 0}

    # 128K context window, reserve ~30% for system prompt + answer + overhead
    total_char_budget = int_env("PQA_CONTEXT_TOTAL_CHAR_BUDGET", 300000)
    selected: list[dict] = []
    selected_chars = 0

    # Sort all contexts by relevance score — no group quotas, just one global ranking
    ranked = sorted(
        contexts,
        key=lambda item: (float(item.get("rank_score", item.get("score", 0)) or 0), -len(item.get("text", ""))),
        reverse=True,
    )
    for context in ranked:
        max_size = total_char_budget - selected_chars
        candidate = fit_context_to_budget(context, max_size)
        if candidate is None:
            continue
        size = context_size(candidate)
        selected.append(candidate)
        selected_chars += size

    meta = {
        "raw_counts": context_group_counts(contexts),
        "selected_counts": context_group_counts(selected),
        "selected_chars": selected_chars,
        "total_char_budget": total_char_budget,
    }
    return selected, meta


def format_local_context(contexts: list[dict]) -> tuple[str, str, list[dict]]:
    if not contexts:
        return "", "", []

    grouped_sections: dict[str, list[str]] = {group: [] for group in CONTEXT_GROUP_ORDER}
    group_headers: dict[str, dict[str, str]] = {}
    references = []
    source_items: list[dict] = []
    seen_sources: set[str] = set()
    wiki_paper_labels: set[str] = set()  # track papers already covered by wiki items

    # First pass: collect wiki paper labels for dedup
    for context in contexts:
        source_type = context.get("source_type")
        if source_type and source_type != "paper":
            wiki_paper_labels.add(context.get("label", "").strip().lower())

    for context in contexts:
        label = context["label"]
        text = context["text"]
        source_type = context.get("source_type")
        role = context_role_info(source_type)
        group = role["group"]
        retrieval_method = context.get("retrieval_method") or ("paperqa" if source_type == "paper" else "keyword")
        score_bits = [f"retrieval_method: {retrieval_method}"]
        if context.get("semantic_score") is not None:
            score_bits.append(f"semantic_score: {float(context.get('semantic_score') or 0):.4f}")
        if context.get("match_score") is not None:
            score_bits.append(f"keyword_match_score: {context.get('match_score')}")
        if context.get("truncated_for_context_budget"):
            score_bits.append("context_note: truncated_to_fit_answer_budget")
        group_headers[group] = role
        grouped_sections.setdefault(group, []).append(
            f"[{label}]\nsource_kind: {role['kind']}\n" + "\n".join(score_bits) + f"\n{text}"
        )
        if source_type == "paper":
            citation = context.get("citation") or context.get("docname") or label
            source_label = source_label_from_context(context)
            if source_label.strip().lower() in wiki_paper_labels:
                continue
            source_key = f"paper:{source_label}"
            if source_key not in seen_sources:
                seen_sources.add(source_key)
                references.append(f"- {source_label}: {citation}")
                docname = context.get("docname", "")
                pdf_uri = ""
                if docname:
                    pdf_uri = _find_pdf_uri(f"data/papers/{docname}.pdf") or _find_pdf_uri(f"data/papers/{docname}")
                source_items.append(
                    {
                        "type": "paper",
                        "label": source_label,
                        "citation": citation,
                        "source_group": role["group"],
                        "source_role": role["role"],
                        "retrieval_method": retrieval_method,
                        "pdf_uri": pdf_uri,
                    }
                )
        else:
            path = Path(context.get("path", ""))
            source_key = f"wiki:{path or label}"
            if source_key not in seen_sources:
                seen_sources.add(source_key)
                refs, source_pdf = _wiki_page_meta(path)
                item = {
                    "type": "wiki",
                    "label": label,
                    "wiki_layer": source_type,
                    "source_group": role["group"],
                    "source_role": role["role"],
                    "path": str(path),
                    "relative_path": path.relative_to(Path(__file__).resolve().parents[1]).as_posix()
                    if path.is_absolute() and Path(__file__).resolve().parents[1] in path.parents
                    else str(path),
                    "obsidian_uri": obsidian_uri_for(path),
                    "pdf_uri": _find_pdf_uri(source_pdf),
                    "preview": source_preview(text),
                    "retrieval_method": retrieval_method,
                    "semantic_score": context.get("semantic_score"),
                    "heading": context.get("heading", ""),
                    "papers_referenced": refs,
                }
                references.append(f"- {label}")
                source_items.append(item)

    package_sections = []
    for group in CONTEXT_GROUP_ORDER:
        entries = grouped_sections.get(group) or []
        if not entries:
            continue
        role = group_headers.get(group)
        if not role:
            continue
        package_sections.append(
            f"## {role['title']}\n"
            f"role: {role['role']}\n"
            f"use_rule: {role['instruction']}\n\n"
            + "\n\n".join(entries)
        )
    context_text = "# LOCAL_KNOWLEDGE_PACKAGE\n\n" + "\n\n".join(package_sections)
    return context_text, "\n".join(references), source_items


def synthesize_evidence_plan(question: str, context_text: str) -> tuple[str, dict]:
    prompt = f"""
你现在只做“证据合成计划”，不要回答用户。

用户问题：
{question}

本地材料如下。它已经按来源角色分层：
- A. LLM Wiki 汇总层：概念、方法、结论、综述性综合，用来建立回答框架和跨论文关系。
- B. LLM Wiki 论文页：单篇论文的研究问题、方法、结论、限制，用来定位相关论文。
- C. PaperQA 原文证据片段：最接近论文原文，用来支撑事实性判断和引用。

<LOCAL_CONTEXT>
{context_text}
</LOCAL_CONTEXT>

请用简短中文生成内部计划，必须按下面结构：

1. 问题重述：用户真正想问什么。
2. 回答框架：优先从 A 层抽取 2-5 个组织角度，不要照抄 A 层原文。
3. 证据回查：指出 B/C 层中哪些论文或片段能支撑这些角度。
4. 关系判断：证据之间是支持、补充、条件限定，还是存在冲突。
5. 证据缺口：哪些判断只有 Wiki 线索，缺少原文片段支撑。
6. 最终回答策略：说明最终回答应先给什么判断、再展开哪些依据。

不要复述材料原文，不要写最终答案。计划是给最终回答阶段使用的内部路标。
"""
    return call_deepseek(
        [{"role": "system", "content": DEFAULT_SYSTEM_PROMPT}, {"role": "user", "content": prompt}],
        temperature=float_env("PQA_SYNTHESIS_TEMPERATURE", 0.2),
        timeout=120,
    )


def answer_messages(question: str, context_text: str, synthesis_plan: str = "") -> list[dict[str, str]]:
    if not context_text:
        return [
            {"role": "system", "content": DEFAULT_SYSTEM_PROMPT},
            {"role": "user", "content": question},
        ]

    prompt = (
        "你不是知识库复读器，而是科研讨论助手。下面材料只是证据和背景，不是最终答案模板。"
        "请先综合判断，再解释理由；不要按检索材料的原始顺序逐条复述。"
        "A 层汇总 Wiki 用来形成回答框架，B 层论文页用来理解论文位置，C 层原文片段用来支撑事实判断。"
        "事实性结论要尽量附上材料中的完整引用标签，例如 [Wang 2018, pp. 3-4]；"
        "解释、比较和推断可以由你完成，但要把推断和论文证据区分开。"
        "如果证据之间存在差异，要指出差异；如果证据不足，要直接说明。"
        "回答风格要像研究伙伴讨论：先给结论，再展开依据，避免 Wiki 条目式罗列。"
        "不要使用 pqac 这类内部编号。\n\n"
        "<SYNTHESIS_PLAN>\n"
        f"{synthesis_plan.strip() if synthesis_plan else '无单独计划；请在内部完成证据筛选和答案规划。'}\n"
        "</SYNTHESIS_PLAN>\n\n"
        "<LOCAL_CONTEXT>\n"
        f"{context_text}\n"
        "</LOCAL_CONTEXT>\n\n"
        f"用户问题：{question}"
    )
    prompt = (
        "重要：LOCAL_CONTEXT 是三段式知识包。"
        "必须先使用 A. LLM Wiki 汇总层确定回答框架和跨论文关系；"
        "再使用 B. LLM Wiki 论文页判断哪些论文处在这个框架中的什么位置；"
        "最后用 C. PaperQA 原文证据片段支撑事实性判断。"
        "不要把 Wiki 原文当作最终答案复述；要把它重新组织成面向用户问题的研究讨论。"
        "如果某个判断只有 A/B 层线索但缺少 C 层原文证据，请明确说明证据强度有限。"
        "如果 C 层证据与 A/B 层概括不一致，以 C 层证据为准并解释差异。\n\n"
        + prompt
    )
    return [
        {"role": "system", "content": DEFAULT_SYSTEM_PROMPT},
        {"role": "user", "content": prompt},
    ]


async def answer_chat(
    question: str,
    *,
    project_root: Path,
    index_name: str,
    knowledge: str,
) -> dict:
    contexts: list[dict] = []
    search_query = ""
    query_package: dict[str, Any] = {}
    context_budget_meta: dict[str, Any] = {}
    wiki_retrieval_meta: dict[str, Any] = {}

    if knowledge != "never":
        settings = make_settings(project_root, index_name, rebuild_index=False)
        search_query = await build_search_query(question)
        query_package = build_query_package(question, search_query)
        wiki_hits, wiki_retrieval_meta = retrieve_wiki_contexts(project_root, query_package)
        paper_hits = await retrieve_paper_contexts(
            project_root,
            index_name,
            query_package.get("paper_search_query", search_query or question),
            settings,
            top_k=int(os.environ.get("PQA_CONTEXT_TOP_K", "50")),
            doc_top_n=int(os.environ.get("PQA_DOC_TOP_N", "50")),
            broad_collection=False,
        )
        contexts, context_budget_meta = budget_contexts(wiki_hits + paper_hits)
        context_budget_meta = {**wiki_retrieval_meta, **context_budget_meta}

    context_text, references, source_items = format_local_context(contexts)
    synthesis_plan = ""
    plan_usage: dict = {}
    if context_text and os.environ.get("PQA_SYNTHESIS_LAYER", "1").lower() not in {"0", "false", "no"}:
        synthesis_plan, plan_usage = synthesize_evidence_plan(question, context_text)

    final_temperature = (
        float_env("PQA_KNOWLEDGE_TEMPERATURE", 0.45)
        if context_text
        else float_env("PQA_CHAT_TEMPERATURE", 0.55)
    )
    answer, answer_usage = call_deepseek(
        answer_messages(question, context_text, synthesis_plan),
        temperature=final_temperature,
    )
    usage = merge_usage(plan_usage, answer_usage)
    route = "knowledge" if contexts else "chat"
    return {
        "question": question,
        "answer": answer.strip(),
        "references": references,
        "source_items": source_items,
        "has_successful_answer": True,
        "context_count": len(contexts),
        "cost": 0,
        "route": route,
        "knowledge_mode": knowledge,
        "model": deepseek_model_name(),
        "synthesis_layer": bool(synthesis_plan),
        "search_query": search_query,
        "retrieval": {
            "intent": query_package.get("intent", ""),
            "variants": query_package.get("variants", []),
            "preferred_folders": query_package.get("preferred_folders", []),
            "paper_search_query": query_package.get("paper_search_query", ""),
            "semantic_enabled": semantic_wiki_enabled(),
            **context_budget_meta,
        },
        "usage": usage,
    }


def cmd_index(args: argparse.Namespace) -> int:
    from paperqa.agents import build_index

    project_root = Path(__file__).resolve().parents[1]
    paper_directory = args.paper_directory or project_root / "data" / "papers"
    settings = make_settings(
        project_root,
        args.index_name,
        rebuild_index=True,
        paper_directory=paper_directory,
        sync_with_paper_directory=not args.no_sync,
    )
    result = maybe_await(
        build_index(
            index_name=args.index_name,
            directory=paper_directory,
            settings=settings,
        )
    )
    print(f"Index built: {args.index_name}")
    print(f"Index object: {type(result).__name__}")
    return 0


def cmd_chat(args: argparse.Namespace) -> int:
    project_root = Path(__file__).resolve().parents[1]
    apply_llm_model_override(getattr(args, "model", None))
    payload = maybe_await(
        answer_chat(
            args.question,
            project_root=project_root,
            index_name=args.index_name,
            knowledge=args.knowledge,
        )
    )
    if args.format == "json":
        print(json.dumps(payload, ensure_ascii=False))
    else:
        print(payload["answer"])
        if payload.get("references"):
            print("\nReferences:")
            print(payload["references"])
    return 0


def cmd_ask(args: argparse.Namespace) -> int:
    knowledge = {
        "auto": "auto",
        "paper": "always",
        "chat": "never",
    }[args.route]
    args.knowledge = knowledge
    return cmd_chat(args)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Zotero PaperQA assistant wrapper.")
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress most info-level runtime logs.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    index_parser = subparsers.add_parser("index", help="Build the PaperQA index.")
    index_parser.add_argument("--index-name", default="papers")
    index_parser.add_argument(
        "--paper-directory",
        type=Path,
        default=None,
        help="Directory of PDFs to index. Defaults to data/papers.",
    )
    index_parser.add_argument(
        "--no-sync",
        action="store_true",
        help="Do not remove index entries for files absent from --paper-directory.",
    )
    index_parser.set_defaults(func=cmd_index)

    chat_parser = subparsers.add_parser("chat", help="Chat with DeepSeek and optional local context.")
    chat_parser.add_argument("--index-name", default="papers")
    chat_parser.add_argument(
        "--knowledge",
        choices=["auto", "always", "never"],
        default=os.environ.get("PQA_KNOWLEDGE_MODE", "auto"),
        help="Whether to augment DeepSeek with the local wiki/paper index.",
    )
    chat_parser.add_argument("--format", choices=["text", "json"], default="text")
    chat_parser.add_argument(
        "--model",
        choices=["deepseek/deepseek-v4-flash", "deepseek/deepseek-v4-pro"],
        default=None,
        help="Override the DeepSeek model for this request.",
    )
    chat_parser.add_argument("question")
    chat_parser.set_defaults(func=cmd_chat)

    ask_parser = subparsers.add_parser("ask", help="Backward-compatible alias for chat.")
    ask_parser.add_argument("--index-name", default="papers")
    ask_parser.add_argument(
        "--route",
        choices=["auto", "paper", "chat"],
        default=os.environ.get("PQA_ROUTE_DEFAULT", "auto"),
    )
    ask_parser.add_argument(
        "--paper-mode",
        choices=["direct", "agent"],
        default="direct",
        help=argparse.SUPPRESS,
    )
    ask_parser.add_argument("--format", choices=["text", "json"], default="text")
    ask_parser.add_argument("question")
    ask_parser.set_defaults(func=cmd_ask)

    return parser


def main() -> int:
    project_root = Path(__file__).resolve().parents[1]
    tmp_dir = project_root / "tmp"
    pqa_home = project_root / ".pqa"
    tmp_dir.mkdir(parents=True, exist_ok=True)
    pqa_home.mkdir(parents=True, exist_ok=True)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    os.environ["TEMP"] = str(tmp_dir)
    os.environ["TMP"] = str(tmp_dir)
    os.environ["PQA_HOME"] = str(pqa_home)
    configure_local_packages(project_root)
    load_dotenv(project_root / ".env")
    normalize_provider_env()
    args = build_parser().parse_args()
    configure_logging(args.quiet)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
