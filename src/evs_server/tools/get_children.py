"""Get children concepts tool for NCI EVS API."""

from typing import Any, Annotated

import httpx
from fastmcp import FastMCP

from ..models import Terminology
from ..utils import to_url_value


def register(mcp: FastMCP) -> None:
    """Register the get_children tool with the MCP server."""
    
    @mcp.tool(
        name="get_children",
        annotations={
            "title": "Get Children Concepts EVS Tool",
            "readOnlyHint": True,
        }
    )
    async def get_children(
        terminology: Annotated[Terminology, "Terminology to search in (e.g., 'ncit' or 'ncim')"],
        code: Annotated[str, "Concept code in the specified terminology. Examples: 'C3224' for ncit, 'C0025202' for ncim"],
    ) -> list[dict[str, Any]]:
        """Get child concepts for the specified terminology and code.
        
        Retrieves all direct child concepts (immediate descendants) of a given concept
        in the hierarchical terminology structure.
        
        Returns:
            Dictionary containing:
            - children: List of child concept objects
            - count: Number of children returned
            - parameters: The parameters used in the query
            
            Each child object contains basic concept information including code, name, 
            and terminology. Returns empty list in 'children' if the concept has no children.
        
        Raises:
            httpx.HTTPStatusError: If the API request fails (e.g., concept not found,
                                   invalid terminology).
        
        Examples:
            Get children of a specific NCIT concept:
            >>> get_children(terminology="ncit", code="C3224")
            
            Get children of a specific NCIM concept:
            >>> get_children(terminology="ncim", code="C0025202")
        
        Notes:
            - This returns only direct children (one level down in the hierarchy)
            - For parent concepts, use the get_parents tool
            - For full hierarchical information, use get_concepts with include="children"
              or include="full"
        """
        base_url = "https://api-evsrest.nci.nih.gov/api/v1"
        url = f"{base_url}/concept/{to_url_value(terminology)}/{code}/children"
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            
            # Wrap list response in a dict for MCP compatibility
            if isinstance(data, list):
                return {
                    "children": data,
                    "count": len(data),
                    "parameters": {
                        "terminology": to_url_value(terminology),
                        "code": code,
                    }
                }
            return data
