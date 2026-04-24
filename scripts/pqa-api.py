from __future__ import annotations

import argparse
import asyncio
import inspect
import json
import logging
import os
import sys
from pathlib import Path

from paperqa.agents import ask as paperqa_ask
from paperqa.agents import build_index
from paperqa.settings import Settings


def load_dotenv(dotenv_path: Path) -> None:
    if not dotenv_path.exists():
        return

    for raw_line in dotenv_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if (
            len(value) >= 2
            and value[0] == value[-1]
            and value[0] in {"'", '"'}
        ):
            value = value[1:-1]
        os.environ[key] = value


def normalize_provider_env() -> None:
    openai_key = os.environ.get("OPENAI_API_KEY")
    openai_base = os.environ.get("OPENAI_BASE_URL", "")
    if openai_key and "dashscope.aliyuncs.com" in openai_base:
        os.environ.setdefault("DASHSCOPE_API_KEY", openai_key)
        os.environ.setdefault("DASHSCOPE_API_BASE", openai_base)


def maybe_await(value):
    if inspect.isawaitable(value):
        return asyncio.run(value)
    return value


def configure_logging(quiet: bool) -> None:
    if quiet:
        logging.disable(logging.INFO)


def make_settings(project_root: Path, index_name: str, rebuild_index: bool) -> Settings:
    llm = os.environ.get("PQA_LLM_MODEL", "dashscope/qwen-plus")
    summary_llm = os.environ.get("PQA_SUMMARY_LLM_MODEL", llm)
    embedding = os.environ.get("PQA_EMBEDDING_MODEL", "openai/text-embedding-v4")
    encoding_format = os.environ.get("PQA_EMBEDDING_ENCODING_FORMAT", "float")

    return Settings(
        llm=llm,
        summary_llm=summary_llm,
        embedding=embedding,
        embedding_config={
            "batch_size": 10,
            "kwargs": {"encoding_format": encoding_format},
        },
        parsing={
            "multimodal": False,
            "use_doc_details": False,
            "enrichment_llm": llm,
        },
        agent={
            "agent_llm": llm,
            "rebuild_index": rebuild_index,
            "index": {
                "name": index_name,
                "paper_directory": project_root / "data" / "papers",
                "index_directory": project_root / "data" / "indexes",
                "concurrency": 1,
                "batch_size": 1,
                "sync_with_paper_directory": True,
            },
        },
    )


def cmd_index(args: argparse.Namespace) -> int:
    project_root = Path(__file__).resolve().parents[1]
    settings = make_settings(project_root, args.index_name, rebuild_index=True)
    result = maybe_await(
        build_index(
            index_name=args.index_name,
            directory=project_root / "data" / "papers",
            settings=settings,
        )
    )
    print(f"Index built: {args.index_name}")
    print(f"Index object: {type(result).__name__}")
    return 0


def response_to_payload(response) -> dict:
    session = response.session
    return {
        "question": session.question,
        "answer": session.answer or session.formatted_answer or "",
        "references": session.references or "",
        "has_successful_answer": session.has_successful_answer,
        "context_count": len(session.contexts),
        "cost": session.cost,
    }


def cmd_ask(args: argparse.Namespace) -> int:
    project_root = Path(__file__).resolve().parents[1]
    settings = make_settings(project_root, args.index_name, rebuild_index=False)
    response = maybe_await(paperqa_ask(args.question, settings=settings))
    payload = response_to_payload(response)
    if args.format == "json":
        print(json.dumps(payload, ensure_ascii=False))
    else:
        print(payload["answer"])
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Stable Python wrapper for PaperQA.")
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress most info-level runtime logs.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    index_parser = subparsers.add_parser("index", help="Build the PaperQA index.")
    index_parser.add_argument("--index-name", default="papers")
    index_parser.set_defaults(func=cmd_index)

    ask_parser = subparsers.add_parser("ask", help="Ask a question with PaperQA.")
    ask_parser.add_argument("--index-name", default="papers")
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
    load_dotenv(project_root / ".env")
    normalize_provider_env()
    args = build_parser().parse_args()
    configure_logging(args.quiet)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
