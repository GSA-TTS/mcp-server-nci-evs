"""Tests for Include enum."""

import pytest

from evs_server.models import Include
from evs_server.utils import to_url_value


class TestInclude:
    """Test suite for the Include enum."""

    def test_special_include_values(self):
        """Test that special include values convert correctly."""
        includes = [
            (Include.MINIMAL, "minimal"),
            (Include.SUMMARY, "summary"),
            (Include.FULL, "full"),
        ]
        
        for enum_value, expected_string in includes:
            assert to_url_value(enum_value) == expected_string

    def test_concept_part_include_values(self):
        """Test that concept part include values convert correctly."""
        includes = [
            (Include.ASSOCIATIONS, "associations"),
            (Include.CHILDREN, "children"),
            (Include.DEFINITIONS, "definitions"),
            (Include.DESCENDANTS, "descendants"),
            (Include.HISTORY, "history"),
            (Include.MAPS, "maps"),
            (Include.PARENTS, "parents"),
            (Include.PROPERTIES, "properties"),
            (Include.ROLES, "roles"),
            (Include.SYNONYMS, "synonyms"),
        ]
        
        for enum_value, expected_string in includes:
            assert to_url_value(enum_value) == expected_string

    def test_camel_case_include_values(self):
        """Test that camelCase include values convert correctly."""
        assert to_url_value(Include.DISJOINT_WITH) == "disjointWith"
        assert to_url_value(Include.INVERSE_ASSOCIATIONS) == "inverseAssociations"
        assert to_url_value(Include.INVERSE_ROLES) == "inverseRoles"

    def test_include_count(self):
        """Test that Include has exactly 17 values."""
        assert len(Include) == 17

    def test_include_string_base(self):
        """Test that Include inherits from str."""
        assert isinstance(Include.MINIMAL, str)
        assert isinstance(Include.SUMMARY.value, str)

    def test_comma_separated_includes(self):
        """Test creating comma-separated list of includes."""
        includes = f"{to_url_value(Include.SYNONYMS)},{to_url_value(Include.DEFINITIONS)},{to_url_value(Include.PROPERTIES)}"
        assert includes == "synonyms,definitions,properties"
        # This should be equivalent to summary
