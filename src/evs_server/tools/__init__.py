"""
EVS MCP Tools

This module provides tools for interacting with the NCI EVS API,
allowing searches, summaries, and analysis of NCI terminology.
"""

from . import (
    get_concepts,
    search_concepts,
)


def register_tools(mcp):
    """Register all EVS tools with the MCP server."""
    get_concepts.register(mcp)
    search_concepts.register(mcp)
