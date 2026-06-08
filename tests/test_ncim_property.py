"""Tests for NCI Metathesaurus property enum."""

import pytest

from evs_server.models import NCIMProperty
from evs_server.utils import to_url_value


class TestNCIMProperty:
    """Test suite for the NCIMProperty enum."""

    def test_property_values(self):
        """Test that common NCIMProperty enum values convert correctly."""
        properties = [
            (NCIMProperty.CODE, "CODE"),
            (NCIMProperty.SEMANTIC_TYPE, "Semantic_Type"),
            (NCIMProperty.CONTRIBUTING_SOURCE, "Contributing_Source"),
            (NCIMProperty.FDA_UNII_CODE, "FDA_UNII_Code"),
            (NCIMProperty.ENTREZGENE_ID, "EntrezGene_ID"),
            (NCIMProperty.ACTIVE, "ACTIVE"),
        ]
        
        for enum_value, expected_string in properties:
            assert to_url_value(enum_value) == expected_string

    def test_property_count(self):
        """Test that NCIMProperty has exactly 185 values."""
        assert len(NCIMProperty) == 185

    def test_property_string_base(self):
        """Test that NCIMProperty inherits from str."""
        assert isinstance(NCIMProperty.CODE, str)
        assert isinstance(NCIMProperty.SEMANTIC_TYPE.value, str)

    def test_comma_separated_properties(self):
        """Test creating comma-separated list of properties."""
        props = f"{to_url_value(NCIMProperty.CODE)},{to_url_value(NCIMProperty.SEMANTIC_TYPE)}"
        assert props == "CODE,Semantic_Type"

    def test_underscore_properties(self):
        """Test properties with underscores."""
        assert to_url_value(NCIMProperty.AA_GI) == "AA_GI"
        assert to_url_value(NCIMProperty.CDNA_REFSEQ) == "CDNA_REFSEQ"
        assert to_url_value(NCIMProperty.HAS_FIRST_NAME) == "HAS_FIRST_NAME"

    def test_mixed_case_properties(self):
        """Test properties with mixed case."""
        assert to_url_value(NCIMProperty.CHEMICAL_FORMULA) == "Chemical_Formula"
        assert to_url_value(NCIMProperty.GENBANK_ACCESSION_NUMBER) == "GenBank_Accession_Number"
        assert to_url_value(NCIMProperty.ESSENTIAL_AMINO_ACID) == "Essential_Amino_Acid"
