# Project State

Last updated: 2026-05-02

This file is the current operational snapshot for the Zotero PaperQA Assistant. It exists so the project can be resumed safely even if chat history changes, an account changes, or a long run is interrupted.

## What Is Complete

- Raw paper store is active under `data/papers/`.
- PaperQA evidence index is active under `data/indexes/papers/`.
- LLM Wiki single-paper layer is complete for the current active journal-paper set:
  - `wiki/papers`: 487 pages
  - all required headings present
  - no stale Fast-generated pages mixed into the current Pro set
  - no skipped-over-budget paper pages remain in the active set
- LLM Wiki aggregate layer is generated:
  - `wiki/concepts`: 131 pages
  - `wiki/methods`: 88 pages
  - `wiki/claims`: 127 pages
  - `wiki/syntheses`: 16 pages
  - `wiki/open-questions`: 1 page
- Aggregate source-link repair is complete:
  - unresolved aggregate source-link targets: 0
- Wiki semantic index is active:
  - `data/indexes/wiki_semantic/index.pkl.zlib`
  - model: `embedding-3`
  - dimensions: 1024
  - indexed units: 10777

## Current Counts And Notes

- Zotero manifest imported PDFs: 538
- Current active `wiki/papers` pages: 487
- Current PaperQA stored docs in `data/indexes/papers/docs`: 508
- Zotero audit snapshot:
  - top-level bibliographic items: 706
  - with PDF attachment: 314
  - without PDF attachment: 392

The `508` indexed-doc count and the `487` active paper-page count are not identical. Treat that as a known discrepancy to audit, not as proof that the active wiki set is broken. The likely causes are duplicate PDFs, historical index residue, or documents intentionally excluded from the current journal-article wiki run.

## Known Warnings

- `wiki/concepts/normalized-ucs.md` is currently flagged as a short aggregate page.
- `wiki/concepts/self-propping-fractures.md` is currently flagged as a short aggregate page.

These are warnings, not build-breaking errors. They should be reviewed before trusting the aggregate layer as final for those topics.

## What Is Not Finished

- Wiki semantic retrieval is active.
- The answer layer now builds a layered local knowledge package:
  - aggregate Wiki structure first
  - Wiki paper pages second
  - PaperQA original evidence third
- Answer planning now asks DeepSeek to use aggregate pages as framework, paper pages as paper-level interpretation, and PaperQA snippets as factual evidence.
- The next risk is answer-quality evaluation, not missing retrieval plumbing.
- Incremental aggregate patching for new papers is not implemented yet.
- Conversation memory ingestion is not implemented yet.
- The operator workflow still needs to be tightened so high-risk maintenance is not casually triggered.

## Recommended Next Work

1. Evaluate answer quality after semantic + layered retrieval on representative Chinese research questions.
2. Add a deeper aggregate audit:
   - per-paper aggregate coverage
   - contradiction/support visibility
   - cross-batch relationship quality
3. After retrieval is stable, design incremental aggregate updates for new papers.

## Safe Routine Operations

- `python scripts/update_paper_database.py --format json`
  - imports new Zotero PDFs only
  - skips existing files
  - skips non-journal items by default
  - deduplicates by content unless explicitly disabled
  - indexes only the newly imported PDFs
- `python scripts/update_wiki_database.py --format json`
  - compiles missing wiki paper pages
  - refreshes the aggregate layer from the current wiki paper set

## High-Risk Operations

- Full vector rebuild
- Full `--force` wiki paper rewrite
- Aggregate-only Pro rewrite
- Any operation that changes completeness-affecting budgets or caps

These should always be preceded by:

1. a dry-run or state check
2. an explicit impact review
3. a resume/checkpoint plan

## Resume Facts

- Single-paper Pro compilation is resumable.
- Aggregate generation now uses batch checkpoints and category-level final merge checkpoints.
- Network interruption can still kill one in-flight API request, but completed checkpoints are retained.
