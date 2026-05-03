"""Tests for _lib.py shared utility functions — no I/O except sha256 temp file."""

from __future__ import annotations

import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import _lib


class TestIntEnv:
    def test_returns_default_when_not_set(self):
        assert _lib.int_env("_TEST_NONEXISTENT_VAR_", 42) == 42

    def test_returns_set_value(self):
        os.environ["_TEST_INT_ENV_VAL_"] = "77"
        try:
            assert _lib.int_env("_TEST_INT_ENV_VAL_", 10) == 77
        finally:
            del os.environ["_TEST_INT_ENV_VAL_"]

    def test_allow_zero_accepts_zero(self):
        os.environ["_TEST_INT_ENV_ZERO_"] = "0"
        try:
            assert _lib.int_env("_TEST_INT_ENV_ZERO_", 10, allow_zero=True) == 0
        finally:
            del os.environ["_TEST_INT_ENV_ZERO_"]

    def test_disallow_zero_falls_back(self):
        os.environ["_TEST_INT_ENV_ZERO_"] = "0"
        try:
            assert _lib.int_env("_TEST_INT_ENV_ZERO_", 10, allow_zero=False) == 10
        finally:
            del os.environ["_TEST_INT_ENV_ZERO_"]

    def test_invalid_string_returns_default(self):
        os.environ["_TEST_INT_ENV_BAD_"] = "not_a_number"
        try:
            assert _lib.int_env("_TEST_INT_ENV_BAD_", 99) == 99
        finally:
            del os.environ["_TEST_INT_ENV_BAD_"]


class TestFloatEnv:
    def test_returns_default_when_not_set(self):
        assert _lib.float_env("_TEST_FLOAT_NONE_", 3.14) == 3.14

    def test_returns_set_value(self):
        os.environ["_TEST_FLOAT_VAL_"] = "2.5"
        try:
            assert _lib.float_env("_TEST_FLOAT_VAL_", 1.0) == 2.5
        finally:
            del os.environ["_TEST_FLOAT_VAL_"]

    def test_invalid_returns_default(self):
        os.environ["_TEST_FLOAT_BAD_"] = "abc"
        try:
            assert _lib.float_env("_TEST_FLOAT_BAD_", 0.5) == 0.5
        finally:
            del os.environ["_TEST_FLOAT_BAD_"]


class TestParseAllowedItemTypes:
    def test_default_journal_article(self):
        assert _lib.parse_allowed_item_types(None) == {"journalArticle"}
        assert _lib.parse_allowed_item_types("") == {"journalArticle"}

    def test_all_disables_filter(self):
        assert _lib.parse_allowed_item_types("all") == set()
        assert _lib.parse_allowed_item_types("ALL") == set()

    def test_comma_separated(self):
        result = _lib.parse_allowed_item_types("journalArticle,book,thesis")
        assert result == {"journalArticle", "book", "thesis"}

    def test_strips_whitespace(self):
        result = _lib.parse_allowed_item_types(" journalArticle ,  book  , thesis ")
        assert result == {"journalArticle", "book", "thesis"}


class TestSha256File:
    def test_known_content(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
            f.write("hello world")
            tmp = Path(f.name)
        try:
            digest = _lib.sha256_file(tmp)
            assert len(digest) == 64
            assert all(c in "0123456789abcdef" for c in digest)
            # Known SHA256 of "hello world"
            assert digest == "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9"
        finally:
            tmp.unlink()


class TestParseFrontmatterScalar:
    def test_empty_returns_empty_string(self):
        assert _lib.parse_frontmatter_scalar("") == ""

    def test_json_number(self):
        assert _lib.parse_frontmatter_scalar("42") == 42

    def test_json_bool(self):
        assert _lib.parse_frontmatter_scalar("true") is True

    def test_strips_quotes(self):
        assert _lib.parse_frontmatter_scalar('"hello"') == "hello"
        assert _lib.parse_frontmatter_scalar("'world'") == "world"

    def test_plain_string(self):
        assert _lib.parse_frontmatter_scalar("plain-text") == "plain-text"


class TestParseSimpleFrontmatter:
    def test_basic_fields(self):
        content = "---\ntitle: Test\nstatus: draft\n---\n\n# Body"
        fields = _lib.parse_simple_frontmatter(content)
        assert fields["title"] == "Test"
        assert fields["status"] == "draft"

    def test_list_field(self):
        content = "---\ntags:\n  - tag1\n  - tag2\n---\n\n# Body"
        fields = _lib.parse_simple_frontmatter(content)
        assert isinstance(fields["tags"], list)
        assert fields["tags"] == ["tag1", "tag2"]

    def test_no_frontmatter(self):
        assert _lib.parse_simple_frontmatter("# Just a heading") == {}

    def test_nested_list_with_numbers(self):
        content = "---\nsources:\n  - source1\n  - 42\n  - true\n---\n\n# Body"
        fields = _lib.parse_simple_frontmatter(content)
        assert fields["sources"] == ["source1", 42, True]

    def test_mixed_list_and_scalar_keys(self):
        content = "---\ntitle: My Paper\naliases:\n  - a\n  - b\nstatus: draft\n---\n\n# Body"
        fields = _lib.parse_simple_frontmatter(content)
        assert fields["title"] == "My Paper"
        assert fields["aliases"] == ["a", "b"]
        assert fields["status"] == "draft"


class TestFrontmatterStrings:
    def test_scalar_value(self):
        fields = {"key": "value"}
        assert _lib.frontmatter_strings(fields, "key") == ["value"]

    def test_list_value(self):
        fields = {"key": ["a", "b", "c"]}
        assert _lib.frontmatter_strings(fields, "key") == ["a", "b", "c"]

    def test_missing_key(self):
        assert _lib.frontmatter_strings({}, "missing") == []

    def test_filters_empty_strings(self):
        fields = {"key": ["a", "", "b", "  "]}
        assert _lib.frontmatter_strings(fields, "key") == ["a", "b"]


class TestStripFrontmatter:
    def test_removes_frontmatter(self):
        content = "---\ntitle: test\n---\n\n# Heading\nBody"
        result = _lib.strip_frontmatter(content)
        assert "title:" not in result
        assert "# Heading" in result
        assert "Body" in result

    def test_no_frontmatter_unchanged(self):
        content = "# Heading\nBody text"
        result = _lib.strip_frontmatter(content)
        assert result == content

    def test_preserves_body_frontmatter_like_text(self):
        content = "# Title\n---\nNot real frontmatter"
        result = _lib.strip_frontmatter(content)
        assert result == content


class TestCleanExcerpt:
    def test_short_text_unchanged(self):
        assert _lib.clean_excerpt("hello world", max_chars=100) == "hello world"

    def test_long_text_truncated(self):
        text = "word " * 200
        result = _lib.clean_excerpt(text, max_chars=80)
        assert len(result) <= 83
        assert result.endswith("...")

    def test_collapses_whitespace(self):
        result = _lib.clean_excerpt("hello    world\n\n\ntest", max_chars=100)
        assert "   " not in result
        assert "\n\n\n" not in result


class TestExtractMarkdownSection:
    def test_extracts_heading_content(self):
        content = "## One-line Summary\nThis is a summary.\n\n## Next Section\nOther content"
        result = _lib.extract_markdown_section(content, "One-line Summary")
        assert "This is a summary" in result

    def test_missing_heading_returns_empty(self):
        content = "## Existing Section\nSome text"
        assert _lib.extract_markdown_section(content, "Missing Section") == ""


class TestMarkdownHeadings:
    def test_extracts_headings(self):
        content = "# Title\n## Section A\nSome text\n### Sub A\n## Section B\nMore text"
        headings = _lib.markdown_headings(content)
        assert headings == ["Section A", "Sub A", "Section B"]

    def test_no_headings(self):
        assert _lib.markdown_headings("Just plain text.") == []
