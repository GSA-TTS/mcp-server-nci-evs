"""Tests for SearchType enum."""

import pytest

from evs_server.models import SearchType
from evs_server.utils import to_url_value


class TestSearchType:
    """Test suite for the SearchType enum."""

    def test_search_type_values(self):
        """Test that all SearchType enum values convert correctly."""
        types = [
            (SearchType.CONTAINS, "contains"),
            (SearchType.MATCH, "match"),
            (SearchType.STARTS_WITH, "startsWith"),
            (SearchType.PHRASE, "phrase"),
            (SearchType.AND, "AND"),
            (SearchType.OR, "OR"),
            (SearchType.FUZZY, "fuzzy"),
        ]
        
        for enum_value, expected_string in types:
            assert to_url_value(enum_value) == expected_string

    def test_search_type_count(self):
        """Test that SearchType has exactly 7 values."""
        assert len(SearchType) == 7

    def test_search_type_string_base(self):
        """Test that SearchType inherits from str."""
        assert isinstance(SearchType.CONTAINS, str)
        assert isinstance(SearchType.MATCH.value, str)

    def test_boolean_operators(self):
        """Test that boolean operators are uppercase."""
        assert to_url_value(SearchType.AND) == "AND"
        assert to_url_value(SearchType.OR) == "OR"

    def test_camel_case_value(self):
        """Test that startsWith maintains camelCase."""
        assert to_url_value(SearchType.STARTS_WITH) == "startsWith"
