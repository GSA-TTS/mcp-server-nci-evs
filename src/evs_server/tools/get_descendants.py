"""Get descendant concepts tool for NCI EVS API."""

from typing import Any, Annotated

import httpx
from fastmcp import FastMCP

from ..models import Terminology
from ..utils import to_url_value


def register(mcp: FastMCP) -> None:
    """Register the get_descendants tool with the MCP server."""
    
    @mcp.tool(
        name="get_descendants",
        annotations={
            "title": "Get Descendant Concepts EVS Tool",
            "readOnlyHint": True,
        }
    )
    async def get_descendants(
        terminology: Annotated[Terminology, "Terminology to search in. Note: This endpoint is only meaningful for 'ncit'."],
        code: Annotated[str, "Concept code in the specified terminology. Example: 'C3224' for ncit"],
        fromRecord: Annotated[int, "Start index of the search results (for pagination). Default: 0"] = 0,
        pageSize: Annotated[int, "Maximum number of results to return. Default: 50000"] = 50000,
        maxLevel: Annotated[int, "Maximum hierarchical level of descendants to return. Default: 10000"] = 10000,
    ) -> dict[str, Any]:
        """Get all descendant concepts for the specified terminology and code.
        
        Retrieves all descendant concepts (children, grandchildren, etc.) of a given concept
        in the hierarchical terminology structure. Unlike get_children which returns only
        direct children, this returns the entire descendant tree up to the specified maxLevel.
        
        Important: This endpoint is primarily designed for NCIT terminology.
        
        Args:
            terminology: Terminology to search in. This call is only meaningful for 'ncit'.
            code: Concept code in the specified terminology.
                  Example: 'C3224' (Melanoma in NCIT)
            fromRecord: Start index for pagination. Use this to retrieve results in batches.
                        Default: 0
            pageSize: Maximum number of results to return per request. Use with fromRecord
                      for pagination of large result sets. Default: 50000
            maxLevel: Maximum hierarchical depth to traverse. Controls how many levels down
                      the hierarchy to retrieve. Default: 10000
        
        Returns:
            Dictionary containing:
            - descendants: List of descendant concept objects
            - count: Number of descendants returned in this response
            - parameters: The parameters used in the query
        
        Raises:
            httpx.HTTPStatusError: If the API request fails (e.g., concept not found,
                                   invalid terminology).
        
        Examples:
            Get all descendants of a concept:
            >>> get_descendants(terminology="ncit", code="C3224")
            
            Get descendants with pagination (first 100):
            >>> get_descendants(
            ...     terminology="ncit",
            ...     code="C3224",
            ...     fromRecord=0,
            ...     pageSize=100
            ... )
            
            Limit descendants to 3 levels deep:
            >>> get_descendants(
            ...     terminology="ncit",
            ...     code="C3224",
            ...     maxLevel=3
            ... )
        
        Notes:
            - This returns ALL descendants at all levels (not just immediate children)
            - Use maxLevel to control depth and avoid retrieving too many concepts
            - Use pageSize and fromRecord for pagination on large result sets
            - For only direct children, use the get_children tool instead
            - For parent concepts, use the get_ancestors or get_parents tools
        """
        base_url = "https://api-evsrest.nci.nih.gov/api/v1"
        url = f"{base_url}/concept/{to_url_value(terminology)}/{code}/descendants"
        
        params = {
            "fromRecord": fromRecord,
            "pageSize": pageSize,
            "maxLevel": maxLevel,
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
            # Wrap list response in a dict for MCP compatibility
            if isinstance(data, list):
                return {
                    "descendants": data,
                    "count": len(data),
                    "parameters": {
                        "terminology": to_url_value(terminology),
                        "code": code,
                        "fromRecord": fromRecord,
                        "pageSize": pageSize,
                        "maxLevel": maxLevel,
                    }
                }
            return data
