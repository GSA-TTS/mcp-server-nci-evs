"""Tests for URL utility functions."""

import pytest

from evs_server.models import Include, Terminology
from evs_server.utils import to_url_value


class TestToUrlValue:
    """Test suite for the to_url_value utility function."""

    def test_terminology_enum_conversion(self):
        """Test that Terminology enum values are correctly converted to strings."""
        assert to_url_value(Terminology.NCIT) == "ncit"
        assert to_url_value(Terminology.NCIM) == "ncim"
        assert to_url_value(Terminology.CHEBI) == "chebi"
        assert to_url_value(Terminology.SNOMEDCT_US) == "snomedct_us"

    def test_include_enum_conversion(self):
        """Test that Include enum values are correctly converted to strings."""
        assert to_url_value(Include.MINIMAL) == "minimal"
        assert to_url_value(Include.SUMMARY) == "summary"
        assert to_url_value(Include.FULL) == "full"
        assert to_url_value(Include.ASSOCIATIONS) == "associations"
        assert to_url_value(Include.DISJOINT_WITH) == "disjointWith"

    def test_string_passthrough(self):
        """Test that string values are passed through unchanged."""
        assert to_url_value("already_a_string") == "already_a_string"
        assert to_url_value("test123") == "test123"

    def test_other_types_conversion(self):
        """Test that other types are converted to strings."""
        assert to_url_value(123) == "123"
        assert to_url_value(True) == "True"
        assert to_url_value(45.67) == "45.67"

    def test_url_construction(self):
        """Test that enums work correctly in URL construction."""
        base_url = "https://api-evsrest.nci.nih.gov/api/v1"
        terminology = Terminology.NCIT
        include = Include.SUMMARY
        
        url = f"{base_url}/concept/{to_url_value(terminology)}"
        expected_url = "https://api-evsrest.nci.nih.gov/api/v1/concept/ncit"
        
        assert url == expected_url
        assert to_url_value(include) == "summary"

    def test_all_terminologies(self):
        """Test that all Terminology enum values convert correctly."""
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

    def test_all_includes(self):
        """Test that all Include enum values convert correctly."""
        includes = [
            (Include.MINIMAL, "minimal"),
            (Include.SUMMARY, "summary"),
            (Include.FULL, "full"),
            (Include.ASSOCIATIONS, "associations"),
            (Include.CHILDREN, "children"),
            (Include.DEFINITIONS, "definitions"),
            (Include.DESCENDANTS, "descendants"),
            (Include.DISJOINT_WITH, "disjointWith"),
            (Include.HISTORY, "history"),
            (Include.INVERSE_ASSOCIATIONS, "inverseAssociations"),
            (Include.INVERSE_ROLES, "inverseRoles"),
            (Include.MAPS, "maps"),
            (Include.PARENTS, "parents"),
            (Include.PATHS, "paths"),
            (Include.PROPERTIES, "properties"),
            (Include.ROLES, "roles"),
            (Include.SYNONYMS, "synonyms"),
        ]
        
        for enum_value, expected_string in includes:
            assert to_url_value(enum_value) == expected_string
