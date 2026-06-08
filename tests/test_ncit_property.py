"""Tests for NCI Thesaurus property enum."""

import pytest

from evs_server.models import NCITProperty
from evs_server.utils import to_url_value


class TestNCITProperty:
    """Test suite for the NCITProperty enum."""

    def test_property_values(self):
        """Test that common NCITProperty enum values convert correctly."""
        properties = [
            (NCITProperty.OMIM_NUMBER, "P100"),
            (NCITProperty.SEMANTIC_TYPE, "P106"),
            (NCITProperty.CONTRIBUTING_SOURCE, "P322"),
            (NCITProperty.FDA_UNII_CODE, "P319"),
            (NCITProperty.ENTREZGENE_ID, "P321"),
            (NCITProperty.CONCEPT_STATUS, "P310"),
        ]
        
        for enum_value, expected_string in properties:
            assert to_url_value(enum_value) == expected_string

    def test_property_count(self):
        """Test that NCITProperty has exactly 70 values."""
        assert len(NCITProperty) == 70

    def test_special_properties(self):
        """Test properties with special formats."""
        assert to_url_value(NCITProperty.XREF) == "oboInOwl:hasDbXref"
        assert to_url_value(NCITProperty.DEPRECATED) == "owl:deprecated"

    def test_property_string_base(self):
        """Test that NCITProperty inherits from str."""
        assert isinstance(NCITProperty.SEMANTIC_TYPE, str)
        assert isinstance(NCITProperty.OMIM_NUMBER.value, str)

    def test_comma_separated_properties(self):
        """Test creating comma-separated list of properties."""
        props = f"{to_url_value(NCITProperty.SEMANTIC_TYPE)},{to_url_value(NCITProperty.CONTRIBUTING_SOURCE)}"
        assert props == "P106,P322"

    def test_all_p_codes_start_with_p_or_special(self):
        """Test that all property codes follow expected pattern."""
        for prop in NCITProperty:
            # Should start with P, NHC, obo, or owl
            assert (
                prop.value.startswith("P") or 
                prop.value.startswith("NHC") or 
                prop.value.startswith("obo") or 
                prop.value.startswith("owl")
            ), f"{prop.value} doesn't follow expected pattern"
