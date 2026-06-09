"""
EVS MCP Tools

This module provides tools for interacting with the NCI EVS API,
allowing searches, summaries, and analysis of NCI terminology.
"""

from . import (
    get_children,
    get_concepts,
    get_descendants,
    get_parents,
    search_concepts,
)


def register_tools(mcp):
    """Register all EVS tools with the MCP server."""
    get_children.register(mcp)
    get_concepts.register(mcp)
    get_descendants.register(mcp)
    get_parents.register(mcp)
    search_concepts.register(mcp)
