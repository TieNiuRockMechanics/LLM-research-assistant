# Zotero PaperQA Research Assistant

## Permission Rules

在执行任何 shell 命令、文件修改、联网请求、安装、删除、移动、后台任务或权限提升操作之前，必须先用中文简要说明：
1. 你要做什么
2. 为什么需要做
3. 会影响哪些文件或目录
4. 有没有风险（删除、覆盖、联网、长时间运行、后台运行）

说明不完整则不发起权限请求。不要擅自开始长时间运行或不可逆操作。

**长任务规则**：预计运行超过 5 分钟的命令（如 PaperQA 索引、Wiki 编译），不要通过后台任务执行——后台任务管理器会截断。把命令原文发给用户，让用户在本地终端（PowerShell）中自己输入运行。

## Where We Are

A local research assistant over a Zotero PDF library (513 papers, geoscience/rock mechanics).

## How To Start

```powershell
cd "F:\shuixin code\zotero-paperqa-assistant"
# Option A: Double-click run-web.cmd
# Option B: Two terminals
python server.py              # Backend on :12556
cd web && npm run dev         # Frontend on :5173
```
Then open **http://localhost:5173**

## Architecture (current state after 2026-05-03 refactor)

- **Backend**: FastAPI (`server.py`) wraps `scripts/pqa-api.py` (PaperQA + DeepSeek V4 + Zhipu embedding-3)
- **Frontend**: React (Vite + Tailwind) in `web/`
- **Retrieval**: Pure semantic (no keyword), budget-only constraint (300K chars)
- **Routing**: Removed all regex-based classification. Auto mode always retrieves; LLM decides response type. No more templates for status/overview queries.
- **Wiki**: 487 paper pages + 363 aggregate (concepts 131, methods 88, claims 127, syntheses 16, open-questions 1)
- **Semantic index**: 10,777 units, embedding-3 1024d, `data/indexes/wiki_semantic/`
- **Conversations**: data/conversations/ (auto-saved chat history)
- **Tests**: 103 passing (`tests/`)

## Key Files

| File | Purpose |
|------|---------|
| `server.py` | FastAPI backend, REST endpoints |
| `scripts/pqa-api.py` | Core: retrieval, budgeting, answer synthesis |
| `scripts/wiki_compile.py` | Wiki compiler (paper pages + aggregate) |
| `scripts/wiki_semantic_index.py` | Semantic index builder |
| `scripts/_lib.py` | Shared utilities |
| `web/src/App.jsx` | React app entry |
| `web/src/components/ChatArea.jsx` | Chat UI |
| `web/src/components/Message.jsx` | Message + source display |
| `web/src/components/Sidebar.jsx` | Conversation history sidebar |
| `web/src/App.jsx` | Main layout |

## Important Design Decisions

- **No more regex routing** — LLM decides how to respond, not keyword matching
- **Source display groups**: 概念与方法 / 论文解读 / 原文验证 / 补充线索
- **PDF links** served through `/api/pdfs/` endpoint (not file://)
- **Obsidian URI** works if OBSIDIAN_VAULT_NAME set in .env
- **Budget system** simplified: single 300K char ceiling, no per-group quotas
- **Atomic file writes** in wiki_compile for paper pages, progress, checkpoints

## What's Left (from TODO_LLM_WIKI.md)

- Incremental aggregate updates (new papers don't auto-enter aggregate layer)
- wiki_compile.py dead code removal (~300 lines)
- Open-questions expansion (only 1 page)
- Conversation memory ingestion (AI对话引入知识库 — attempted, rolled back, needs redesign)
- Long-run monitoring improvements

## Git

- Remote: https://github.com/TieNiuRockMechanics/LLM-research-assistant.git
- Latest commit: `5a4c738` Routing refactor
