"""Tests for Terminology enum."""

import pytest

from evs_server.models import Terminology
from evs_server.utils import to_url_value


class TestTerminology:
    """Test suite for the Terminology enum."""

    def test_common_terminologies(self):
        """Test that common terminology values convert correctly."""
        terminologies = [
            (Terminology.NCIT, "ncit"),
            (Terminology.NCIM, "ncim"),
            (Terminology.SNOMEDCT_US, "snomedct_us"),
            (Terminology.LOINC, "loinc"),
            (Terminology.ICD10, "icd10"),
        ]
        
        for enum_value, expected_string in terminologies:
            assert to_url_value(enum_value) == expected_string

    def test_terminology_count(self):
        """Test that Terminology has exactly 26 values."""
        assert len(Terminology) == 26

    def test_terminology_string_base(self):
        """Test that Terminology inherits from str."""
        assert isinstance(Terminology.NCIT, str)
        assert isinstance(Terminology.NCIM.value, str)

    def test_all_terminologies_lowercase(self):
        """Test that all terminology codes are lowercase."""
        for term in Terminology:
            assert term.value.islower(), f"{term.value} should be lowercase"

    def test_underscores_in_terminologies(self):
        """Test terminologies with underscores."""
        assert to_url_value(Terminology.SNOMEDCT_US) == "snomedct_us"
        assert to_url_value(Terminology.ICD10CM) == "icd10cm"
        assert to_url_value(Terminology.ICD9CM) == "icd9cm"

    def test_all_terminology_values(self):
        """Test that all 26 Terminology enum values convert correctly."""
        terminologies = [
            (Terminology.NCIT, "ncit"),
            (Terminology.NCIM, "ncim"),
            (Terminology.CANMED, "canmed"),
            (Terminology.CHEBI, "chebi"),
            (Terminology.CTCAE5, "ctcae5"),
            (Terminology.DUO, "duo"),
            (Terminology.GO, "go"),
            (Terminology.HGNC, "hgnc"),
            (Terminology.HL7V30, "hl7v30"),
            (Terminology.ICD10, "icd10"),
            (Terminology.ICD10CM, "icd10cm"),
            (Terminology.ICD9CM, "icd9cm"),
            (Terminology.LOINC, "loinc"),
            (Terminology.MA, "ma"),
            (Terminology.MDR, "mdr"),
            (Terminology.MEDRT, "medrt"),
            (Terminology.MGED, "mged"),
            (Terminology.NDFRT, "ndfrt"),
            (Terminology.NPO, "npo"),
            (Terminology.OBI, "obi"),
            (Terminology.OBIB, "obib"),
            (Terminology.PDQ, "pdq"),
            (Terminology.RADLEX, "radlex"),
            (Terminology.SNOMEDCT_US, "snomedct_us"),
            (Terminology.UMLSSEMNET, "umlssemnet"),
            (Terminology.ZFA, "zfa"),
        ]
        
        for enum_value, expected_string in terminologies:
            assert to_url_value(enum_value) == expected_string
