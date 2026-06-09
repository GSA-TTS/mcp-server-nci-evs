#!/usr/bin/env python3
"""Test script for enum validation in search_concepts tool."""

import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from evs_server.models import (
    NCITProperty,
    NCIMProperty,
    NCITDefinitionSource,
    NCIMDefinitionSource,
    NCITSynonymSource,
    NCIMSynonymSource,
    NCITSynonymTermType,
    NCIMSynonymTermType,
    Terminology,
)
from evs_server.utils import to_enum_list_value, validate_enum_for_terminology


def test_to_enum_list_value():
    """Test the to_enum_list_value function."""
    print("Testing to_enum_list_value...")
    
    # Test single enum
    result = to_enum_list_value(NCITProperty.SEMANTIC_TYPE, NCITProperty, "property")
    assert result == "P106", f"Expected 'P106', got {result}"
    print("✓ Single enum value works")
    
    # Test list of enums
    result = to_enum_list_value(
        [NCITProperty.SEMANTIC_TYPE, NCITProperty.CONTRIBUTING_SOURCE],
        NCITProperty,
        "property"
    )
    assert result == "P106,P322", f"Expected 'P106,P322', got {result}"
    print("✓ List of enum values works")
    
    # Test None
    result = to_enum_list_value(None, NCITProperty, "property")
    assert result is None, f"Expected None, got {result}"
    print("✓ None value works")
    
    # Test wrong enum type (should raise TypeError)
    try:
        to_enum_list_value(NCIMProperty.CODE, NCITProperty, "property")
        print("✗ Should have raised TypeError for wrong enum type")
        sys.exit(1)
    except TypeError as e:
        print(f"✓ TypeError raised correctly: {e}")
    
    # Test empty list (should raise ValueError)
    try:
        to_enum_list_value([], NCITProperty, "property")
        print("✗ Should have raised ValueError for empty list")
        sys.exit(1)
    except ValueError as e:
        print(f"✓ ValueError raised correctly: {e}")
    
    print()


def test_validate_enum_for_terminology():
    """Test the validate_enum_for_terminology function."""
    print("Testing validate_enum_for_terminology...")
    
    # Test valid NCIT enum with ncit terminology
    try:
        validate_enum_for_terminology(
            NCITProperty.SEMANTIC_TYPE,
            "ncit",
            NCITProperty,
            NCIMProperty,
            "property"
        )
        print("✓ Valid NCIT enum with ncit terminology passes")
    except ValueError as e:
        print(f"✗ Should not have raised error: {e}")
        sys.exit(1)
    
    # Test valid NCIM enum with ncim terminology
    try:
        validate_enum_for_terminology(
            NCIMProperty.CODE,
            "ncim",
            NCITProperty,
            NCIMProperty,
            "property"
        )
        print("✓ Valid NCIM enum with ncim terminology passes")
    except ValueError as e:
        print(f"✗ Should not have raised error: {e}")
        sys.exit(1)
    
    # Test invalid NCIT enum with ncim terminology (should raise ValueError)
    try:
        validate_enum_for_terminology(
            NCITProperty.SEMANTIC_TYPE,
            "ncim",
            NCITProperty,
            NCIMProperty,
            "property"
        )
        print("✗ Should have raised ValueError for NCIT enum with ncim terminology")
        sys.exit(1)
    except ValueError as e:
        print(f"✓ ValueError raised correctly: {e}")
    
    # Test invalid NCIM enum with ncit terminology (should raise ValueError)
    try:
        validate_enum_for_terminology(
            NCIMProperty.CODE,
            "ncit",
            NCITProperty,
            NCIMProperty,
            "property"
        )
        print("✗ Should have raised ValueError for NCIM enum with ncit terminology")
        sys.exit(1)
    except ValueError as e:
        print(f"✓ ValueError raised correctly: {e}")
    
    # Test list of valid enums
    try:
        validate_enum_for_terminology(
            [NCITProperty.SEMANTIC_TYPE, NCITProperty.CONTRIBUTING_SOURCE],
            "ncit",
            NCITProperty,
            NCIMProperty,
            "property"
        )
        print("✓ Valid list of NCIT enums with ncit terminology passes")
    except ValueError as e:
        print(f"✗ Should not have raised error: {e}")
        sys.exit(1)
    
    # Test list with invalid enum
    try:
        validate_enum_for_terminology(
            [NCITProperty.SEMANTIC_TYPE, NCIMProperty.CODE],
            "ncit",
            NCITProperty,
            NCIMProperty,
            "property"
        )
        print("✗ Should have raised ValueError for mixed enum list")
        sys.exit(1)
    except ValueError as e:
        print(f"✓ ValueError raised correctly: {e}")
    
    # Test None (should pass)
    try:
        validate_enum_for_terminology(
            None,
            "ncit",
            NCITProperty,
            NCIMProperty,
            "property"
        )
        print("✓ None value passes validation")
    except ValueError as e:
        print(f"✗ Should not have raised error for None: {e}")
        sys.exit(1)
    
    print()


def test_all_enum_types():
    """Test all enum types that are now incorporated."""
    print("Testing all enum types...")
    
    # Test NCITDefinitionSource
    result = to_enum_list_value(NCITDefinitionSource.NCI, NCITDefinitionSource, "definitionSource")
    assert result == "NCI", f"Expected 'NCI', got {result}"
    print("✓ NCITDefinitionSource works")
    
    # Test NCIMDefinitionSource
    result = to_enum_list_value(NCIMDefinitionSource.MSH, NCIMDefinitionSource, "definitionSource")
    assert result == "MSH", f"Expected 'MSH', got {result}"
    print("✓ NCIMDefinitionSource works")
    
    # Test NCITSynonymSource
    result = to_enum_list_value(NCITSynonymSource.CDISC, NCITSynonymSource, "synonymSource")
    assert result == "CDISC", f"Expected 'CDISC', got {result}"
    print("✓ NCITSynonymSource works")
    
    # Test NCIMSynonymSource
    result = to_enum_list_value(NCIMSynonymSource.SNOMEDCT_US, NCIMSynonymSource, "synonymSource")
    assert result == "SNOMEDCT_US", f"Expected 'SNOMEDCT_US', got {result}"
    print("✓ NCIMSynonymSource works")
    
    # Test NCITSynonymTermType
    result = to_enum_list_value(NCITSynonymTermType.PT, NCITSynonymTermType, "synonymTermType")
    assert result == "PT", f"Expected 'PT', got {result}"
    print("✓ NCITSynonymTermType works")
    
    # Test NCIMSynonymTermType
    result = to_enum_list_value(NCIMSynonymTermType.SY, NCIMSynonymTermType, "synonymTermType")
    assert result == "SY", f"Expected 'SY', got {result}"
    print("✓ NCIMSynonymTermType works")
    
    print()


if __name__ == "__main__":
    print("=" * 60)
    print("Testing Enum Validation Utilities")
    print("=" * 60)
    print()
    
    test_to_enum_list_value()
    test_validate_enum_for_terminology()
    test_all_enum_types()
    
    print("=" * 60)
    print("All tests passed! ✓")
    print("=" * 60)
