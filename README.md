# PaperQA2 Workspace

This workspace is set up to run `PaperQA2` against a local paper folder while using a cloud LLM API.

## What is ready

- `PaperQA2` is installed into the project-local `.packages` directory
- `scripts/pqa.ps1` loads `.env`, sets the local package path, and runs the CLI
- `scripts/index-papers.ps1` builds or refreshes an index from `data/papers`
- `scripts/ask.ps1` asks questions against the saved index
- `scripts/check-dashscope.ps1` validates DashScope chat and embedding endpoints from `.env`
- `app.py` provides a local Streamlit chat UI for the indexed library
- `run-ui.cmd` starts the local chat UI on `http://localhost:8501`

## Project layout

```text
data/
  papers/      Put PDFs here
  indexes/     Generated PaperQA2 indexes
scripts/
  ask.ps1
  import-zotero.py
  index-papers.ps1
  install-paperqa.ps1
  pqa-api.py
  pqa.ps1
app.py
run-ui.cmd
```

## First run

1. Copy `.env.example` to `.env`
2. Fill in your API settings
3. Put your PDFs into `data/papers`
4. Build the index:

```powershell
.\scripts\index-papers.ps1
```

5. Ask a question:

```powershell
.\scripts\ask.ps1 -Question "What are the main methodological disagreements in this literature?"
```

## Useful commands

```powershell
.\scripts\pqa.ps1 --help
.\\scripts\\check-dashscope.ps1
.\scripts\pqa.ps1 view
.\scripts\index-papers.ps1 -IndexName my-topic
.\scripts\ask.ps1 -IndexName my-topic -Question "Summarize the classic papers in this folder."
.\.venv\Scripts\python.exe .\scripts\import-zotero.py
.\.venv\Scripts\python.exe .\scripts\pqa-api.py index
.\.venv\Scripts\python.exe .\scripts\pqa-api.py ask "What is the shared model across these fracture-network papers?"
```

## Local chat UI

Start the local chat page:

```cmd
run-ui.cmd
```

Then open:

```text
http://localhost:8501
```

The UI talks directly to the existing PaperQA index in `data/indexes/papers`.

## Notes

- PaperQA2 will answer from indexed evidence and attach citations in its own citation-key format.
- The wrapper supports `OpenAI`-style variables and also maps `MOONSHOT_API_KEY` to `OPENAI_API_KEY` for Kimi compatibility.
- If you use Kimi as the chat model, the wrapper will stop early unless you also provide an embedding provider. This is intentional, because PaperQA2 needs embeddings for indexing/retrieval and Kimi's public docs currently document chat/files compatibility rather than a public embeddings setup.
- Later, we can add Zotero synchronization on top of this workspace without changing the retrieval core.
