"""Tests for ConceptStatus enum."""

import pytest

from evs_server.models import ConceptStatus
from evs_server.utils import to_url_value


class TestConceptStatus:
    """Test suite for the ConceptStatus enum."""

    def test_concept_status_values(self):
        """Test that all ConceptStatus enum values convert correctly."""
        statuses = [
            (ConceptStatus.HEADER_CONCEPT, "Header_Concept"),
            (ConceptStatus.RETIRED_CONCEPT, "Retired_Concept"),
            (ConceptStatus.OBSOLETE_CONCEPT, "Obsolete_Concept"),
            (ConceptStatus.PROVISIONAL_CONCEPT, "Provisional_Concept"),
            (ConceptStatus.CONCEPT_PENDING_APPROVAL, "Concept_Pending_Approval"),
        ]
        
        for enum_value, expected_string in statuses:
            assert to_url_value(enum_value) == expected_string

    def test_concept_status_count(self):
        """Test that ConceptStatus has exactly 5 values."""
        assert len(ConceptStatus) == 5

    def test_concept_status_in_params(self):
        """Test that ConceptStatus works correctly in URL params construction."""
        from evs_server.models import Terminology, SearchType, Include
        
        params = {
            "term": "melanoma",
            "terminology": to_url_value(Terminology.NCIT),
            "type": to_url_value(SearchType.CONTAINS),
            "include": to_url_value(Include.MINIMAL),
            "conceptStatus": to_url_value(ConceptStatus.RETIRED_CONCEPT),
        }
        
        assert params["conceptStatus"] == "Retired_Concept"
        assert params["terminology"] == "ncit"

    def test_concept_status_string_base(self):
        """Test that ConceptStatus inherits from str."""
        assert isinstance(ConceptStatus.HEADER_CONCEPT, str)
        assert isinstance(ConceptStatus.RETIRED_CONCEPT.value, str)

    def test_all_concept_statuses_have_correct_format(self):
        """Test that all status values follow the correct naming pattern."""
        for status in ConceptStatus:
            # All values should contain an underscore and end with _Concept or _Approval
            assert "_" in status.value
            assert status.value.endswith("_Concept") or status.value.endswith("_Approval")
            
            # First letter after underscore should be capitalized
            parts = status.value.split("_")
            for part in parts:
                assert part[0].isupper(), f"{status.value} part '{part}' should start with uppercase"
