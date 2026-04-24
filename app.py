from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parent
PAPERS_DIR = PROJECT_ROOT / "data" / "papers"
INDEX_DIR = PROJECT_ROOT / "data" / "indexes" / "papers"
MANIFEST_PATH = PROJECT_ROOT / "data" / "zotero-import-manifest.json"
API_SCRIPT = PROJECT_ROOT / "scripts" / "pqa-api.py"


def configure_page() -> None:
    st.set_page_config(
        page_title="Zotero PaperQA",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.markdown(
        """
        <style>
        .stApp {
            background:
                radial-gradient(circle at top left, rgba(191, 222, 255, 0.45), transparent 32%),
                radial-gradient(circle at top right, rgba(241, 217, 181, 0.35), transparent 28%),
                linear-gradient(180deg, #f6f3ee 0%, #efe8df 100%);
            color: #18222d;
        }
        h1, h2, h3 {
            font-family: "Palatino Linotype", "Book Antiqua", Georgia, serif;
            letter-spacing: 0.02em;
        }
        .block-container {
            max-width: 1180px;
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .hero-card {
            background: rgba(255, 252, 247, 0.82);
            border: 1px solid rgba(125, 97, 71, 0.14);
            border-radius: 22px;
            padding: 1.25rem 1.4rem;
            box-shadow: 0 18px 40px rgba(78, 59, 42, 0.08);
            margin-bottom: 1rem;
        }
        .metric-card {
            background: rgba(255, 255, 255, 0.72);
            border: 1px solid rgba(24, 34, 45, 0.08);
            border-radius: 18px;
            padding: 0.9rem 1rem;
            margin-bottom: 0.75rem;
        }
        .caption-chip {
            display: inline-block;
            padding: 0.2rem 0.55rem;
            border-radius: 999px;
            background: #1f4b73;
            color: white;
            font-size: 0.8rem;
            margin-right: 0.4rem;
        }
        .stChatMessage {
            background: rgba(255, 255, 255, 0.62);
            border: 1px solid rgba(24, 34, 45, 0.06);
            border-radius: 18px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def ensure_state() -> None:
    if "messages" not in st.session_state:
        st.session_state.messages = []


def paper_files() -> list[Path]:
    return sorted(path for path in PAPERS_DIR.glob("*.pdf"))


def import_manifest() -> dict | None:
    if not MANIFEST_PATH.exists():
        return None
    try:
        return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None


def build_env() -> dict[str, str]:
    env = os.environ.copy()
    packages_path = str(PROJECT_ROOT / ".packages")
    existing_pythonpath = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = packages_path if not existing_pythonpath else packages_path + os.pathsep + existing_pythonpath
    env["PYTHONUTF8"] = "1"
    return env


def run_pqa(command: list[str], timeout_seconds: int = 600) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(API_SCRIPT), "--quiet", *command],
        cwd=PROJECT_ROOT,
        env=build_env(),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout_seconds,
        check=False,
    )


def ask_pqa(question: str) -> dict:
    result = run_pqa(["ask", "--format", "json", question])
    if result.returncode != 0:
        detail = (result.stderr or result.stdout or "").strip()
        raise RuntimeError(detail or "PaperQA ask failed.")
    return json.loads(result.stdout.strip())


def rebuild_index() -> str:
    result = run_pqa(["index"], timeout_seconds=900)
    if result.returncode != 0:
        detail = (result.stderr or result.stdout or "").strip()
        raise RuntimeError(detail or "PaperQA index build failed.")
    return result.stdout.strip()


def render_sidebar() -> None:
    manifest = import_manifest()
    papers = paper_files()

    with st.sidebar:
        st.markdown("## Library")
        st.markdown(
            """
            <div class="metric-card">
              <div class="caption-chip">PaperQA</div>
              <div class="caption-chip">Zotero</div>
              <p style="margin-top:0.8rem;">这个界面直接复用你已经建好的本地知识库，不会另外再做一套 RAG。</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.metric("已导入 PDF", len(papers))
        st.metric("索引状态", "已建立" if INDEX_DIR.exists() else "未建立")
        if manifest:
            st.caption(f"最近导入条目数: {manifest.get('imported_count', 0)}")

        if st.button("重建索引", use_container_width=True):
            with st.spinner("正在重建索引，可能需要半分钟到几分钟..."):
                try:
                    message = rebuild_index()
                except Exception as exc:
                    st.error(str(exc))
                else:
                    st.success(message or "索引重建完成。")

        st.markdown("### 当前论文")
        for path in papers:
            st.markdown(f"- {path.stem}")

        st.markdown("### 可直接问")
        st.markdown("- 这组论文的核心争议是什么？")
        st.markdown("- 这些论文如何解释 fracture network connectivity？")
        st.markdown("- 2010 和 2013 两篇论文的方法论差别是什么？")


def render_header() -> None:
    st.markdown(
        """
        <div class="hero-card">
          <h1 style="margin-bottom:0.3rem;">Zotero PaperQA Chat</h1>
          <p style="font-size:1.02rem; margin-bottom:0;">
            这里就是你和知识库对话的地方。问题会直接送到已经建好的
            <code>data/indexes/papers</code>，回答基于当前导入的论文证据生成。
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_messages() -> None:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if message.get("references"):
                with st.expander("查看引用"):
                    st.markdown(message["references"])


def main() -> None:
    configure_page()
    ensure_state()
    render_sidebar()
    render_header()
    render_messages()

    question = st.chat_input("输入一个关于你文献库的问题")
    if not question:
        return

    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("正在检索论文并生成回答..."):
            try:
                payload = ask_pqa(question)
            except Exception as exc:
                error_message = f"问答失败：{exc}"
                st.error(error_message)
                st.session_state.messages.append(
                    {"role": "assistant", "content": error_message}
                )
                return

        answer = payload.get("answer", "").strip() or "这次没有返回可用答案。"
        references = payload.get("references", "").strip()
        st.markdown(answer)
        if references:
            with st.expander("查看引用"):
                st.markdown(references)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer, "references": references}
    )


if __name__ == "__main__":
    main()
