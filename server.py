"""FastAPI backend for Zotero PaperQA Research Assistant."""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel

PROJECT_ROOT = Path(__file__).resolve().parent
API_SCRIPT = PROJECT_ROOT / "scripts" / "pqa-api.py"
CONVERSATIONS_DIR = PROJECT_ROOT / "data" / "conversations"
PAPERS_DIR = PROJECT_ROOT / "data" / "papers"
WIKI_DIR = PROJECT_ROOT / "wiki"

app = FastAPI(title="Research Assistant API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


# ── Env ────────────────────────────────────────────────────────────────

def _load_dotenv() -> None:
    dotenv_path = PROJECT_ROOT / ".env"
    if not dotenv_path.exists(): return
    for raw_line in dotenv_path.read_text(encoding="utf-8-sig").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line: continue
        key, value = line.split("=", 1)
        key, value = key.strip(), value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}: value = value[1:-1]
        os.environ.setdefault(key, value)

_load_dotenv()


# ── Models ─────────────────────────────────────────────────────────────

class ChatRequest(BaseModel):
    question: str
    knowledge_mode: str = "auto"
    model: str = "deepseek/deepseek-v4-flash"

class ConversationMeta(BaseModel):
    id: str
    title: str
    updated_at: str
    message_count: int

class Conversation(BaseModel):
    id: str
    title: str
    created_at: str
    updated_at: str
    messages: list[dict]


# ── Helpers ────────────────────────────────────────────────────────────

def _run(cmd: list[str], timeout: int = 600, env_overrides: dict | None = None) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    pkg = str(PROJECT_ROOT / ".packages")
    existing = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = pkg if not existing else pkg + os.pathsep + existing
    env["PYTHONUTF8"] = "1"
    if env_overrides: env.update({k: v for k, v in env_overrides.items() if v})
    return subprocess.run(cmd, cwd=PROJECT_ROOT, env=env,
                          capture_output=True, text=True, encoding="utf-8", errors="replace",
                          timeout=timeout, check=False)

def _model_env(model: str) -> dict[str, str]:
    return {"PQA_LLM_MODEL": model, "PQA_SUMMARY_LLM_MODEL": model,
            "PQA_AGENT_LLM_MODEL": model, "PQA_ENRICHMENT_LLM_MODEL": model}

def _parse_json(stdout: str) -> dict:
    text = stdout.strip()
    if not text: return {"answer": "", "error": "empty response"}
    try: return json.loads(text)
    except json.JSONDecodeError:
        s = text.find("{"); e = text.rfind("}")
        if s >= 0 and e > s: return json.loads(text[s:e + 1])
        return {"answer": text, "error": "json parse failed"}

def _new_id() -> str:
    return datetime.now().strftime("%Y%m%d-%H%M%S-") + hashlib.sha1(os.urandom(8)).hexdigest()[:6]


# ── Conversations ──────────────────────────────────────────────────────

def _list_convs() -> list[dict]:
    CONVERSATIONS_DIR.mkdir(parents=True, exist_ok=True)
    result = []
    for p in sorted(CONVERSATIONS_DIR.glob("*.json"), key=lambda x: x.stat().st_mtime, reverse=True):
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
            result.append({"id": p.stem, "title": d.get("title", p.stem),
                           "updated_at": d.get("updated_at", ""), "message_count": len(d.get("messages", []))})
        except (json.JSONDecodeError, OSError): pass
    return result

def _load_conv(conv_id: str) -> dict | None:
    p = CONVERSATIONS_DIR / f"{conv_id}.json"
    if not p.exists(): return None
    return json.loads(p.read_text(encoding="utf-8"))

def _save_conv(conv_id: str, messages: list[dict]) -> None:
    CONVERSATIONS_DIR.mkdir(parents=True, exist_ok=True)
    title = ""
    for m in messages:
        if m["role"] == "user": title = m["content"][:60]; break
    payload = {"id": conv_id, "title": title, "created_at": datetime.now().isoformat(timespec="seconds"),
               "updated_at": datetime.now().isoformat(timespec="seconds"), "messages": messages}
    (CONVERSATIONS_DIR / f"{conv_id}.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


# ── API Routes ─────────────────────────────────────────────────────────

@app.get("/api/conversations")
def list_conversations() -> list[dict]:
    return _list_convs()

@app.get("/api/conversations/{conv_id}")
def get_conversation(conv_id: str) -> dict:
    data = _load_conv(conv_id)
    if not data: raise HTTPException(404, "Conversation not found")
    return data

@app.delete("/api/conversations/{conv_id}")
def delete_conversation(conv_id: str) -> dict:
    p = CONVERSATIONS_DIR / f"{conv_id}.json"
    if p.exists(): p.unlink()
    return {"ok": True}

@app.post("/api/chat")
def chat(req: ChatRequest) -> dict:
    result = _run(
        [sys.executable, str(API_SCRIPT), "--quiet", "chat",
         "--index-name", "papers", "--knowledge", req.knowledge_mode,
         "--model", req.model, "--format", "json", req.question],
        timeout=900, env_overrides=_model_env(req.model),
    )
    if result.returncode != 0:
        detail = (result.stderr or result.stdout or "").strip()
        raise HTTPException(500, detail or "Chat request failed")
    data = _parse_json(result.stdout)
    return {
        "question": req.question,
        "answer": data.get("answer", "").strip(),
        "route": data.get("route", ""),
        "context_count": data.get("context_count", 0),
        "source_items": data.get("source_items", []),
        "references": data.get("references", ""),
        "retrieval": data.get("retrieval", {}),
        "usage": data.get("usage", {}),
        "synthesis_layer": data.get("synthesis_layer", False),
    }

@app.post("/api/conversations/{conv_id}/messages")
def save_messages(conv_id: str, messages: list[dict]) -> dict:
    _save_conv(conv_id, messages)
    return {"ok": True}

@app.get("/api/status")
def status() -> dict:
    papers = len([p for p in PAPERS_DIR.glob("*.pdf") if p.is_file()]) if PAPERS_DIR.exists() else 0
    wiki_pages = len([p for p in (WIKI_DIR / "papers").glob("*.md") if p.is_file()]) if (WIKI_DIR / "papers").exists() else 0
    return {"papers": papers, "wiki_pages": wiki_pages}

@app.get("/api/pdfs/{filename:path}")
def serve_pdf(filename: str):
    pdf_path = PAPERS_DIR / filename
    if not pdf_path.exists() or not pdf_path.is_file():
        raise HTTPException(404, "PDF not found")
    if pdf_path.resolve().parent.resolve() != PAPERS_DIR.resolve():
        raise HTTPException(403, "Access denied")
    return FileResponse(pdf_path, media_type="application/pdf")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=12556)
