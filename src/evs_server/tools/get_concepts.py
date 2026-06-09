from typing import Any

import httpx
from fastmcp import FastMCP

from ..models import Include, Terminology
from ..utils import to_url_value


def register(mcp: FastMCP) -> None:
    """Register the get_concepts tool with the MCP server."""
    
    @mcp.tool(
        name="get_concepts",
        annotations={
            "title": "Get Concepts EVS Tool",
            "readOnlyHint": True, 
        }
    )
    async def get_concepts(
        terminology: Terminology,
        list: str,
        include: Include = Include.MINIMAL,
    ) -> list[dict[str, Any]]:
        """Get concepts specified by list parameter.
        
        Retrieves detailed information about one or more concepts from the NCI EVS API.
        
        Property Reference:
            When include='properties' or include='full', the response will contain property information
            for each concept. To understand what properties are available and their meanings, refer to:
            - skill://ncit-property-information/SKILL.md (for terminology='ncit')
            - skill://ncim-property-information/SKILL.md (for terminology='ncim')
        
        Args:
            terminology: Terminology to search in (e.g., 'ncit' or 'ncim').
            list: Comma-separated list of concept codes to retrieve.
                  Examples:
                  - For ncit: 'C2291,C3224'
                  - For ncim: 'C0010137,C0025202'
            include: Level of detail to return. Can be a single value or comma-separated list.
                     Options: minimal, summary, full, associations, children, definitions,
                     disjointWith, history, inverseAssociations, inverseRoles, maps,
                     parents, properties, roles, synonyms.
                     Default: 'minimal'
        
        Returns:
            List of concept objects with details based on the include parameter.
            When include='properties', each concept will contain a 'properties' array with
            property code, value, and type information.
        
        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        base_url = "https://api-evsrest.nci.nih.gov/api/v1"
        url = f"{base_url}/concept/{to_url_value(terminology)}"
        
        params = {
            "list": list,
            "include": to_url_value(include),
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            return response.json()