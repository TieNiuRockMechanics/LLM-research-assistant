# Zotero PaperQA Research Assistant

A local research assistant for a Zotero PDF library. The project keeps PDFs and PaperQA indexes local, uses DeepSeek V4 for answer synthesis, and keeps embeddings on a separate provider for retrieval.

## Architecture

```text
Zotero PDFs -> data/papers/ -> PaperQA index -> routed Q&A -> optional wiki layer
```

- `data/papers/`: copied PDFs from Zotero.
- `data/indexes/`: generated PaperQA indexes.
- `scripts/pqa-api.py`: stable Python wrapper with model config and question routing.
- `app.py`: Streamlit UI over the wrapper.
- `wiki/`: durable research notes and syntheses. See `WIKI_SCHEMA.md`.
- `ARCHITECTURE.md`: design notes, workflow, and cost controls.
- `PROJECT_STATE.md`: current operational snapshot of the pipeline.
- `DATABASE_OPERATIONS.md`: safe-vs-risky maintenance rules.

## Model Setup

DeepSeek V4 is configured for chat/synthesis:

```env
DEEPSEEK_API_KEY=...
PQA_LLM_MODEL=deepseek/deepseek-v4-flash
PQA_SUMMARY_LLM_MODEL=deepseek/deepseek-v4-flash
PQA_PAPER_MODE=direct
PQA_KNOWLEDGE_MODE=auto
```

The Streamlit sidebar can override the answer/synthesis model per UI session. Available defaults are `deepseek/deepseek-v4-flash` and `deepseek/deepseek-v4-pro`; embeddings remain configured separately.

PaperQA still needs embeddings for indexing and retrieval, so keep a separate embedding provider:

```env
OPENAI_API_KEY=your_zhipu_embedding_key
OPENAI_BASE_URL=https://open.bigmodel.cn/api/paas/v4
PQA_EMBEDDING_MODEL=openai/embedding-3
PQA_EMBEDDING_DIMENSIONS=1024
```

Do not point embeddings at DeepSeek unless DeepSeek provides a compatible embeddings endpoint. The current default example uses ZhipuAI/BigModel embedding-3.

## First Run

```powershell
# Install PaperQA dependencies into .packages
.\scripts\install-paperqa.ps1

# Validate DeepSeek chat
.\scripts\check-deepseek-chat.ps1

# Validate ZhipuAI / BigModel embeddings
.\scripts\check-zhipu-embedding.ps1

# Import a small Zotero sample first, default 10 PDFs
.\scripts\import-zotero-sample.ps1

# Build or refresh the PaperQA index
.\scripts\index-papers.ps1

# Chat with automatic local knowledge augmentation
.\scripts\chat.ps1 -Question "What are the main methodological disagreements in this literature?"
```

## Question Routing

The normal entrypoint is DeepSeek-first chat. Local wiki and paper evidence are added only when the router decides they are relevant, or when you force them.
Knowledge answers use a synthesis step by default: the model first builds an internal evidence plan from Wiki structure and PaperQA snippets, then writes a natural answer from that plan instead of simply replaying retrieved notes.
The Wiki layer now has its own semantic index at `data/indexes/wiki_semantic/`. It embeds Markdown units from `wiki/` with Zhipu `embedding-3` and supplements the older keyword Wiki search. This semantic index is separate from the PaperQA/PDF evidence index and can be rebuilt without touching PDF vectors or existing Wiki Markdown.
For knowledge answers, retrieved context is packaged by role before it reaches DeepSeek:

1. LLM Wiki aggregate pages provide the conceptual and cross-paper framework.
2. LLM Wiki paper pages provide paper-level interpretation and positioning.
3. PaperQA evidence snippets provide the closest available support for factual claims and citations.

The synthesis layer receives that package first and creates an internal evidence plan; the final answer is then written from that plan rather than by replaying Wiki notes.

```powershell
python .\scripts\pqa-api.py chat --format json "你好"
python .\scripts\pqa-api.py chat --knowledge always "这些论文如何定义 fracture network connectivity?"
python .\scripts\pqa-api.py chat --knowledge never "帮我头脑风暴一个引言结构"
```

Semantic Wiki maintenance:

```powershell
python .\scripts\wiki_semantic_index.py status
python .\scripts\wiki_semantic_index.py build --dry-run
python .\scripts\wiki_semantic_index.py build
python .\scripts\wiki_semantic_index.py query --top-k 6 "fracture network connectivity"
```

The PaperQA agent mode remains an internal fallback only. DeepSeek rejects PaperQA's tool-calling `tool_choice` parameter, so the current production path retrieves local evidence directly and sends it to DeepSeek as context.

## Zotero Import

The app is designed around one unified paper database. Zotero collections are imported as metadata tags, not as separate knowledge bases.

Use the UI `更新论文数据库` button to scan Zotero, import new PDFs, and add only newly imported PDFs to the PaperQA evidence index. This path does not compile the LLM Wiki and does not repair/rebuild the whole index.

Use the UI `更新 LLM Wiki` button after the paper database is current. It compiles missing `wiki/papers/` pages and refreshes the aggregate knowledge layer.

For non-routine maintenance, prefer checking `PROJECT_STATE.md` and `DATABASE_OPERATIONS.md` first. The intended long-term operating model is operator-led maintenance with explicit dry-runs for costly actions, not casual rebuilds from the UI.

The same workflows are available from the command line:

```powershell
python .\scripts\update_paper_database.py --scan-only --format json
python .\scripts\update_paper_database.py --format json
python .\scripts\update_wiki_database.py --format json
```

High-cost maintenance actions are intentionally separate: full vector index rebuild, full Wiki Pro rewrite, and aggregate-only Wiki Pro rewrite.

For development, you can still import a small sample first:

```powershell
.\scripts\import-zotero-sample.ps1 -Limit 5
.\scripts\import-zotero-sample.ps1 -Limit 10
```

If Zotero is not in the default `%USERPROFILE%\Zotero` location:

```powershell
.\scripts\import-zotero-sample.ps1 -ZoteroDir "D:\path\to\Zotero" -Limit 10
```

To import one Zotero collection as a tagged subset into the unified PDF folder:

```powershell
python .\scripts\import-zotero.py --collection "雷恩学派分形研究" --paper-directory "data\papers" --manifest-path "data\zotero-import-manifest.json" --skip-existing
python .\scripts\pqa-api.py index --index-name papers --paper-directory "data\papers"
python .\scripts\wiki_compile.py --wiki-dir "wiki" ingest --index-name papers
```

## Local Chat UI

```cmd
run-ui.cmd
```

The script starts Streamlit in the background and opens:

```text
http://localhost:12555
```

The UI has chat, library, and LLM Wiki tabs. The sidebar controls whether local knowledge is used automatically, always, or never. Wiki draft creation is manual: after a useful answer, click `保存最近回答`.

## LLM Wiki Compiler

The LLM Wiki is compiled from the PaperQA index. It is not just saved chat history.

```powershell
python .\scripts\wiki_compile.py init
python .\scripts\wiki_compile.py ingest --limit 5
python .\scripts\wiki_compile.py ingest --force
python .\scripts\wiki_compile.py status
python .\scripts\wiki_compile.py lint
```

The first pass creates durable paper pages under `wiki/papers/`, then aggregates reusable `concepts`, `methods`, `claims`, `syntheses`, and `open-questions`. Generated pages are marked `draft`; use the provenance fields before treating a claim as final.

## Notes

- `.env`, `.packages`, generated indexes, copied PDFs, and Zotero manifests are gitignored.
- The first index build spends embedding tokens; later questions spend mostly LLM tokens plus retrieval overhead.
- The wiki layer is intentionally separate from PaperQA so durable research syntheses do not get mixed with raw evidence retrieval.
- `TODO_LLM_WIKI.md` tracks follow-up engineering tasks; `PROJECT_STATE.md` is the live state snapshot.

