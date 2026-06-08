"""Search concepts tool for NCI EVS API."""

from typing import Any

import httpx
from fastmcp import FastMCP

from ..models import (
    ConceptStatus,
    Include,
    NCIMDefinitionSource,
    NCIMProperty,
    NCIMSynonymSource,
    NCIMSynonymTermType,
    NCITDefinitionSource,
    NCITProperty,
    NCITSynonymSource,
    NCITSynonymTermType,
    SearchType,
    Terminology,
)
from ..utils import to_url_value


def register(mcp: FastMCP) -> None:
    """Register the search_concepts tool with the MCP server."""
    
    @mcp.tool(
        name="search_concepts",
        annotations={
            "title": "Search Concepts EVS Tool",
            "readOnlyHint": True,
        }
    )
    async def search_concepts(
        term: str,
        terminology: Terminology = Terminology.NCIT,
        type: SearchType = SearchType.CONTAINS,
        include: Include = Include.MINIMAL,
        conceptStatus: ConceptStatus | None = None,
        property: str | None = None,
        value: str | None = None,
        definitionSource: str | None = None,
        definitionType: str | None = None,
        synonymSource: str | None = None,
        synonymType: str | None = None,
        synonymTermType: str | None = None,
        subset: str | None = None,
        sort: str | None = None,
        ascending: bool = True,
        fromRecord: int = 0,
        pageSize: int = 10,
    ) -> dict[str, Any]:
        """Search for concepts in the NCI EVS API.
        
        Provides flexible search capabilities ranging from simple term searches to
        complex queries with filters, sorting, and paging.
        
        Args:
            term: The term, phrase, or code to search for (e.g., 'melanoma').
            terminology: Comma-separated list of terminologies to search
                        (e.g., 'ncit' or 'ncim'). Default: 'ncit'
            type: The match type for the search. Options:
                  - contains: Search for terms containing the query string
                  - match: Exact match search
                  - startsWith: Search for terms starting with the query string
                  - phrase: Phrase search - matches the exact phrase
                  - AND: Boolean AND search - all terms must be present
                  - OR: Boolean OR search - any term must be present
                  - fuzzy: Fuzzy search - matches similar terms
                  Default: 'contains'
            include: Level of detail to return. Can be a single value or comma-separated list.
                     Options: minimal, summary, full, associations, children, definitions,
                     disjointWith, history, inverseAssociations, inverseRoles, maps,
                     parents, properties, roles, synonyms.
                     Default: 'minimal'
            conceptStatus: Filter by concept status. Optional.
                          Options: Header_Concept, Retired_Concept, Obsolete_Concept,
                          Provisional_Concept, Concept_Pending_Approval.
                          NOTE: This parameter can ONLY be used when terminology is set to 'ncit'.
            property: Comma-separated list of property codes to restrict search results by.
                     Can be specified as code or name. Optional.
                     Examples:
                     - For ncit: 'P106,P322' or 'Semantic_Type,Contributing_Source'
                     - For ncim: 'COLOR,SHAPE' or property names
                     NOTE: NCITProperty codes can ONLY be used with terminology='ncit'.
                     NOTE: NCIMProperty codes can ONLY be used with terminology='ncim'.
                     This works with the 'value' parameter to find concepts with specific
                     property values. Using 'term' will further restrict results.
            value: A property value to restrict search results by. Optional.
                  NOTE: This parameter works with 'property' to find concepts having one of
                  the specified properties with an exact value matching this parameter.
                  Using 'term' will further restrict results to those also matching the term.
                  Example: property='P322', value='CDISC' finds concepts with Contributing_Source='CDISC'
            definitionSource: Comma-separated list of definition sources to restrict results by. Optional.
                             Can be specified using source codes.
                             Examples:
                             - For ncit: 'NCI,CDISC' or NCITDefinitionSource.NCI
                             - For ncim: 'NCI,MSH' or NCIMDefinitionSource.NCI
                             NOTE: NCITDefinitionSource values can ONLY be used with terminology='ncit'.
                             NOTE: NCIMDefinitionSource values can ONLY be used with terminology='ncim'.
            definitionType: Comma-separated list of definition types to restrict results by. Optional.
                           Examples:
                           - For ncit: 'DEFINITION,ALT_DEFINITION'
                           Common types: DEFINITION, ALT_DEFINITION
            synonymSource: Comma-separated list of synonym sources to restrict results by. Optional.
                          Examples:
                          - For ncit: 'NCI,CDISC,FDA' or NCITSynonymSource values
                          - For ncim: 'NCI,MSH,SNOMEDCT_US' or NCIMSynonymSource values
                          NOTE: NCITSynonymSource values can ONLY be used with terminology='ncit'.
                          NOTE: NCIMSynonymSource values can ONLY be used with terminology='ncim'.
            synonymType: Comma-separated list of synonym types to restrict results by. Optional.
                        Examples:
                        - For ncit: 'FULL_SYN', 'Display_Name', 'Preferred_Name', or 'P90,P107,P108'
                        NOTE: This parameter is ONLY meaningful for terminology='ncit'.
                        Available types: P90 (FULL_SYN), P107 (Display_Name), P108 (Preferred_Name)
            synonymTermType: Comma-separated list of synonym term types to restrict results by. Optional.
                            Examples:
                            - For ncit: 'PT,SY,AB' or NCITSynonymTermType values
                            - For ncim: 'PT,SY,AB' or NCIMSynonymTermType values
                            NOTE: NCITSynonymTermType values can ONLY be used with terminology='ncit'.
                            NOTE: NCIMSynonymTermType values can ONLY be used with terminology='ncim'.
                            This allows filtering by specific term types like Preferred Term (PT), Synonym (SY), etc.
            subset: Comma-separated list of subset codes to restrict search results by. Optional.
                   Examples: 'C157225' or 'C157225,C157226'
                   Special value: '*' returns results that participate in at least one subset.
                   NOTE: This parameter is ONLY meaningful for terminology='ncit'.
            sort: The search parameter to sort results by. Optional.
            ascending: Sort ascending (if True) or descending (if False). Default: True
            fromRecord: Start index of the search results (for pagination). Default: 0
            pageSize: Maximum number of results to return. Default: 10
        
        Returns:
            Dictionary containing search results with the following structure:
            - total: Total number of results
            - parameters: Search parameters used
            - concepts: List of matching concept objects
        
        Raises:
            httpx.HTTPStatusError: If the API request fails.
        
        Examples:
            Simple search:
            >>> search_concepts(term="melanoma")
            
            Search with filters:
            >>> search_concepts(
            ...     term="cancer",
            ...     terminology="ncit",
            ...     type=SearchType.STARTS_WITH,
            ...     include=Include.SUMMARY,
            ...     pageSize=20
            ... )
        """
        base_url = "https://api-evsrest.nci.nih.gov/api/v1"
        url = f"{base_url}/concept/search"
        
        params = {
            "term": term,
            "terminology": to_url_value(terminology),
            "type": to_url_value(type),
            "include": to_url_value(include),
            "ascending": str(ascending).lower(),
            "fromRecord": fromRecord,
            "pageSize": pageSize,
        }
        
        # Add optional parameters if provided
        if conceptStatus is not None:
            params["conceptStatus"] = to_url_value(conceptStatus)
        
        if property is not None:
            # Handle both enum values and strings for property parameter
            params["property"] = to_url_value(property) if hasattr(property, 'value') else property
        
        if value is not None:
            params["value"] = value
        
        if definitionSource is not None:
            # Handle both enum values and strings for definitionSource parameter
            params["definitionSource"] = to_url_value(definitionSource) if hasattr(definitionSource, 'value') else definitionSource
        
        if definitionType is not None:
            params["definitionType"] = definitionType
        
        if synonymSource is not None:
            # Handle both enum values and strings for synonymSource parameter
            params["synonymSource"] = to_url_value(synonymSource) if hasattr(synonymSource, 'value') else synonymSource
        
        if synonymType is not None:
            params["synonymType"] = synonymType
        
        if synonymTermType is not None:
            # Handle both enum values and strings for synonymTermType parameter
            params["synonymTermType"] = to_url_value(synonymTermType) if hasattr(synonymTermType, 'value') else synonymTermType
        
        if subset is not None:
            params["subset"] = subset
        
        if sort is not None:
            params["sort"] = sort
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            return response.json()
