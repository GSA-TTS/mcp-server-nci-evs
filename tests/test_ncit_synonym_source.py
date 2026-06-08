"""Tests for NCI Thesaurus synonym source enum."""

import pytest

from evs_server.models import NCITSynonymSource
from evs_server.utils import to_url_value


class TestNCITSynonymSource:
    """Test suite for the NCITSynonymSource enum."""

    def test_synonym_source_values(self):
        """Test that common NCITSynonymSource enum values convert correctly."""
        sources = [
            (NCITSynonymSource.NCI, "NCI"),
            (NCITSynonymSource.CDISC, "CDISC"),
            (NCITSynonymSource.FDA, "FDA"),
            (NCITSynonymSource.CTCAE, "CTCAE"),
            (NCITSynonymSource.NICHD, "NICHD"),
            (NCITSynonymSource.WHO, "WHO"),
        ]
        
        for enum_value, expected_string in sources:
            assert to_url_value(enum_value) == expected_string

    def test_synonym_source_count(self):
        """Test that NCITSynonymSource has exactly 61 values."""
        assert len(NCITSynonymSource) == 61

    def test_synonym_source_with_special_chars(self):
        """Test synonym sources with special characters convert correctly."""
        assert to_url_value(NCITSynonymSource.ACC_AHA) == "ACC/AHA"
        assert to_url_value(NCITSynonymSource.CDISC_GLOSS) == "CDISC-GLOSS"
        assert to_url_value(NCITSynonymSource.NCI_GLOSS) == "NCI-GLOSS"
        assert to_url_value(NCITSynonymSource.DIPG_DMG) == "DIPG/DMG"
        assert to_url_value(NCITSynonymSource.FDA_NIH_MORE) == "FDA-NIH-MoRE"

    def test_synonym_source_with_versions(self):
        """Test synonym sources with version numbers."""
        assert to_url_value(NCITSynonymSource.BRIDG_3_0_3) == "BRIDG 3.0.3"
        assert to_url_value(NCITSynonymSource.BRIDG_5_3) == "BRIDG 5.3"
        assert to_url_value(NCITSynonymSource.CTCAE_3_0) == "CTCAE 3.0"
        assert to_url_value(NCITSynonymSource.CTCAE_5_0) == "CTCAE 5.0"
        assert to_url_value(NCITSynonymSource.CTCAE_6_0) == "CTCAE 6.0"

    def test_synonym_source_string_base(self):
        """Test that NCITSynonymSource inherits from str."""
        assert isinstance(NCITSynonymSource.NCI, str)
        assert isinstance(NCITSynonymSource.CDISC.value, str)

    def test_comma_separated_sources(self):
        """Test creating comma-separated list of synonym sources."""
        sources = f"{to_url_value(NCITSynonymSource.NCI)},{to_url_value(NCITSynonymSource.CDISC)}"
        assert sources == "NCI,CDISC"

    def test_mixed_case_sources(self):
        """Test sources with mixed case."""
        assert to_url_value(NCITSynonymSource.CARELEX) == "CareLex"
        assert to_url_value(NCITSynonymSource.CELLOSAURUS) == "Cellosaurus"
        assert to_url_value(NCITSynonymSource.HEMONC) == "HemOnc"
        assert to_url_value(NCITSynonymSource.ZFIN) == "ZFin"
        assert to_url_value(NCITSynonymSource.CADSR) == "caDSR"
        assert to_url_value(NCITSynonymSource.MCODE) == "mCode"

    def test_hyphenated_sources(self):
        """Test sources with hyphens."""
        assert to_url_value(NCITSynonymSource.ICD_10) == "ICD-10"
        assert to_url_value(NCITSynonymSource.PI_RADS) == "PI-RADS"
        assert to_url_value(NCITSynonymSource.PRO_CTCAE) == "PRO-CTCAE"
