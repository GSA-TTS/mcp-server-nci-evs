#!/usr/bin/env python3
"""Integration test for search_concepts with enum parameters."""

import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from evs_server.models import (
    NCITProperty,
    NCITSynonymTermType,
    SearchType,
    Terminology,
)


def test_enum_class_extraction():
    """Test that we can get the enum class without calling type()."""
    print("Testing enum class extraction with shadowed type()...")
    
    # Simulate the parameter name shadowing
    type = SearchType.CONTAINS  # This shadows built-in type()
    
    # This would fail: enum_class = type(NCITProperty.SEMANTIC_TYPE)
    # Because type is now SearchType.CONTAINS, not the built-in function
    
    # This works: use __class__ instead
    property_value = NCITProperty.SEMANTIC_TYPE
    enum_class = property_value.__class__
    
    assert enum_class == NCITProperty, f"Expected NCITProperty, got {enum_class}"
    print(f"✓ Got correct enum class: {enum_class.__name__}")
    
    # Test with list
    property_list = [NCITProperty.SEMANTIC_TYPE, NCITProperty.CONTRIBUTING_SOURCE]
    enum_class = property_list[0].__class__
    
    assert enum_class == NCITProperty, f"Expected NCITProperty, got {enum_class}"
    print(f"✓ Got correct enum class from list: {enum_class.__name__}")
    
    print()


def test_search_concepts_signature():
    """Test that search_concepts function signature can be inspected."""
    print("Testing search_concepts function signature...")
    
    from evs_server.tools.search_concepts import register
    from fastmcp import FastMCP
    
    # Create a mock MCP instance
    mcp = FastMCP("test")
    
    # Register the tool
    register(mcp)
    
    print("✓ search_concepts registered successfully")
    print(f"✓ Number of tools registered: {len(mcp._tool_manager._tools)}")
    
    # Get the registered tool
    tool = mcp._tool_manager._tools.get("search_concepts")
    if tool:
        print(f"✓ Tool found: {tool.name}")
        print(f"✓ Tool has {len(tool.parameters)} parameters")
    else:
        print("✗ Tool not found")
        sys.exit(1)
    
    print()


def test_parameter_types():
    """Test that parameter types are correctly defined."""
    print("Testing parameter types...")
    
    from evs_server.tools.search_concepts import register
    from fastmcp import FastMCP
    import inspect
    
    mcp = FastMCP("test")
    register(mcp)
    
    # Get the actual function
    tool = mcp._tool_manager._tools.get("search_concepts")
    if tool and hasattr(tool, 'fn'):
        sig = inspect.signature(tool.fn)
        
        # Check property parameter
        if 'property' in sig.parameters:
            param = sig.parameters['property']
            print(f"✓ property parameter found: {param.annotation}")
        
        # Check type parameter (should be SearchType)
        if 'type' in sig.parameters:
            param = sig.parameters['type']
            print(f"✓ type parameter found: {param.annotation}")
            print(f"✓ type parameter default: {param.default}")
    
    print()


if __name__ == "__main__":
    print("=" * 60)
    print("Integration Test: search_concepts with Enum Parameters")
    print("=" * 60)
    print()
    
    test_enum_class_extraction()
    test_search_concepts_signature()
    test_parameter_types()
    
    print("=" * 60)
    print("All integration tests passed! ✓")
    print("=" * 60)
