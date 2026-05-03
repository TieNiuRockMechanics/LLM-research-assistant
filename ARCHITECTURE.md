# Research Knowledge Base Architecture

This project uses a layered design rather than treating every interaction as a raw PDF RAG question.

## Layers

1. Raw sources
   - Zotero PDFs live in `data/papers/`.
   - These files are the source of truth and are not rewritten by the assistant.
   - Zotero collections are imported as metadata tags. They are not separate databases.

2. Evidence engine
   - PaperQA indexes PDFs under `data/indexes/`.
   - It supplies paper text, citations, retrieval, and page-level evidence.

3. LLM Wiki compiler
   - `scripts/wiki_compile.py` compiles indexed papers into durable Markdown pages.
   - It creates `wiki/papers/` first, then derives concepts, methods, claims, syntheses, and open questions.
   - Generated pages are `draft` until reviewed.

4. Question router
   - `scripts/pqa-api.py chat --knowledge auto` is the default.
   - Ordinary chat goes directly to DeepSeek.
   - Research/library questions search the LLM Wiki first and then PaperQA evidence when needed.
   - Knowledge answers use a synthesis layer: Wiki gives structure, PaperQA gives evidence, and DeepSeek builds an internal answer plan before writing the final response.

5. Model providers
   - DeepSeek V4 Flash is the default for chat, synthesis, and wiki compilation; the UI can switch to DeepSeek V4 Pro for stronger responses.
   - Embeddings stay on a separate OpenAI-compatible provider; the current setup uses ZhipuAI/BigModel `embedding-3`.

## Recommended Workflow

```powershell
.\scripts\install-paperqa.ps1
.\scripts\import-zotero-sample.ps1 -Limit 5
.\scripts\index-papers.ps1
python .\scripts\wiki_compile.py ingest --limit 5
run-ui.cmd
```

For normal use after Zotero changes:

```powershell
python .\scripts\update_paper_database.py --format json
python .\scripts\update_wiki_database.py --format json
```

## Cost Controls

- Import 5-10 papers for development before scaling up.
- Normal paper database updates stage only newly imported PDFs and add them with `--no-sync`, so they do not repair or rebuild the full index.
- Rebuild the full PaperQA index only from Advanced Maintenance.
- Re-run `wiki_compile.py ingest --force` only from Advanced Maintenance when intentionally rewriting Wiki paper pages.
- Use the LLM Wiki for repeated background knowledge so normal questions need fewer raw PDF chunks.
