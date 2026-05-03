# Project TODO

Last updated: 2026-05-03

---

## ✅ Done (since 2026-05-02)

### Routing & Retrieval
- [x] Removed hardcoded domain detection — auto mode always retrieves, no regex gatekeeping
- [x] Removed keyword-based wiki search — pure semantic retrieval
- [x] Removed route classification (`is_status_query`, `decide_knowledge_mode`, template-based answers)
- [x] LLM decides how to respond — no more fixed templates for "状态查询" / "全库概览"
- [x] Budget simplified to single total-char limit (300,000 chars), no group quotas
- [x] Removed retrieval hard limits — PaperQA top_k/doc_top_n raised, budget is the only gate

### UI
- [x] React frontend with ChatGPT-style design (web/)
- [x] FastAPI backend (server.py)
- [x] Conversation history with auto-save (data/conversations/)
- [x] Model selector near input area
- [x] AI avatar color matches route indicator (green=chat, amber=knowledge)
- [x] Source display: renamed groups (概念与方法 / 论文解读 / 原文验证 / 补充线索)
- [x] Source display: wiki items show paper references with Obsidian + PDF links
- [x] Source display: paper_evidence deduplicated against wiki papers
- [x] Source display: PDF links served via API endpoint (no more broken file:// links)
- [x] Paper references resolved from wiki slugs to full titles
- [x] One-click startup script (run-web.cmd)

### Code Quality
- [x] Shared utility module (scripts/_lib.py) — unified load_dotenv, int_env, parse_simple_frontmatter, etc.
- [x] Atomic file writes in wiki_compile.py for paper pages, progress, checkpoints
- [x] 103 unit tests (tests/)
- [x] Fixed: Obsidian URI never worked (env read at module import → lazy read)
- [x] Fixed: int_env(0) silently returned default
- [x] Fixed: stale index blocked incremental import of new PDFs
- [x] Fixed: OSError crash in import-zotero.py content dedup
- [x] Fixed: PaperQA search errors silently swallowed
- [x] Fixed: chunk_texts oversized items now warned
- [x] Fixed: resolve_paper_source_id unresolved now warned
- [x] Fixed: CJK_RE now covers Extension B+ characters
- [x] Fixed: COLLECTION_QUERY_RE over-broad triggering of library overview
- [x] Fixed: infer_question_intent concept check before claim check
- [x] PowerShell scripts: hardcoded Python path → dynamic detection
- [x] .env.example budgets synced with actual Pro run values

---

## 🔲 Next — Engineering

### Wiki Compiler
- [ ] Remove ~300 lines of dead multi-stage pipeline code in wiki_compile.py
- [ ] Add incremental aggregate update mode:
  - compare new paper cards with existing aggregate pages
  - propose add/update/merge/delete patches
  - write patches to `wiki/.staging/aggregate-deltas/<run_id>/`
  - apply only after validation
- [ ] Define update thresholds:
  - small update (1-5 papers): incremental aggregate patch
  - medium (5-30 papers): incremental patch + audit
  - large or new domain: full aggregate rebuild
- [ ] Track which paper pages have been included in current aggregate layer

### Answer Quality
- [ ] Evaluate answer quality on representative Chinese research questions
- [ ] Add deeper aggregate audit: per-paper coverage, contradiction/support density, cross-batch quality
- [ ] Consider citation-aware prompting for "补引用" (add-citation) type tasks

### Conversation Memory
- [ ] Staged conversation-to-wiki workflow
- [ ] Save useful chat insights into `wiki/inbox/` with provenance
- [ ] Review/apply step for conversation-derived updates

### Operations
- [ ] Improve long-run monitoring (progress, ETA, token usage)
- [ ] Improve network resilience (distinguish Wi-Fi down / VPN / API timeout)
- [ ] Record failed papers in persistent retry queue
- [ ] Operator-led database workflow — high-risk actions through chat guidance, not UI buttons
- [ ] Define source intake folders: incoming Zotero, standalone papers, AI conversations, failed docs

---

## 🔲 Next — Content

### Wiki Quality
- [ ] Audit `wiki/concepts/normalized-ucs.md` and `wiki/concepts/self-propping-fractures.md` (flagged as short)
- [ ] Deeper aggregate audit: per-paper coverage, contradiction/support visibility, cross-batch relationships
- [ ] Make batch aggregation high-recall for reusable knowledge units (not paper summaries)
- [ ] Ensure final merge builds cross-batch relationships, contradictions, supports, aliases
- [ ] Keep aggregate output Chinese-first with English terms preserved

### Coverage
- [ ] Increase open-questions coverage (currently only 1 page)
- [ ] Topic-clustering stage before global aggregate pages

---

## 📊 Current State

- PDFs: 513
- PaperQA indexed: 513
- Wiki paper pages: 487 (all Pro-generated)
- Wiki aggregate: concepts 131 / methods 88 / claims 127 / syntheses 16 / open-questions 1
- Wiki semantic index: 10,777 units (embedding-3, 1024d)
- Tests: 103 passing
