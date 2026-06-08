"""Tests for NCI Thesaurus definition source enum."""

import pytest

from evs_server.models import NCITDefinitionSource
from evs_server.utils import to_url_value


class TestNCITDefinitionSource:
    """Test suite for the NCITDefinitionSource enum."""

    def test_definition_source_values(self):
        """Test that common NCITDefinitionSource enum values convert correctly."""
        sources = [
            (NCITDefinitionSource.NCI, "NCI"),
            (NCITDefinitionSource.CDISC, "CDISC"),
            (NCITDefinitionSource.FDA, "FDA"),
            (NCITDefinitionSource.CTCAE, "CTCAE"),
            (NCITDefinitionSource.NICHD, "NICHD"),
            (NCITDefinitionSource.WHO, "WHO"),
        ]
        
        for enum_value, expected_string in sources:
            assert to_url_value(enum_value) == expected_string

    def test_definition_source_count(self):
        """Test that NCITDefinitionSource has exactly 37 values."""
        assert len(NCITDefinitionSource) == 37

    def test_definition_source_with_special_chars(self):
        """Test definition sources with special characters convert correctly."""
        assert to_url_value(NCITDefinitionSource.ACC_AHA) == "ACC/AHA"
        assert to_url_value(NCITDefinitionSource.CDISC_GLOSS) == "CDISC-GLOSS"
        assert to_url_value(NCITDefinitionSource.NCI_GLOSS) == "NCI-GLOSS"
        assert to_url_value(NCITDefinitionSource.DIPG_DMG) == "DIPG/DMG"
        assert to_url_value(NCITDefinitionSource.FDA_NIH_MORE) == "FDA-NIH-MoRE"

    def test_definition_source_with_versions(self):
        """Test definition sources with version numbers."""
        assert to_url_value(NCITDefinitionSource.BRIDG_3_0_3) == "BRIDG 3.0.3"
        assert to_url_value(NCITDefinitionSource.BRIDG_5_3) == "BRIDG 5.3"
        assert to_url_value(NCITDefinitionSource.CTCAE_3_0) == "CTCAE 3.0"
        assert to_url_value(NCITDefinitionSource.CTCAE_5_0) == "CTCAE 5.0"
        assert to_url_value(NCITDefinitionSource.CTCAE_6_0) == "CTCAE 6.0"

    def test_definition_source_string_base(self):
        """Test that NCITDefinitionSource inherits from str."""
        assert isinstance(NCITDefinitionSource.NCI, str)
        assert isinstance(NCITDefinitionSource.CDISC.value, str)

    def test_comma_separated_sources(self):
        """Test creating comma-separated list of definition sources."""
        sources = f"{to_url_value(NCITDefinitionSource.NCI)},{to_url_value(NCITDefinitionSource.CDISC)}"
        assert sources == "NCI,CDISC"

    def test_all_sources_are_uppercase_or_mixed(self):
        """Test that all source codes follow naming conventions."""
        for source in NCITDefinitionSource:
            # Values should not be all lowercase
            assert not source.value.islower(), f"{source.value} should not be all lowercase"
