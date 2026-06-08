"""Tests for NCI Metathesaurus synonym source enum."""

import pytest

from evs_server.models import NCIMSynonymSource
from evs_server.utils import to_url_value


class TestNCIMSynonymSource:
    """Test suite for the NCIMSynonymSource enum."""

    def test_synonym_source_values(self):
        """Test that common NCIMSynonymSource enum values convert correctly."""
        sources = [
            (NCIMSynonymSource.NCI, "NCI"),
            (NCIMSynonymSource.MSH, "MSH"),
            (NCIMSynonymSource.SNOMEDCT_US, "SNOMEDCT_US"),
            (NCIMSynonymSource.GO, "GO"),
            (NCIMSynonymSource.FMA, "FMA"),
            (NCIMSynonymSource.HPO, "HPO"),
        ]
        
        for enum_value, expected_string in sources:
            assert to_url_value(enum_value) == expected_string

    def test_synonym_source_count(self):
        """Test that NCIMSynonymSource has exactly 119 values."""
        assert len(NCIMSynonymSource) == 119

    def test_synonym_source_with_special_chars(self):
        """Test synonym sources with special characters convert correctly."""
        assert to_url_value(NCIMSynonymSource.ACC_AHA) == "ACC-AHA"
        assert to_url_value(NCIMSynonymSource.CDISC_GLOSS) == "CDISC-GLOSS"
        assert to_url_value(NCIMSynonymSource.NCI_GLOSS) == "NCI-GLOSS"
        assert to_url_value(NCIMSynonymSource.EDQM_HC) == "EDQM-HC"
        assert to_url_value(NCIMSynonymSource.FDA_NIH_MORE) == "FDA-NIH-MoRE"
        assert to_url_value(NCIMSynonymSource.MRCT_CTR) == "MRCT-Ctr"

    def test_synonym_source_with_underscores(self):
        """Test synonym sources with underscores."""
        assert to_url_value(NCIMSynonymSource.BRIDG_3_0_3) == "BRIDG_3_0_3"
        assert to_url_value(NCIMSynonymSource.BRIDG_5_3) == "BRIDG_5_3"
        assert to_url_value(NCIMSynonymSource.CTCAE_3) == "CTCAE_3"
        assert to_url_value(NCIMSynonymSource.CTCAE_5) == "CTCAE_5"
        assert to_url_value(NCIMSynonymSource.DIPG_DMG) == "DIPG_DMG"
        assert to_url_value(NCIMSynonymSource.HL7V3_0) == "HL7V3.0"
        assert to_url_value(NCIMSynonymSource.CCSR_ICD10CM) == "CCSR_ICD10CM"
        assert to_url_value(NCIMSynonymSource.CCSR_ICD10PCS) == "CCSR_ICD10PCS"

    def test_synonym_source_string_base(self):
        """Test that NCIMSynonymSource inherits from str."""
        assert isinstance(NCIMSynonymSource.NCI, str)
        assert isinstance(NCIMSynonymSource.MSH.value, str)

    def test_comma_separated_sources(self):
        """Test creating comma-separated list of synonym sources."""
        sources = f"{to_url_value(NCIMSynonymSource.NCI)},{to_url_value(NCIMSynonymSource.MSH)}"
        assert sources == "NCI,MSH"

    def test_loinc_source(self):
        """Test LOINC source (LNC code)."""
        assert to_url_value(NCIMSynonymSource.LNC) == "LNC"

    def test_meddra_source(self):
        """Test MedDRA source (MDR code)."""
        assert to_url_value(NCIMSynonymSource.MDR) == "MDR"

    def test_case_sensitive_sources(self):
        """Test that sources maintain proper case sensitivity."""
        # BioCarta should maintain its case
        assert to_url_value(NCIMSynonymSource.BIOC) == "BioC"
        
        # CARELEX should be all caps
        assert to_url_value(NCIMSynonymSource.CARELEX) == "CARELEX"
        
        # Mixed case examples
        assert to_url_value(NCIMSynonymSource.HEMONC) == "HemOnc"
        assert to_url_value(NCIMSynonymSource.SERONET) == "SeroNet"

    def test_icd_codes(self):
        """Test ICD code variations."""
        assert to_url_value(NCIMSynonymSource.ICD_10) == "ICD-10"
        assert to_url_value(NCIMSynonymSource.ICD10) == "ICD10"
        assert to_url_value(NCIMSynonymSource.ICD10CM) == "ICD10CM"
        assert to_url_value(NCIMSynonymSource.ICD10PCS) == "ICD10PCS"
        assert to_url_value(NCIMSynonymSource.ICD9CM) == "ICD9CM"

    def test_special_metathesaurus_sources(self):
        """Test special UMLS Metathesaurus sources."""
        assert to_url_value(NCIMSynonymSource.MTH) == "MTH"
        assert to_url_value(NCIMSynonymSource.MTHCMSFRF) == "MTHCMSFRF"
        assert to_url_value(NCIMSynonymSource.MTHICD9) == "MTHICD9"
        assert to_url_value(NCIMSynonymSource.MTHMST) == "MTHMST"
        assert to_url_value(NCIMSynonymSource.MTHSPL) == "MTHSPL"

    def test_nci_specific_sources(self):
        """Test NCI-specific sources."""
        assert to_url_value(NCIMSynonymSource.NCI_GLOSS) == "NCI-GLOSS"
        assert to_url_value(NCIMSynonymSource.NCI_HGNC) == "NCI-HGNC"
        assert to_url_value(NCIMSynonymSource.NCI_HL7) == "NCI-HL7"

    def test_lowercase_prefixed_sources(self):
        """Test sources with lowercase prefixes."""
        assert to_url_value(NCIMSynonymSource.CADSR) == "caDSR"
        assert to_url_value(NCIMSynonymSource.MCODE) == "mCode"

    def test_iso_standard(self):
        """Test ISO standard source."""
        assert to_url_value(NCIMSynonymSource.ISO3166_2) == "ISO3166-2"
