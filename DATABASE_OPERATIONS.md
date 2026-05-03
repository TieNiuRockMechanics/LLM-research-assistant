# Database Operations

This document defines the intended operating rules for the local research database. It is written for safe day-to-day maintenance, not for one-off experiments.

## Core Rule

The project treats the paper library as one unified database.

- Zotero collections are weak tags for orientation.
- They are not separate knowledge bases.
- The durable knowledge layers are built from content and evidence, not from folder boundaries.

## Allowed Source Type

The standard pipeline currently targets `journalArticle`.

- Books should not enter the normal fast path.
- Theses should not enter the normal fast path.
- Unsupported or bad PDFs should move to `data/papers/_failed-pdf/` for later manual review.

## Standard Safe Workflow

### 1. Update the paper database

Command:

```powershell
python .\scripts\update_paper_database.py --format json
```

What it does:

- scans Zotero
- imports only new PDFs
- skips already known files
- excludes non-journal items by default
- deduplicates by content unless disabled
- indexes only newly imported PDFs

What it does not do:

- it does not repair an already stale index
- it does not rebuild the whole vector layer
- it does not rewrite the LLM Wiki

### 2. Update the LLM Wiki

Command:

```powershell
python .\scripts\update_wiki_database.py --format json
```

What it does:

- compiles missing `wiki/papers` pages
- refreshes aggregate pages from the current paper-page set

What it does not do:

- it does not rebuild PaperQA vectors
- it does not force-rewrite already current paper pages unless asked

## High-Cost Maintenance Workflow

These actions are not routine:

- full vector rebuild
- Pro full-paper rewrite
- Pro aggregate-only rewrite
- changes to merge budgets, caps, or completeness limits

Use them only when one of these is true:

- the active corpus changed in a way incremental logic cannot safely absorb
- the schema changed
- the current generated layer is known to be incomplete or low quality
- a previous build mixed old and new rule sets

## Safety Rules

Before any expensive run:

1. Check current state first.
2. Record expected input count.
3. Record the exact model and budget settings.
4. Confirm whether the run is resumable.
5. Confirm what existing outputs will be reused, replaced, or archived.

Never change completeness-affecting limits casually. If a hard cap can drop content, it must be documented and reviewed before the run.

## Stale Index Rule

If `update_paper_database.py` reports that the index was already stale before the update:

- stop treating normal update as a repair path
- do not assume the new index state is complete
- inspect the cause before rebuilding

Routine incremental update is intentionally conservative. It refuses to silently repair a stale index during a normal update.

## Current Resume Behavior

- Single-paper wiki generation supports resume.
- Aggregate generation uses batch checkpoints and category-level final merge checkpoints.
- A network failure can still kill one active API request.
- Completed checkpoints remain reusable after restart.

## Current Semantic Wiki Index

The LLM Wiki has a separate semantic index under `data/indexes/wiki_semantic/`.

- It is built from Markdown files under `wiki/`.
- It does not modify `wiki/**/*.md`.
- It does not touch the PaperQA/PDF evidence index under `data/indexes/papers/`.
- Query-time answering uses it when available, then falls back to keyword Wiki retrieval if the semantic index or API call is unavailable.

Useful checks:

```powershell
python scripts\wiki_semantic_index.py status
python scripts\wiki_semantic_index.py query --top-k 6 "fracture network connectivity"
```

Rebuild this index after material Wiki edits:

```powershell
python scripts\wiki_semantic_index.py build --dry-run
python scripts\wiki_semantic_index.py build
```

## Planned But Not Yet Standard

These are design targets, not current guaranteed behavior:

- incremental aggregate patching for newly added papers
- conversation Markdown ingestion into `wiki/inbox/`
- operator-led intake of standalone paper folders

Until those are implemented, treat chat-guided maintenance as the preferred control layer for non-routine work.
