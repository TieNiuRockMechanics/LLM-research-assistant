from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import quote

import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parent
PAPERS_DIR = PROJECT_ROOT / "data" / "papers"
INDEX_NAME = "papers"
MANIFEST_PATH = PROJECT_ROOT / "data" / "zotero-import-manifest.json"
WIKI_DIR = PROJECT_ROOT / "wiki"
WIKI_INBOX_DIR = WIKI_DIR / "inbox"
API_SCRIPT = PROJECT_ROOT / "scripts" / "pqa-api.py"
UPDATE_PAPER_DATABASE_SCRIPT = PROJECT_ROOT / "scripts" / "update_paper_database.py"
UPDATE_WIKI_DATABASE_SCRIPT = PROJECT_ROOT / "scripts" / "update_wiki_database.py"
CONVERSATIONS_DIR = PROJECT_ROOT / "data" / "conversations"
OBSIDIAN_VAULT_PATH = WIKI_DIR

SOURCE_GROUP_ORDER = ["wiki_aggregate", "wiki_paper_page", "paper_evidence", "wiki_other"]


# ── Helpers ────────────────────────────────────────────────────────────

def _source_group_key(item: dict) -> str:
    return item.get("source_group") or item.get("wiki_layer") or ("paper_evidence" if item.get("type") != "wiki" else "wiki_other")

def _source_group_title(group: str) -> str:
    return {"wiki_aggregate": "思路来源", "wiki_paper_page": "论文笔记",
            "paper_evidence": "论文证据", "wiki_other": "其他线索"}.get(group, group)

def _route_label(r: str) -> str:
    return {"chat": "直接对话", "knowledge": "参考知识库", "status": "本地状态"}.get(r, r or "")

def _signal(payload: dict) -> tuple[str, str]:
    r = payload.get("route", "")
    n = int(payload.get("context_count", 0) or 0)
    if r == "status": return "⬤", "本地状态"
    if r == "knowledge" or n > 0: return "⬤", "已参考本地 Wiki 或论文数据库"
    return "⬤", "DeepSeek 直接回答"

def load_dotenv(dotenv_path: Path) -> None:
    if not dotenv_path.exists(): return
    for raw_line in dotenv_path.read_text(encoding="utf-8-sig").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line: continue
        key, value = line.split("=", 1)
        key, value = key.strip(), value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}: value = value[1:-1]
        os.environ.setdefault(key, value)

def _build_env(overrides: dict[str, str] | None = None) -> dict[str, str]:
    env = os.environ.copy()
    pkg = str(PROJECT_ROOT / ".packages")
    existing = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = pkg if not existing else pkg + os.pathsep + existing
    env["PYTHONUTF8"] = "1"
    if overrides: env.update({k: v for k, v in overrides.items() if v})
    return env

def _model_env(model: str | None) -> dict[str, str]:
    if not model: return {}
    return {"PQA_LLM_MODEL": model, "PQA_SUMMARY_LLM_MODEL": model,
            "PQA_AGENT_LLM_MODEL": model, "PQA_ENRICHMENT_LLM_MODEL": model}

def _run(cmd: list[str], timeout: int = 600, env_overrides: dict | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=PROJECT_ROOT, env=_build_env(env_overrides),
                          capture_output=True, text=True, encoding="utf-8", errors="replace",
                          timeout=timeout, check=False)

def _run_pqa(command: list[str], timeout: int = 600, llm_model: str | None = None) -> subprocess.CompletedProcess[str]:
    return _run([sys.executable, str(API_SCRIPT), "--quiet", *command],
                timeout=timeout, env_overrides=_model_env(llm_model))

def _parse_json(stdout: str) -> dict:
    text = stdout.strip()
    if not text: raise ValueError("命令没有返回 JSON。")
    try: return json.loads(text)
    except json.JSONDecodeError:
        s = text.find("{"); e = text.rfind("}")
        if s >= 0 and e > s: return json.loads(text[s:e + 1])
        raise

def ask_assistant(question: str, knowledge_mode: str, llm_model: str) -> dict:
    result = _run_pqa(["chat", "--index-name", INDEX_NAME, "--knowledge", knowledge_mode,
                        "--model", llm_model, "--format", "json", question],
                       timeout=900, llm_model=llm_model)
    if result.returncode != 0:
        detail = (result.stderr or result.stdout or "").strip()
        raise RuntimeError(detail or "Assistant request failed.")
    return _parse_json(result.stdout)

def _obsidian_uri(path: Path) -> str:
    vault = os.environ.get("OBSIDIAN_VAULT_ID", "").strip() or os.environ.get("OBSIDIAN_VAULT_NAME", "").strip()
    if not vault: return ""
    try:
        rel = path.resolve().relative_to(OBSIDIAN_VAULT_PATH.resolve())
        return "obsidian://open?vault=" + quote(vault, safe="") + "&file=" + quote(rel.with_suffix("").as_posix(), safe="")
    except (OSError, ValueError):
        return "obsidian://open?path=" + quote(str(path), safe="")


# ── Conversation persistence ────────────────────────────────────────────

def _list_convs() -> list[dict]:
    if not CONVERSATIONS_DIR.exists(): return []
    result = []
    for p in sorted(CONVERSATIONS_DIR.glob("*.json"), key=lambda x: x.stat().st_mtime, reverse=True):
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
            result.append({"id": p.stem, "title": d.get("title", p.stem),
                           "updated_at": d.get("updated_at", ""), "n": len(d.get("messages", []))})
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

def _del_conv(conv_id: str) -> None:
    p = CONVERSATIONS_DIR / f"{conv_id}.json"
    if p.exists(): p.unlink()

def _new_id() -> str:
    return datetime.now().strftime("%Y%m%d-%H%M%S-") + hashlib.sha1(os.urandom(8)).hexdigest()[:6]


# ── CSS — ChatGPT-style design system ──────────────────────────────────

STYLE = """
<style>
:root {
    --main-surface: #ffffff;
    --sidebar-surface: #f9f9f9;
    --border-light: #e5e5e5;
    --border-medium: #d9d9d9;
    --text-primary: #0d0d0d;
    --text-secondary: #5d5d5d;
    --text-tertiary: #8e8e8e;
    --accent: #212121;
    --accent-text: #ffffff;
    --user-bubble: #f4f4f4;
    --hover-surface: #ececec;
}

.stApp { background: var(--main-surface); }

/* Remove default Streamlit padding */
.block-container { max-width: 768px; padding: 0 1.5rem 0.5rem; margin: 0 auto; }
[data-testid="stAppViewContainer"] > .main { background: var(--main-surface); }

/* Sidebar — ChatGPT style */
[data-testid="stSidebar"] { background: var(--sidebar-surface); border-right: 1px solid var(--border-light); }
[data-testid="stSidebar"] .block-container { padding: 0.6rem 0.6rem 0.4rem; }
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h1,
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h2,
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h3 { font-size: 0.92rem; font-weight: 600; padding: 0.25rem 0.25rem 0; color: var(--text-primary); }
[data-testid="stSidebar"] hr { margin: 0.5rem 0; border-color: var(--border-light); }

/* Chat messages — clean and minimal */
.stChatMessage { border: none !important; border-radius: 0 !important; background: transparent !important; padding: 0.6rem 0 !important; }
[data-testid="stChatMessageContent"] p { font-size: 0.938rem; line-height: 1.75; color: var(--text-primary); }
[data-testid="stChatMessageContent"] h1 { font-size: 1.1rem; font-weight: 600; margin: 1.2rem 0 0.4rem; }
[data-testid="stChatMessageContent"] h2 { font-size: 1rem; font-weight: 600; margin: 1rem 0 0.3rem; }
[data-testid="stChatMessageContent"] h3 { font-size: 0.95rem; font-weight: 600; margin: 0.8rem 0 0.25rem; }
[data-testid="stChatMessageContent"] code { font-size: 0.82rem; background: #f4f4f4; padding: 0.15em 0.35em; border-radius: 4px; }
[data-testid="stChatMessageContent"] pre { background: #f8f8f8; border: 1px solid var(--border-light); border-radius: 8px; padding: 0.8rem 1rem; overflow-x: auto; }
[data-testid="stChatMessageContent"] pre code { background: transparent; padding: 0; }
[data-testid="stChatMessageContent"] ul, [data-testid="stChatMessageContent"] ol { padding-left: 1.5rem; }
[data-testid="stChatMessageContent"] li { margin-bottom: 0.25rem; }

/* Chat avatar spacing */
[data-testid="stChatMessage"] [data-testid="chatAvatarIcon-user"] { background: #0d0d0d; }
[data-testid="stChatMessage"] [data-testid="chatAvatarIcon-assistant"] { background: #10a37f; }

/* Route indicator line */
.route-line { display: flex; align-items: center; gap: 0.4rem; margin-bottom: 0.25rem; font-size: 0.75rem; color: var(--text-tertiary); }
.route-dot { width: 6px; height: 6px; border-radius: 50%; display: inline-block; flex-shrink: 0; }
.dot-green { background: #10a37f; }
.dot-amber { background: #f0a030; }

/* Chat input — ChatGPT style rounded */
[data-testid="stChatInput"] { position: sticky; bottom: 0; padding: 0.75rem 0 1rem; background: linear-gradient(to bottom, transparent, var(--main-surface) 30%); }
[data-testid="stChatInput"] textarea {
    border-radius: 28px; border: 1px solid var(--border-medium);
    min-height: 52px; padding: 12px 20px; font-size: 0.938rem;
    box-shadow: 0 0 0 0 rgba(0,0,0,0); transition: box-shadow 0.15s, border-color 0.15s;
    background: var(--main-surface); color: var(--text-primary);
}
[data-testid="stChatInput"] textarea:focus {
    border-color: #999; box-shadow: 0 0 0 1px rgba(0,0,0,0.04);
    outline: none;
}
[data-testid="stChatInput"] textarea::placeholder { color: var(--text-tertiary); }

/* Buttons */
div.stButton > button {
    border-radius: 8px; font-size: 0.813rem; font-weight: 500;
    border: 1px solid var(--border-light); background: var(--main-surface);
    color: var(--text-primary); padding: 0.35rem 0.7rem;
    transition: background 0.1s;
}
div.stButton > button:hover { background: var(--hover-surface); }
div.stButton > button[kind="primary"] {
    background: var(--accent); border-color: var(--accent); color: var(--accent-text);
}
div.stButton > button[kind="primary"]:hover { background: #333; }

/* Expander */
.streamlit-expanderHeader { font-size: 0.813rem; color: var(--text-secondary); border-radius: 8px; }
.streamlit-expanderHeader:hover { background: var(--hover-surface); }

/* Sidebar conversation history items */
[data-testid="stSidebar"] .stButton { margin-bottom: 0; }
[data-testid="stSidebar"] div.stButton > button {
    border: none; background: transparent; border-radius: 8px;
    text-align: left; font-size: 0.813rem; padding: 0.45rem 0.6rem;
    white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
    width: 100%; color: var(--text-primary);
}
[data-testid="stSidebar"] div.stButton > button:hover { background: var(--hover-surface); }
[data-testid="stSidebar"] div.stButton > button[kind="primary"] { background: var(--hover-surface); color: var(--text-primary); }

/* Link buttons */
div.stLinkButton > a { font-size: 0.813rem; color: var(--text-secondary); }

/* Radio buttons in sidebar */
[data-testid="stSidebar"] .stRadio label { font-size: 0.75rem; }

/* Empty state */
.empty-state { padding: 3rem 1rem; text-align: center; }
.empty-state h2 { font-size: 1.15rem; color: var(--text-primary); margin-bottom: 2rem; font-weight: 500; }
.suggest-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.6rem; max-width: 600px; margin: 0 auto; }
.suggest-card { border: 1px solid var(--border-light); border-radius: 10px; padding: 0.7rem 0.9rem; cursor: pointer; transition: background 0.1s; font-size: 0.85rem; color: var(--text-secondary); text-align: left; }
.suggest-card:hover { background: var(--hover-surface); }
@media (max-width: 560px) { .suggest-grid { grid-template-columns: 1fr; } }

/* Source expander tweaks */
[data-testid="stExpander"] { border: 1px solid var(--border-light); border-radius: 8px; margin-top: 0.4rem; }
[data-testid="stExpander"] .streamlit-expanderContent { font-size: 0.85rem; }

/* Spinner */
[data-testid="stSpinner"] { border-color: var(--text-tertiary); }

/* Hide Streamlit's own header/deploy button */
[data-testid="stHeader"] { display: none; }
[data-testid="stDecoration"] { display: none; }
#MainMenu { display: none; }
footer { display: none; }
</style>
"""


# ── Sidebar ────────────────────────────────────────────────────────────

def render_sidebar() -> None:
    with st.sidebar:
        # Logo area
        cL, cR = st.columns([5, 1])
        with cL:
            st.markdown("#### Research Assistant")
        with cR:
            vault_ok = os.environ.get("OBSIDIAN_VAULT_NAME", "").strip() or os.environ.get("OBSIDIAN_VAULT_ID", "")
            if vault_ok:
                st.link_button("📓", _obsidian_uri(WIKI_DIR / "index.md"), help="在 Obsidian 中打开 Wiki")

        # New chat button
        if st.button("＋ 新对话", use_container_width=True):
            _persist_current()
            st.session_state.messages = []
            st.session_state.conv_id = ""
            st.session_state.last_payload = None
            st.rerun()

        st.divider()

        # Conversation history
        conversations = _list_convs()
        active_id = st.session_state.get("conv_id", "")
        if conversations:
            st.caption("对话历史")
            for c in conversations:
                title = c["title"] or "未命名对话"
                is_active = c["id"] == active_id
                cc = st.columns([9, 1])
                with cc[0]:
                    bt = st.button(title[:40], key=f"h_{c['id']}", use_container_width=True,
                                   type="primary" if is_active else "secondary",
                                   help=f"{c.get('n',0)} 条消息 · {c.get('updated_at','')[:16]}")
                    if bt:
                        _persist_current()
                        data = _load_conv(c["id"])
                        if data:
                            st.session_state.messages = data.get("messages", [])
                            st.session_state.conv_id = c["id"]
                            st.rerun()
                with cc[1]:
                    if st.button("✕", key=f"x_{c['id']}", help="删除"):
                        _del_conv(c["id"])
                        if active_id == c["id"]:
                            st.session_state.messages = []; st.session_state.conv_id = ""
                        st.rerun()
        else:
            st.caption("暂无对话历史")

        st.divider()

        # Settings
        with st.expander("⚙ 知识库模式"):
            km = st.session_state.knowledge_mode
            km_labels = {"auto": "自动", "always": "总是参考", "never": "不使用"}
            st.session_state.knowledge_mode = st.radio(
                "本地知识库", ["auto", "always", "never"],
                index=["auto", "always", "never"].index(km),
                format_func=km_labels.get, horizontal=True, label_visibility="collapsed",
            )

        # Library status
        with st.expander("📊 知识库"):
            n_pdf = len([p for p in PAPERS_DIR.glob("*.pdf") if p.is_file()]) if PAPERS_DIR.exists() else 0
            n_wiki = len([p for p in (WIKI_DIR / "papers").glob("*.md") if p.is_file()]) if (WIKI_DIR / "papers").exists() else 0
            st.caption(f"PDF: {n_pdf}  ·  Wiki 论文页: {n_wiki}")

        # Maintenance
        with st.expander("🔧 维护"):
            if st.button("同步 Zotero 论文", use_container_width=True):
                with st.spinner("扫描 Zotero..."):
                    try:
                        r = _run([sys.executable, str(UPDATE_PAPER_DATABASE_SCRIPT), "--format", "json"], timeout=7200)
                        if r.returncode == 0:
                            pl = _parse_json(r.stdout)
                            n = pl.get("new_imported_count", 0)
                            st.success(f"新增 {n} 篇") if n else st.info("无新 PDF")
                        else:
                            st.error((r.stderr or r.stdout or "")[:300])
                    except Exception as exc: st.error(str(exc))
            if st.button("更新 LLM Wiki", use_container_width=True):
                with st.spinner("编译 Wiki..."):
                    try:
                        r = _run([sys.executable, str(UPDATE_WIKI_DATABASE_SCRIPT), "--format", "json", "--max-new", "0", "--resume"],
                                 timeout=7200, env_overrides=_model_env(st.session_state.llm_model))
                        if r.returncode == 0: st.success("完成")
                        else: st.error((r.stderr or r.stdout or "")[:300])
                    except Exception as exc: st.error(str(exc))


def _persist_current() -> None:
    msgs = st.session_state.get("messages", [])
    cid = st.session_state.get("conv_id", "")
    if msgs and cid: _save_conv(cid, msgs)


# ── Chat area ──────────────────────────────────────────────────────────

def _render_sources(payload: dict) -> None:
    items = payload.get("source_items") or []
    refs = payload.get("references", "").strip()
    if items:
        with st.expander("来源"):
            grouped: dict[str, list[tuple]] = {}
            for i, it in enumerate(items, 1):
                grouped.setdefault(_source_group_key(it), []).append((i, it))
            ordered = [g for g in SOURCE_GROUP_ORDER if g in grouped]
            ordered += [g for g in grouped if g not in ordered]
            for group in ordered:
                st.caption(f"**{_source_group_title(group)}**")
                for idx, it in grouped[group]:
                    label = it.get("label", "source")
                    role = it.get("source_role", "")
                    uri = it.get("obsidian_uri") or (_obsidian_uri(Path(it["path"])) if it.get("path") and it.get("type") == "wiki" else "")
                    st.markdown(f"{idx}. {label}")
                    bits = [f"角色：{role}"]
                    if it.get("heading"): bits.append(f"小节：{it['heading']}")
                    if it.get("retrieval_method"): bits.append(it["retrieval_method"])
                    st.caption(" · ".join(bits))
                    if uri: st.link_button("Obsidian", uri)
    elif refs:
        with st.expander("来源"):
            st.markdown(refs)


def render_messages() -> None:
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            payload = msg.get("payload")
            if payload and msg["role"] == "assistant":
                dot, label = _signal(payload)
                color = "dot-green" if payload.get("route") == "chat" else "dot-amber" if payload.get("context_count", 0) > 0 else "dot-green"
                st.markdown(f'<div class="route-line"><span class="route-dot {color}"></span>{label} · {_route_label(payload.get("route",""))} · {payload.get("context_count",0)} 上下文</div>', unsafe_allow_html=True)
            st.markdown(msg["content"])
            if payload and msg["role"] == "assistant":
                _render_sources(payload)


def handle_question(question: str) -> None:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner(""):
            try:
                payload = ask_assistant(question, st.session_state.knowledge_mode, st.session_state.llm_model)
            except Exception as exc:
                err = f"请求失败：{exc}"
                st.error(err)
                st.session_state.messages.append({"role": "assistant", "content": err})
                return

        answer = payload.get("answer", "").strip() or "这次没有返回可用答案。"
        dot, label = _signal(payload)
        color = "dot-green" if payload.get("route") == "chat" else "dot-amber" if payload.get("context_count", 0) > 0 else "dot-green"
        st.markdown(f'<div class="route-line"><span class="route-dot {color}"></span>{label} · {_route_label(payload.get("route",""))}</div>', unsafe_allow_html=True)
        st.markdown(answer)
        _render_sources(payload)

    st.session_state.last_payload = payload
    st.session_state.messages.append({"role": "assistant", "content": answer, "payload": payload})

    cid = st.session_state.get("conv_id", "")
    if not cid:
        cid = _new_id(); st.session_state.conv_id = cid
    _save_conv(cid, st.session_state.messages)


# ── Empty state ────────────────────────────────────────────────────────

SUGGESTIONS = [
    ("📄", "这些论文分别讲了什么？", "概览全库"),
    ("🔍", "根据我的论文库，裂缝网络连通性如何影响渗透率？", "知识检索"),
    ("💡", "帮我头脑风暴一个论文引言结构", "纯聊天"),
    ("📊", "知识库里有几篇论文？", "状态查询"),
]

def render_empty_state() -> None:
    st.markdown('<div class="empty-state"><h2>今天想研究什么？</h2>', unsafe_allow_html=True)
    st.markdown('<div class="suggest-grid">', unsafe_allow_html=True)
    for icon, question, hint in SUGGESTIONS:
        st.markdown(
            f'<div class="suggest-card" onclick=""><strong>{icon} {hint}</strong><br><span style="font-size:0.78rem;color:#8e8e8e">{question[:50]}…</span></div>',
            unsafe_allow_html=True)
    st.markdown('</div></div>', unsafe_allow_html=True)


# ── Main ───────────────────────────────────────────────────────────────

def main() -> None:
    load_dotenv(PROJECT_ROOT / ".env")

    st.set_page_config(page_title="Research Assistant", layout="wide", initial_sidebar_state="expanded")
    st.markdown(STYLE, unsafe_allow_html=True)

    defaults = {"messages": [], "conv_id": "", "knowledge_mode": "auto",
                "llm_model": os.environ.get("PQA_LLM_MODEL", "deepseek/deepseek-v4-flash"),
                "last_payload": None, "queued_question": None}
    for k, v in defaults.items():
        if k not in st.session_state: st.session_state[k] = v

    render_sidebar()

    # Empty state or messages
    if not st.session_state.messages:
        render_empty_state()
    else:
        render_messages()

    # Quick suggestions below empty state
    if not st.session_state.messages:
        cols = st.columns(len(SUGGESTIONS))
        for i, (icon, question, hint) in enumerate(SUGGESTIONS):
            with cols[i]:
                if st.button(f"{icon}\n{hint}", use_container_width=True, key=f"sug_{i}"):
                    st.session_state.queued_question = question
                    st.rerun()

    queued = st.session_state.queued_question

    # Model selector row above input — like ChatGPT
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        models = {"deepseek/deepseek-v4-flash": "DeepSeek V4 Flash", "deepseek/deepseek-v4-pro": "DeepSeek V4 Pro"}
        cur = st.session_state.llm_model
        opts = list(models.keys())
        if cur not in opts: opts.insert(0, cur)
        idx = opts.index(cur)
        st.session_state.llm_model = st.selectbox(
            "", opts, index=idx, format_func=lambda v: models.get(v, v),
            label_visibility="collapsed", key="model_inline",
        )

    question = st.chat_input("输入研究问题…")
    if question:
        st.session_state.queued_question = question
        st.rerun()
    if queued and not question:
        st.session_state.queued_question = None
        handle_question(queued)


if __name__ == "__main__":
    main()
