# LLM Wiki Follow-up Tasks

This file tracks pending work for the Zotero PaperQA Assistant LLM Wiki pipeline.

## Current Run

- [x] Finish DeepSeek V4 Pro single-paper page rewrite for all active journal articles.
- [x] Repair incomplete paper pages and the long review paper that previously exceeded the single-pass budget.
- [x] After completion, audit `wiki/papers/` before starting aggregate generation:
  - [x] Empty or near-empty pages.
  - [x] Missing required headings.
  - [x] Non-v4 or stale pages.
  - [x] `Source Coverage` presence and full-index metadata.
  - [x] Citation/provenance label format:
    - [x] normalize labels to `[Author Year, pp. x-y]`.
    - [x] replace full-width brackets, citation-only parentheses, non-ASCII page-range dashes, and `pp.x` forms.
    - [x] report ambiguous page-only labels that cannot safely infer author/year.
  - [x] Page length distribution.
  - [x] Chinese/English/mixed language distribution.
  - [x] Failed or skipped records in `wiki/.staging`.
  - [x] Add citation-format generation rules and a reusable normalization lint/script before aggregate generation.
- [x] Pre-aggregate paper-page status on 2026-05-02:
  - `wiki/papers`: 487 pages.
  - missing required headings: 0.
  - non-Pro or stale pages: 0.
  - skipped over budget: 0.
  - failed: 0.
  - shortest page: 3,778 chars; median: 8,097 chars; p95: 18,224 chars; max: 22,892 chars.
  - citation normalization dry-run after cleanup: 0 files changed.

## Aggregate Layer

- [x] Set aggregate budgets from real paper-page statistics instead of fixed guesses.
- [x] Reassess these defaults before Pro aggregate generation:
  - `LLM_WIKI_AGGREGATE_CARD_CHAR_BUDGET = 70000`
  - `LLM_WIKI_AGGREGATE_BATCH_CHAR_BUDGET = 700000`
  - `LLM_WIKI_AGGREGATE_MERGE_CHAR_BUDGET = 700000`
  - `LLM_WIKI_AGGREGATE_TIMEOUT = 1800`
  - `LLM_WIKI_AGGREGATE_MAX_MERGE_ROUNDS = 6`
- [x] Increase aggregate item caps so the knowledge layer is not compressed into too few items:
  - `LLM_WIKI_MAX_CONCEPTS = 160`
  - `LLM_WIKI_MAX_METHODS = 160`
  - `LLM_WIKI_MAX_CLAIMS = 320`
  - `LLM_WIKI_MAX_SYNTHESES = 120`
  - `LLM_WIKI_MAX_OPEN_QUESTIONS = 90`
  - batch-level max item caps raised in `scripts/run_pro_aggregate.ps1`.
- [ ] Make batch aggregation high-recall for reusable knowledge units, not paper summaries.
- [ ] Ensure final merge builds cross-batch relationships, contradictions, supports, aliases, and source links.
- [ ] Keep aggregate output Chinese-first, with English terms, abbreviations, variables, and aliases preserved.
- [ ] Consider adding a topic-clustering stage before global aggregate pages:
  - global map
  - topic pages
  - concepts
  - methods
  - claims
  - syntheses
  - open questions
- [x] Keep aggregate checkpoints and refuse silent truncation when merge does not converge.
- [x] Run Pro aggregate generation.
- [ ] Audit generated aggregate layer before retrieval/answering changes.
  - [x] Basic post-run integrity check:
    - aggregate pages written successfully
    - category final merges completed
    - source-link repair applied
    - no missing aggregate source-link targets remain
  - [ ] Deeper content audit still pending:
    - per-paper aggregate coverage
    - contradiction/support density
    - short-page semantic adequacy
    - cross-batch relationship quality

## Incremental Updates

- [ ] Split future updates into clear stages:
  - update vector index for new PDFs only
  - generate single-paper pages for new papers only
  - generate new paper cards
  - update aggregate layer
- [ ] Add an aggregate incremental update mode:
  - compare new paper cards with existing aggregate pages
  - propose add/update/merge/delete patches
  - write patches to `wiki/.staging/aggregate-deltas/<run_id>/`
  - apply only after validation.
- [ ] Define thresholds:
  - small update: incremental aggregate patch
  - medium update: incremental patch plus audit
  - large update or new domain: full aggregate rebuild
- [ ] Track which paper pages have already been included in the current aggregate layer.
- [ ] Design a safer operator-led database workflow:
  - avoid exposing high-risk database/vector/wiki rebuild actions as ordinary front-end buttons.
  - let the user describe the update goal in chat, then inspect inputs, dry-run, report impact, and execute only the needed stage.
  - keep destructive or high-token operations out of casual UI actions.
- [x] Write a database operation guide for routine maintenance:
  - what counts as a standard journal-paper import.
  - what happens when Zotero receives new PDFs.
  - how to import a standalone folder of papers.
  - how to import a folder of AI conversation Markdown files.
  - when vector indexing is needed.
  - when single-paper Wiki pages are needed.
  - when aggregate Wiki updates are needed.
  - expected costs, risks, and rollback/resume behavior.
- [ ] Define future source intake folders after the knowledge base stabilizes:
  - incoming Zotero PDFs.
  - standalone paper folders.
  - AI conversation Markdown folders.
  - failed/unsupported documents.
  - manual-review queue.

## Retrieval And Answering

- [x] Build a Wiki semantic index after aggregate pages exist.
- [x] Index separate Wiki layers with metadata:
  - aggregate pages
  - paper pages
  - claims
  - methods
  - concepts
  - syntheses
  - open questions
- [ ] Add Chinese/English query rewriting for retrieval.
- [x] Supplement keyword Wiki search with semantic retrieval.
- [x] Retrieve in layers:
  - aggregate structure first
  - paper pages second
  - PaperQA original evidence third
- [x] Add answer planning so DeepSeek uses Wiki as structure and PaperQA chunks as evidence.
- [ ] Evaluate answer quality after semantic + layered retrieval on representative Chinese research questions.
- [ ] Keep source display grouped by role:
  - LLM Wiki aggregate structure
  - LLM Wiki paper page
  - PaperQA original evidence
  - other Wiki leads
- [ ] Improve citations to readable labels such as `[Wang 2018, pp. 5-7]`, and keep these labels parseable for source grouping and Obsidian links.

## Quality Gates

- [ ] Before each expensive Pro run, do a dry-run and inspect:
  - input record count
  - included/excluded item types
  - expected output paths
  - resume/force behavior
  - completeness-affecting budgets and caps.
- [x] Before aggregate generation, produce an audit report and require it to pass:
  - no near-empty paper pages
  - required headings present
  - no stale Fast-generated pages mixed into the Pro set
  - citation labels normalized or explicitly reported
  - oversized/failed/skipped records accounted for.
- [ ] After aggregate generation, audit:
  - item counts by layer
  - source coverage by paper
  - unresolved conflicts
  - merge-round convergence
  - truncation/refusal logs.
- [ ] Keep every irreversible or high-token operation resumable and checkpointed.
- [ ] Never silently truncate source material in a completeness-critical stage; fail with a report instead.

## Conversation Memory

- [ ] Add a staged conversation-to-wiki workflow.
- [ ] Save useful chat insights into `wiki/inbox/` with provenance and status.
- [ ] Do not merge chat answers into durable Wiki pages without evidence.
- [ ] Add a review/apply step for conversation-derived updates.

## Operations

- [ ] Improve long-run monitoring:
  - current paper
  - completed/skipped/failed/remaining
  - ETA
  - latest API error
  - token usage when available
- [ ] Improve network resilience:
  - distinguish Wi-Fi down, VPN/proxy refused, API timeout, incomplete read.
  - consider API health checks in addition to ping checks.
- [ ] Add safer resume behavior after transient API failures.
- [ ] Record failed papers in a persistent retry queue.
- [ ] Avoid broad or unexplained hard-coded limits; document every limit that affects completeness.

## Current State Snapshot

- [x] Active evidence corpus is built and usable.
- [x] `wiki/papers/`: 487 Pro-generated single-paper pages.
- [x] Aggregate layer generated:
  - `concepts`: 131
  - `methods`: 88
  - `claims`: 127
  - `syntheses`: 16
  - `open-questions`: 1
- [x] Aggregate source-link repair completed; unresolved link targets: 0.
- [x] Current aggregate warnings are limited to:
  - `wiki/concepts/normalized-ucs.md`
  - `wiki/concepts/self-propping-fractures.md`
- [ ] Retrieval/answering layer is still the main unfinished product area.
- [ ] Operator workflow docs and state snapshot need to stay synced with real runs.
