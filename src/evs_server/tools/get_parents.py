"""Get parent concepts tool for NCI EVS API."""

from typing import Any, Annotated

import httpx
from fastmcp import FastMCP

from ..models import Terminology
from ..utils import to_url_value


def register(mcp: FastMCP) -> None:
    """Register the get_parents tool with the MCP server."""
    
    @mcp.tool(
        name="get_parents",
        annotations={
            "title": "Get Parent Concepts EVS Tool",
            "readOnlyHint": True,
        }
    )
    async def get_parents(
        terminology: Annotated[Terminology, "Terminology to search in (e.g., 'ncit' or 'ncim')"],
        code: Annotated[str, "Concept code in the specified terminology. Examples: 'C3224' for ncit, 'C0025202' for ncim"],
    ) -> dict[str, Any]:
        """Get parent concepts for the specified terminology and code.
        
        Retrieves all direct parent concepts (immediate ancestors) of a given concept
        in the hierarchical terminology structure.
        
        Args:
            terminology: Terminology to search in (e.g., 'ncit' or 'ncim').
            code: Concept code in the specified terminology.
                  Examples:
                  - For ncit: 'C3224' (Melanoma)
                  - For ncim: 'C0025202' (Melanoma)
        
        Returns:
            Dictionary containing:
            - parents: List of parent concept objects
            - count: Number of parents returned
            - parameters: The parameters used in the query
            
            Each parent object contains basic concept information including code, name, 
            and terminology. Returns empty list in 'parents' if the concept has no parents
            (i.e., it's a root concept).
        
        Raises:
            httpx.HTTPStatusError: If the API request fails (e.g., concept not found,
                                   invalid terminology).
        
        Examples:
            Get parents of a specific NCIT concept:
            >>> get_parents(terminology="ncit", code="C3224")
            
            Get parents of a specific NCIM concept:
            >>> get_parents(terminology="ncim", code="C0025202")
        
        Notes:
            - This returns only direct parents (one level up in the hierarchy)
            - For child concepts, use the get_children tool
            - For all ancestors, use the get_ancestors tool
            - Root concepts will return an empty list of parents
            - For full hierarchical information, use get_concepts with include="parents"
              or include="full"
        """
        base_url = "https://api-evsrest.nci.nih.gov/api/v1"
        url = f"{base_url}/concept/{to_url_value(terminology)}/{code}/parents"
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            
            # Wrap list response in a dict for MCP compatibility
            if isinstance(data, list):
                return {
                    "parents": data,
                    "count": len(data),
                    "parameters": {
                        "terminology": to_url_value(terminology),
                        "code": code,
                    }
                }
            return data
