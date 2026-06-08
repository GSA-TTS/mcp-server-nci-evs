"""Tests for NCI Metathesaurus definition source enum."""

import pytest

from evs_server.models import NCIMDefinitionSource
from evs_server.utils import to_url_value


class TestNCIMDefinitionSource:
    """Test suite for the NCIMDefinitionSource enum."""

    def test_definition_source_values(self):
        """Test that common NCIMDefinitionSource enum values convert correctly."""
        sources = [
            (NCIMDefinitionSource.NCI, "NCI"),
            (NCIMDefinitionSource.MSH, "MSH"),
            (NCIMDefinitionSource.SNOMEDCT_US, "SNOMEDCT_US"),
            (NCIMDefinitionSource.GO, "GO"),
            (NCIMDefinitionSource.FMA, "FMA"),
            (NCIMDefinitionSource.HPO, "HPO"),
        ]
        
        for enum_value, expected_string in sources:
            assert to_url_value(enum_value) == expected_string

    def test_definition_source_count(self):
        """Test that NCIMDefinitionSource has exactly 53 values."""
        assert len(NCIMDefinitionSource) == 53

    def test_definition_source_with_special_chars(self):
        """Test definition sources with special characters convert correctly."""
        assert to_url_value(NCIMDefinitionSource.ACC_AHA) == "ACC-AHA"
        assert to_url_value(NCIMDefinitionSource.CDISC_GLOSS) == "CDISC-GLOSS"
        assert to_url_value(NCIMDefinitionSource.NCI_GLOSS) == "NCI-GLOSS"
        assert to_url_value(NCIMDefinitionSource.EDQM_HC) == "EDQM-HC"
        assert to_url_value(NCIMDefinitionSource.FDA_NIH_MORE) == "FDA-NIH-MoRE"
        assert to_url_value(NCIMDefinitionSource.MRCT_CTR) == "MRCT-Ctr"

    def test_definition_source_with_underscores(self):
        """Test definition sources with underscores."""
        assert to_url_value(NCIMDefinitionSource.BRIDG_3_0_3) == "BRIDG_3_0_3"
        assert to_url_value(NCIMDefinitionSource.BRIDG_5_3) == "BRIDG_5_3"
        assert to_url_value(NCIMDefinitionSource.CTCAE_3) == "CTCAE_3"
        assert to_url_value(NCIMDefinitionSource.CTCAE_5) == "CTCAE_5"
        assert to_url_value(NCIMDefinitionSource.DIPG_DMG) == "DIPG_DMG"
        assert to_url_value(NCIMDefinitionSource.HL7V3_0) == "HL7V3.0"

    def test_definition_source_string_base(self):
        """Test that NCIMDefinitionSource inherits from str."""
        assert isinstance(NCIMDefinitionSource.NCI, str)
        assert isinstance(NCIMDefinitionSource.MSH.value, str)

    def test_comma_separated_sources(self):
        """Test creating comma-separated list of definition sources."""
        sources = f"{to_url_value(NCIMDefinitionSource.NCI)},{to_url_value(NCIMDefinitionSource.MSH)}"
        assert sources == "NCI,MSH"

    def test_loinc_source(self):
        """Test LOINC source (LNC code)."""
        assert to_url_value(NCIMDefinitionSource.LNC) == "LNC"

    def test_meddra_source(self):
        """Test MedDRA source (MDR code)."""
        assert to_url_value(NCIMDefinitionSource.MDR) == "MDR"

    def test_case_sensitive_sources(self):
        """Test that sources maintain proper case sensitivity."""
        # BioCarta should maintain its case
        assert to_url_value(NCIMDefinitionSource.BIOC) == "BioC"
        
        # CARELEX should be all caps
        assert to_url_value(NCIMDefinitionSource.CARELEX) == "CARELEX"
