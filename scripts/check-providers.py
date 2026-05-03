from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.request
from pathlib import Path
from urllib.error import HTTPError, URLError


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def load_dotenv(dotenv_path: Path) -> None:
    if not dotenv_path.exists():
        raise FileNotFoundError("Missing .env. Copy .env.example to .env first.")

    for raw_line in dotenv_path.read_text(encoding="utf-8-sig").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        os.environ[key.strip()] = value


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
    except URLError as exc:
        raise RuntimeError(f"Connection failed: {exc.reason}") from exc


def deepseek_chat(args: argparse.Namespace) -> int:
    api_key = os.environ.get("DEEPSEEK_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("DEEPSEEK_API_KEY is missing in .env.")

    model = args.model or os.environ.get("PQA_LLM_MODEL", "deepseek-chat")
    api_model = model.removeprefix("deepseek/")
    response = post_json(
        "https://api.deepseek.com/chat/completions",
        {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        {
            "model": api_model,
            "messages": [{"role": "user", "content": args.prompt}],
        },
        args.timeout,
    )
    answer = response["choices"][0]["message"].get("content", "")
    print(f"deepseek chat: status 200, model={api_model}, response_chars={len(answer)}")
    return 0


def zhipu_embedding(args: argparse.Namespace) -> int:
    api_key = os.environ.get("OPENAI_API_KEY", "").strip()
    base_url = os.environ.get("OPENAI_BASE_URL", "").strip().rstrip("/")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is missing in .env.")
    if not base_url:
        raise RuntimeError("OPENAI_BASE_URL is missing in .env.")

    model = args.model or os.environ.get("PQA_EMBEDDING_MODEL", "embedding-3")
    api_model = model.removeprefix("openai/")
    payload: dict[str, object] = {
        "model": api_model,
        "input": args.input,
    }
    dimensions = args.dimensions or os.environ.get("PQA_EMBEDDING_DIMENSIONS", "")
    if dimensions:
        payload["dimensions"] = int(dimensions)

    response = post_json(
        f"{base_url}/embeddings",
        {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        payload,
        args.timeout,
    )
    embedding = response["data"][0]["embedding"]
    print(f"zhipu embedding: status 200, model={api_model}, dimensions={len(embedding)}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate configured LLM providers.")
    parser.add_argument("--timeout", type=int, default=60)
    subparsers = parser.add_subparsers(dest="command", required=True)

    deepseek_parser = subparsers.add_parser("deepseek-chat")
    deepseek_parser.add_argument("--model")
    deepseek_parser.add_argument("--prompt", default="Reply with ok only.")
    deepseek_parser.set_defaults(func=deepseek_chat)

    zhipu_parser = subparsers.add_parser("zhipu-embedding")
    zhipu_parser.add_argument("--model")
    zhipu_parser.add_argument("--dimensions", type=int)
    zhipu_parser.add_argument("--input", default="embedding connectivity test")
    zhipu_parser.set_defaults(func=zhipu_embedding)
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
