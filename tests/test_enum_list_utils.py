"""Tests for enum list utilities."""

import pytest

from evs_server.models import (
    NCIMDefinitionSource,
    NCIMProperty,
    NCIMSynonymSource,
    NCIMSynonymTermType,
    NCITDefinitionSource,
    NCITProperty,
    NCITSynonymSource,
    NCITSynonymTermType,
)
from evs_server.utils import to_enum_list_value, validate_enum_for_terminology


class TestToEnumListValue:
    """Tests for to_enum_list_value function."""

    def test_single_enum_value(self):
        """Test conversion of single enum value."""
        result = to_enum_list_value(NCITProperty.SEMANTIC_TYPE, NCITProperty, "property")
        assert result == "P106"

    def test_list_of_enum_values(self):
        """Test conversion of list of enum values."""
        result = to_enum_list_value(
            [NCITProperty.SEMANTIC_TYPE, NCITProperty.CONTRIBUTING_SOURCE],
            NCITProperty,
            "property",
        )
        assert result == "P106,P322"

    def test_none_value(self):
        """Test that None returns None."""
        result = to_enum_list_value(None, NCITProperty, "property")
        assert result is None

    def test_wrong_enum_type(self):
        """Test that wrong enum type raises TypeError."""
        with pytest.raises(TypeError, match="must be of type NCITProperty"):
            to_enum_list_value(NCIMProperty.CODE, NCITProperty, "property")

    def test_empty_list(self):
        """Test that empty list raises ValueError."""
        with pytest.raises(ValueError, match="cannot be an empty list"):
            to_enum_list_value([], NCITProperty, "property")

    def test_list_with_wrong_enum_type(self):
        """Test that list with wrong enum type raises TypeError."""
        with pytest.raises(TypeError, match="must be of type NCITProperty"):
            to_enum_list_value([NCIMProperty.CODE], NCITProperty, "property")

    def test_ncit_definition_source(self):
        """Test NCITDefinitionSource enum."""
        result = to_enum_list_value(NCITDefinitionSource.NCI, NCITDefinitionSource, "definitionSource")
        assert result == "NCI"

    def test_ncim_definition_source(self):
        """Test NCIMDefinitionSource enum."""
        result = to_enum_list_value(NCIMDefinitionSource.MSH, NCIMDefinitionSource, "definitionSource")
        assert result == "MSH"

    def test_ncit_synonym_source(self):
        """Test NCITSynonymSource enum."""
        result = to_enum_list_value(NCITSynonymSource.CDISC, NCITSynonymSource, "synonymSource")
        assert result == "CDISC"

    def test_ncim_synonym_source(self):
        """Test NCIMSynonymSource enum."""
        result = to_enum_list_value(NCIMSynonymSource.SNOMEDCT_US, NCIMSynonymSource, "synonymSource")
        assert result == "SNOMEDCT_US"

    def test_ncit_synonym_term_type(self):
        """Test NCITSynonymTermType enum."""
        result = to_enum_list_value(NCITSynonymTermType.PT, NCITSynonymTermType, "synonymTermType")
        assert result == "PT"

    def test_ncim_synonym_term_type(self):
        """Test NCIMSynonymTermType enum."""
        result = to_enum_list_value(NCIMSynonymTermType.SY, NCIMSynonymTermType, "synonymTermType")
        assert result == "SY"


class TestValidateEnumForTerminology:
    """Tests for validate_enum_for_terminology function."""

    def test_valid_ncit_property_with_ncit(self):
        """Test valid NCIT property with ncit terminology."""
        # Should not raise
        validate_enum_for_terminology(
            NCITProperty.SEMANTIC_TYPE,
            "ncit",
            NCITProperty,
            NCIMProperty,
            "property",
        )

    def test_valid_ncim_property_with_ncim(self):
        """Test valid NCIM property with ncim terminology."""
        # Should not raise
        validate_enum_for_terminology(
            NCIMProperty.CODE,
            "ncim",
            NCITProperty,
            NCIMProperty,
            "property",
        )

    def test_ncit_property_with_wrong_terminology(self):
        """Test NCIT property with ncim terminology raises error."""
        with pytest.raises(ValueError, match="can ONLY be used when terminology='ncit'"):
            validate_enum_for_terminology(
                NCITProperty.SEMANTIC_TYPE,
                "ncim",
                NCITProperty,
                NCIMProperty,
                "property",
            )

    def test_ncim_property_with_wrong_terminology(self):
        """Test NCIM property with ncit terminology raises error."""
        with pytest.raises(ValueError, match="can ONLY be used when terminology='ncim'"):
            validate_enum_for_terminology(
                NCIMProperty.CODE,
                "ncit",
                NCITProperty,
                NCIMProperty,
                "property",
            )

    def test_valid_list_of_ncit_properties(self):
        """Test valid list of NCIT properties with ncit terminology."""
        # Should not raise
        validate_enum_for_terminology(
            [NCITProperty.SEMANTIC_TYPE, NCITProperty.CONTRIBUTING_SOURCE],
            "ncit",
            NCITProperty,
            NCIMProperty,
            "property",
        )

    def test_list_with_ncim_property_and_ncit_terminology(self):
        """Test list containing NCIM property with ncit terminology raises error."""
        with pytest.raises(ValueError, match="can ONLY be used when terminology='ncim'"):
            validate_enum_for_terminology(
                [NCITProperty.SEMANTIC_TYPE, NCIMProperty.CODE],
                "ncit",
                NCITProperty,
                NCIMProperty,
                "property",
            )

    def test_none_value(self):
        """Test that None value passes validation."""
        # Should not raise
        validate_enum_for_terminology(
            None,
            "ncit",
            NCITProperty,
            NCIMProperty,
            "property",
        )

    def test_ncit_definition_source_with_ncit(self):
        """Test NCIT definition source with ncit terminology."""
        # Should not raise
        validate_enum_for_terminology(
            NCITDefinitionSource.NCI,
            "ncit",
            NCITDefinitionSource,
            NCIMDefinitionSource,
            "definitionSource",
        )

    def test_ncim_definition_source_with_ncim(self):
        """Test NCIM definition source with ncim terminology."""
        # Should not raise
        validate_enum_for_terminology(
            NCIMDefinitionSource.MSH,
            "ncim",
            NCITDefinitionSource,
            NCIMDefinitionSource,
            "definitionSource",
        )

    def test_ncit_synonym_source_with_ncit(self):
        """Test NCIT synonym source with ncit terminology."""
        # Should not raise
        validate_enum_for_terminology(
            NCITSynonymSource.CDISC,
            "ncit",
            NCITSynonymSource,
            NCIMSynonymSource,
            "synonymSource",
        )

    def test_ncim_synonym_source_with_ncim(self):
        """Test NCIM synonym source with ncim terminology."""
        # Should not raise
        validate_enum_for_terminology(
            NCIMSynonymSource.SNOMEDCT_US,
            "ncim",
            NCITSynonymSource,
            NCIMSynonymSource,
            "synonymSource",
        )

    def test_ncit_synonym_term_type_with_ncit(self):
        """Test NCIT synonym term type with ncit terminology."""
        # Should not raise
        validate_enum_for_terminology(
            NCITSynonymTermType.PT,
            "ncit",
            NCITSynonymTermType,
            NCIMSynonymTermType,
            "synonymTermType",
        )

    def test_ncim_synonym_term_type_with_ncim(self):
        """Test NCIM synonym term type with ncim terminology."""
        # Should not raise
        validate_enum_for_terminology(
            NCIMSynonymTermType.SY,
            "ncim",
            NCITSynonymTermType,
            NCIMSynonymTermType,
            "synonymTermType",
        )
