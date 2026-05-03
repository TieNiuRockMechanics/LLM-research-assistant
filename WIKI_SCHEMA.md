# LLM Wiki Schema

The wiki layer is a durable, LLM-maintained research knowledge base compiled from the PaperQA evidence engine. Raw PDFs remain the source of truth; Markdown pages are the editable knowledge layer.

## Directories

```text
wiki/
  index.md
  log.md
  papers/
  concepts/
  methods/
  claims/
  syntheses/
  open-questions/
  inbox/
```

## Compiler

```powershell
python .\scripts\wiki_compile.py init
python .\scripts\wiki_compile.py ingest --limit 5
python .\scripts\wiki_compile.py ingest --force
python .\scripts\wiki_compile.py status
python .\scripts\wiki_compile.py lint
```

- `papers/`: one durable note per indexed paper.
- `concepts/`: reusable research concepts extracted from paper pages.
- `methods/`: named methods and workflows.
- `claims/`: concrete scientific claims with provenance.
- `syntheses/`: cross-paper summaries.
- `open-questions/`: unresolved questions and possible research directions.
- `inbox/`: manually saved chat answers that have not been curated yet.

Zotero collection names may appear in paper page front matter as `collections`. They are weak tags used for orientation only; the LLM Wiki should organize knowledge by content, evidence, concepts, methods, and claims.

## Paper Pages

Each `wiki/papers/*.md` page is a structured evidence note, not just a summary. The compiler asks for these sections:

- `One-line Summary`
- `Research Question`
- `Study Area / Data`
- `Methods`
- `Key Findings`
- `Core Evidence Table`
- `Limitations`
- `Assumptions / Conditions`
- `Key Variables / Parameters`
- `Reusable Claims`
- `Candidate Concepts`
- `Candidate Methods`
- `Connections To Other Work`
- `Open Questions`
- `Source Coverage`

The `Core Evidence Table` should map evidence to source labels and conditions. `Source Coverage` should state whether the indexed chunks are enough to support the note.

## Aggregate Pages

Aggregate pages are compiled from structured cards extracted from paper pages. The compiler should avoid raw fixed-prefix truncation; use these configurable budgets instead:

```text
LLM_WIKI_AGGREGATE_CARD_CHAR_BUDGET=70000
LLM_WIKI_AGGREGATE_BATCH_CHAR_BUDGET=700000
LLM_WIKI_AGGREGATE_MERGE_CHAR_BUDGET=700000
```

If the library is large, aggregation runs in batches and then performs a final merge/deduplication pass.

Aggregate rewrites are staged before they replace the active Wiki pages. Existing aggregate pages are moved to:

```text
wiki/.archive/aggregates/<timestamp>/
```

This prevents stale concept/method/claim/synthesis pages from remaining active after a rewrite, while keeping a recoverable copy.

Forced paper rewrites are resumable. Current-schema paper pages are skipped when `--force --resume` is used, so an interrupted run can be restarted without paying again for pages already completed.

- `concepts/`: definition, aliases, boundary, related methods, related claims, sources.
- `methods/`: purpose, workflow, inputs, outputs, assumptions, strengths, limitations, related concepts, sources.
- `claims/`: claim, evidence, condition, limitation, confidence, status, supports, contradicts, sources.
- `syntheses/`: central question, synthesis, evidence chain, disagreements, boundary conditions, writing uses, sources.
- `open-questions/`: why it matters, current evidence, needed evidence, sources.

## Required Provenance

Non-trivial claims should carry provenance:

```yaml
claim: "A concrete scientific claim, not a vague summary."
sources:
  - paper_id: "year-author-short-title"
    locator: "page/section if available"
confidence: low|medium|high
status: provisional|supported|contested|deprecated
last_checked: YYYY-MM-DD
```

## Rules

- Keep raw PDFs as the source of truth.
- Use PaperQA to verify claims before writing synthesis pages.
- Mark disagreements explicitly instead of smoothing them into one answer.
- Prefer short, linked pages over one large summary document.
- Treat generated pages as `draft` until reviewed.
- Do not move chat answers from `inbox/` into the durable wiki without provenance.
