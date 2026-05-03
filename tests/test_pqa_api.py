"""Tests for pqa-api.py pure functions — no I/O, no network, no subprocess."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(_SCRIPTS))

_spec = importlib.util.spec_from_file_location("pqa_api", _SCRIPTS / "pqa-api.py")
pqa_api = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(pqa_api)


class TestInferQuestionIntent:
    def test_overview_is_default(self):
        assert pqa_api.infer_question_intent("你好") == "overview"

    def test_comparison(self):
        assert pqa_api.infer_question_intent("比较DFN和continuum方法") == "comparison"
        assert pqa_api.infer_question_intent("compare method A versus method B") == "comparison"

    def test_method(self):
        assert pqa_api.infer_question_intent("如何表征裂缝网络") == "method"
        assert pqa_api.infer_question_intent("what is the workflow for") == "method"

    def test_concept(self):
        assert pqa_api.infer_question_intent("permeability是什么概念") == "concept"
        assert pqa_api.infer_question_intent("如何理解fractal dimension") == "concept"

    def test_claim(self):
        assert pqa_api.infer_question_intent("这些论文的结论是什么") == "claim"
        assert pqa_api.infer_question_intent("裂缝网络如何影响渗透率") == "claim"
        assert pqa_api.infer_question_intent("what is the effect of stress on permeability") == "claim"

    def test_open_question(self):
        assert pqa_api.infer_question_intent("这个领域的开放问题有哪些") == "open_question"
        assert pqa_api.infer_question_intent("research gaps in fracture modeling") == "open_question"


class TestBuildQueryPackage:
    def test_basic_package(self):
        pkg = pqa_api.build_query_package("fracture connectivity是什么", "fracture connectivity definition")
        assert pkg["question"] == "fracture connectivity是什么"
        assert pkg["english_query"] == "fracture connectivity definition"
        assert len(pkg["variants"]) >= 1
        assert len(pkg["terms"]) > 0
        assert "intent" in pkg
        assert "preferred_folders" in pkg
        assert "paper_search_query" in pkg

    def test_empty_english_query(self):
        pkg = pqa_api.build_query_package("你好", "")
        assert pkg["english_query"] == ""
        assert len(pkg["variants"]) >= 1


class TestResultIdentityKey:
    def test_semantic_with_heading(self):
        item = {"path": "/wiki/concepts/test.md", "heading": "Definition", "retrieval_method": "semantic"}
        key = pqa_api.result_identity_key(item)
        assert "test.md::Definition" in key

    def test_keyword_without_heading(self):
        item = {"path": "/wiki/papers/test.md", "retrieval_method": "keyword"}
        key = pqa_api.result_identity_key(item)
        assert key == "/wiki/papers/test.md"

    def test_no_path_falls_back_to_label(self):
        item = {"label": "unique-label", "retrieval_method": "semantic"}
        key = pqa_api.result_identity_key(item)
        assert key == "unique-label"


class TestMergeRankedResults:
    def test_deduplication(self):
        group1 = [{"path": "a.md", "score": 10}, {"path": "b.md", "score": 8}]
        group2 = [{"path": "a.md", "score": 5}, {"path": "c.md", "score": 7}]
        result = pqa_api.merge_ranked_results(group1, group2)
        paths = [r["path"] for r in result]
        assert paths == ["a.md", "b.md", "c.md"]

    def test_limit(self):
        group1 = [{"path": f"{i}.md", "score": 10 - i} for i in range(5)]
        group2 = [{"path": f"{i + 10}.md", "score": 5 - i} for i in range(5)]
        result = pqa_api.merge_ranked_results(group1, group2, limit=3)
        assert len(result) == 3

    def test_empty_groups(self):
        assert pqa_api.merge_ranked_results() == []
        assert pqa_api.merge_ranked_results([], []) == []
        assert len(pqa_api.merge_ranked_results([{"path": "a.md"}])) == 1


class TestContextRoleInfo:
    def test_known_types(self):
        assert pqa_api.context_role_info("wiki_aggregate")["group"] == "wiki_aggregate"
        assert pqa_api.context_role_info("wiki_paper_page")["group"] == "wiki_paper_page"
        assert pqa_api.context_role_info("paper")["group"] == "paper_evidence"
        assert pqa_api.context_role_info("wiki")["group"] == "wiki_other"

    def test_unknown_falls_back_to_wiki(self):
        assert pqa_api.context_role_info(None)["group"] == "wiki_other"
        assert pqa_api.context_role_info("")["group"] == "wiki_other"
        assert pqa_api.context_role_info("unknown_type")["group"] == "wiki_other"


class TestBudgetContexts:
    def test_empty_returns_empty(self):
        selected, meta = pqa_api.budget_contexts([])
        assert selected == []
        assert meta["selected_chars"] == 0

    def test_basic_budgeting(self):
        contexts = [
            {"label": "test", "text": "short text", "source_type": "wiki_aggregate", "score": 10},
        ]
        selected, meta = pqa_api.budget_contexts(contexts)
        assert len(selected) == 1
        assert selected[0]["label"] == "test"
        assert meta["selected_chars"] > 0


class TestCleanExcerpt:
    def test_short_text_unchanged(self):
        result = pqa_api.clean_excerpt("hello world", max_chars=100)
        assert result == "hello world"

    def test_long_text_truncated(self):
        long_text = "word " * 200
        result = pqa_api.clean_excerpt(long_text, max_chars=100)
        assert len(result) <= 103  # 100 + "..."
        assert result.endswith("...")


class TestStripFrontmatter:
    def test_removes_frontmatter(self):
        content = "---\ntitle: test\n---\n\n# Heading\nBody text"
        result = pqa_api.strip_frontmatter(content)
        assert "# Heading" in result
        assert "title:" not in result

    def test_no_frontmatter_unchanged(self):
        content = "# Just a heading\nBody text"
        result = pqa_api.strip_frontmatter(content)
        assert result == content


class TestParseSimpleFrontmatter:
    def test_scalar_fields(self):
        content = "---\ntitle: My Paper\nstatus: draft\n---\n\n# Body"
        fields = pqa_api.parse_simple_frontmatter(content)
        assert fields["title"] == "My Paper"
        assert fields["status"] == "draft"

    def test_list_fields(self):
        content = "---\naliases:\n  - alias1\n  - alias2\n---\n\n# Body"
        fields = pqa_api.parse_simple_frontmatter(content)
        assert isinstance(fields["aliases"], list)
        assert fields["aliases"] == ["alias1", "alias2"]

    def test_no_frontmatter(self):
        assert pqa_api.parse_simple_frontmatter("# No frontmatter") == {}


class TestMergeUsage:
    def test_merges_token_counts(self):
        a = {"prompt_tokens": 100, "completion_tokens": 50, "total_tokens": 150}
        b = {"prompt_tokens": 200, "completion_tokens": 80, "total_tokens": 280}
        result = pqa_api.merge_usage(a, b)
        assert result["prompt_tokens"] == 300
        assert result["completion_tokens"] == 130
        assert result["total_tokens"] == 430

    def test_handles_empty(self):
        assert pqa_api.merge_usage() == {}
        assert pqa_api.merge_usage({}, {}) == {}


class TestContainsCjk:
    def test_chinese_returns_true(self):
        assert pqa_api.contains_cjk("裂缝网络连通性") is True
        assert pqa_api.contains_cjk("hello 世界") is True

    def test_english_returns_false(self):
        assert pqa_api.contains_cjk("fracture network connectivity") is False
        assert pqa_api.contains_cjk("") is False


class TestWikiTerms:
    def test_english_terms(self):
        terms = pqa_api.wiki_terms("fracture network connectivity")
        assert "fracture" in terms
        assert "network" in terms
        assert "connectivity" in terms

    def test_chinese_bigrams(self):
        terms = pqa_api.wiki_terms("裂缝网络")
        cjk_terms = {t for t in terms if any("一" <= c <= "鿿" for c in t)}
        assert len(cjk_terms) > 0

    def test_short_terms_filtered(self):
        terms = pqa_api.wiki_terms("a b c")
        assert "a" not in terms  # too short
