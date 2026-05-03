"""Tests for wiki_compile.py pure functions — no I/O, no LLM calls."""

from __future__ import annotations

import importlib.util
import os
import sys
import tempfile
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(_SCRIPTS))

# wiki_compile does module-level work (loads pqa_api, reads env, etc.)
# Keep side-effects contained by setting required env vars temporarily.
os.environ.setdefault("PQA_LLM_MODEL", "deepseek/deepseek-v4-flash")
os.environ.setdefault("DEEPSEEK_API_KEY", "test-key")

_spec = importlib.util.spec_from_file_location("wiki_compile", _SCRIPTS / "wiki_compile.py")
wiki_compile = importlib.util.module_from_spec(_spec)
sys.modules["wiki_compile"] = wiki_compile
_spec.loader.exec_module(wiki_compile)


def _temp_md_file(content: str, name: str = "test.md") -> Path:
    """Create a temporary markdown file for tests that need one."""
    tmp = Path(tempfile.mkdtemp()) / name
    tmp.parent.mkdir(parents=True, exist_ok=True)
    tmp.write_text(content, encoding="utf-8")
    return tmp


class TestCleanFilename:
    def test_ascii_title(self):
        result = wiki_compile.clean_filename("Validity of Cubic Law for Fluid Flow")
        assert result == "Validity of Cubic Law for Fluid Flow"

    def test_removes_invalid_chars(self):
        result = wiki_compile.clean_filename('Test: "hello" / world?')
        # : " / ? removed, replaced with spaces then collapsed
        assert ":" not in result
        assert '"' not in result
        assert "/" not in result
        assert "?" not in result

    def test_collapses_spaces(self):
        result = wiki_compile.clean_filename("hello    world")
        assert result == "hello world"

    def test_trims_dots_and_spaces(self):
        result = wiki_compile.clean_filename("  .hello.  ")
        assert result == "hello"

    def test_empty_becomes_untitled(self):
        result = wiki_compile.clean_filename("...")
        assert result == "untitled"


class TestCleanText:
    def test_collapses_whitespace(self):
        result = wiki_compile.clean_text("hello    world\n\n\ntest")
        assert result == "hello world test"

    def test_truncates(self):
        result = wiki_compile.clean_text("a" * 200, max_chars=50)
        assert len(result) <= 53  # 50 + "..."
        assert result.endswith("...")

    def test_no_truncation_when_under_limit(self):
        result = wiki_compile.clean_text("short", max_chars=100)
        assert result == "short"


class TestCleanMarkdownExcerpt:
    def test_removes_repeated_newlines(self):
        result = wiki_compile.clean_markdown_excerpt("para1\n\n\n\npara2")
        assert "\n\n\n\n" not in result

    def test_truncates_at_newline_boundary(self):
        result = wiki_compile.clean_markdown_excerpt("line one\nline two\nline three", max_chars=15)
        lines = result.split("\n")
        assert len(lines) <= 3


class TestChunkTexts:
    def test_empty_input(self):
        assert wiki_compile.chunk_texts([], max_chars=100) == []

    def test_single_item_fits(self):
        batches = wiki_compile.chunk_texts(["hello"], max_chars=100)
        assert len(batches) == 1
        assert batches[0] == ["hello"]

    def test_multiple_items_in_one_batch(self):
        items = ["a" * 10, "b" * 10, "c" * 10]
        batches = wiki_compile.chunk_texts(items, max_chars=1000)
        assert len(batches) == 1
        assert len(batches[0]) == 3

    def test_splits_when_budget_exceeded(self):
        items = ["x" * 50, "y" * 50, "z" * 50]
        batches = wiki_compile.chunk_texts(items, max_chars=80)
        assert len(batches) >= 2

    def test_single_oversized_item_gets_own_batch(self):
        items = ["x" * 200, "short"]
        batches = wiki_compile.chunk_texts(items, max_chars=50)
        assert len(batches) == 2
        assert batches[0] == ["x" * 200]


class TestPaperPageComplete:
    def test_returns_true_for_full_index(self):
        sections = "\n".join(
            f"## {h}\nTest content for {h}.\n"
            for h in wiki_compile.PAPER_REQUIRED_SECTIONS
        )
        tmp = _temp_md_file(
            "---\nschema_version: paper-v4-2026-04-30\n"
            "paper_id: test-paper\n"
            "coverage_status: full-index\n"
            "compiled_model: deepseek/deepseek-v4-pro\n"
            "---\n\n" + sections
        )
        try:
            result = wiki_compile.paper_page_complete(tmp)
            assert result is True
        finally:
            import shutil
            shutil.rmtree(tmp.parent)

    def test_returns_false_for_non_full_index(self):
        tmp = _temp_md_file(
            "---\nschema_version: paper-v4-2026-04-30\n"
            "paper_id: test-paper\n"
            "coverage_status: partial\n"
            "compiled_model: deepseek/deepseek-v4-pro\n"
            "---\n\n"
            "## One-line Summary\nPartial test\n"
        )
        try:
            result = wiki_compile.paper_page_complete(tmp)
            assert result is False
        finally:
            import shutil
            shutil.rmtree(tmp.parent)

    def test_returns_false_for_missing_required_headings(self):
        tmp = _temp_md_file(
            "---\nschema_version: paper-v4-2026-04-30\n"
            "paper_id: test-paper\n"
            "coverage_status: full-index\n"
            "compiled_model: deepseek/deepseek-v4-pro\n"
            "---\n\n"
            "# Title Only\nNo required headings here.\n"
        )
        try:
            result = wiki_compile.paper_page_complete(tmp)
            assert result is False
        finally:
            import shutil
            shutil.rmtree(tmp.parent)


class TestStripCodeFence:
    def test_removes_fence(self):
        result = wiki_compile.strip_code_fence("```\ncontent\n```")
        assert result == "content"

    def test_removes_json_fence(self):
        result = wiki_compile.strip_code_fence("```json\n{\"key\": 1}\n```")
        assert result == '{"key": 1}'

    def test_no_fence_unchanged(self):
        assert wiki_compile.strip_code_fence("plain text") == "plain text"


class TestFrontmatterAndJsonScalar:
    def test_json_scalar_string(self):
        result = wiki_compile.json_scalar("hello")
        assert '"hello"' in result

    def test_json_scalar_number(self):
        result = wiki_compile.json_scalar(42)
        assert "42" in result

    def test_frontmatter_output(self):
        fields = {"type": "paper", "title": "Test"}
        result = wiki_compile.frontmatter(fields)
        assert "type:" in result
        assert "title:" in result
        assert result.startswith("---")
        assert result.strip().endswith("---")


class TestResolvePaperSourceId:
    def test_exact_match(self):
        paper_ids = {"2020-smith-test-paper", "2021-jones-other"}
        result = wiki_compile.resolve_paper_source_id("2020-smith-test-paper", paper_ids)
        assert result == "2020-smith-test-paper"

    def test_source_alias_match(self):
        paper_ids = {"2023-gomez-a-non-parametric-discrete-fracture-network-model"}
        result = wiki_compile.resolve_paper_source_id("2023-gomez-a-non-parametric", paper_ids)
        assert result == "2023-gomez-a-non-parametric-discrete-fracture-network-model"

    def test_prefix_match(self):
        paper_ids = {"2020-smith-a-very-long-title-with-suffix"}
        result = wiki_compile.resolve_paper_source_id("2020-smith-a-very-long-title", paper_ids)
        assert result == "2020-smith-a-very-long-title-with-suffix"

    def test_returns_original_on_no_match(self):
        paper_ids = {"2020-smith-valid"}
        result = wiki_compile.resolve_paper_source_id("nonexistent-id", paper_ids)
        assert result == "nonexistent-id"

    def test_empty_returns_empty(self):
        assert wiki_compile.resolve_paper_source_id("", set()) == ""


class TestAggregateFunctions:
    def test_topic_type(self):
        assert wiki_compile.topic_type("concepts") == "concept"
        assert wiki_compile.topic_type("methods") == "method"
        assert wiki_compile.topic_type("claims") == "claim"
        assert wiki_compile.topic_type("syntheses") == "synthesis"
        assert wiki_compile.topic_type("open-questions") == "open-question"
        assert wiki_compile.topic_type("unknown") == "unknown"


class TestSlugify:
    def test_ascii(self):
        result = wiki_compile.slugify("Hello World Test")
        assert result == "hello-world-test"

    def test_removes_special_chars(self):
        result = wiki_compile.slugify('Test: "hello" (world)')
        assert ":" not in result
        assert '"' not in result
        assert "(" not in result

    def test_max_length(self):
        result = wiki_compile.slugify("a" * 200, max_len=20)
        assert len(result) <= 20

    def test_collapses_hyphens(self):
        result = wiki_compile.slugify("hello---world")
        assert "---" not in result
