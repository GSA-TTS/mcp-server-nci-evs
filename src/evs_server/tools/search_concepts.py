"""Search concepts tool for NCI EVS API."""

from typing import Any, Annotated, Literal 
from pydantic import Field 

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
from ..utils import to_enum_list_value, to_url_value, validate_enum_for_terminology


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
        term: Annotated[str, "The term, phrase, or code to search for (e.g., 'melanoma')."],
        terminology: Annotated[Terminology, "The terminology to search within. Can be a single value or comma-separated list (e.g., 'ncit' or 'ncit,ncim'). Default: 'ncit'"] = Terminology.NCIT,
        type: Annotated[SearchType, "The match type for the search."] = SearchType.CONTAINS,
        include: Annotated[Include, "The level of detail to return."] = Include.MINIMAL,
        conceptStatus: Annotated[ConceptStatus, "Filter by concept status. Only use when terminology is ncit."] = None,
        property: Annotated[NCITProperty | NCIMProperty | None, "Property enum to restrict search results by. Only use NCITProperty values when terminology is 'ncit' and NCIMProperty values when terminology is 'ncim'."] = None,
        value: Annotated[str, "A property value to restrict search results by."] = None,
        definitionSource: Annotated[NCITDefinitionSource | NCIMDefinitionSource | None, "Definition source enum to restrict search results by. Can be NCITDefinitionSource (for ncit) or NCIMDefinitionSource (for ncim)."] = None,
        definitionType: Annotated[
            Literal["DEFINITION", "ALT_DEFINITION"] | None,
            "Definition types to restrict search results by. Only use when terminology is ncit",
        ] = None,
        synonymSource: Annotated[
            NCITSynonymSource | NCIMSynonymSource | None,
            "Single synonym source enum to restrict results by. Use NCITSynonymSource values when terminology is 'ncit' and NCIMSynonymSource values when terminology is 'ncim'."
        ] = None,
        synonymType: Annotated[
            Literal["FULL_SYN", "Display_Name", "Preferred_Name"] | None,
            "Comma-separated list of synonym types to restrict results by. Only use when terminology is 'ncit'."
        ] = None,
        synonymTermType: Annotated[
            NCITSynonymTermType | NCIMSynonymTermType | None,
            "Synonym term type to restrict results by. Use NCITSynonymTermType values when terminology is 'ncit' and NCIMSynonymTermType values when terminology is 'ncim'."
        ] = None, 
        subset: Annotated[str | None, "Comma-separated list of subsets to restrict search results by, e.g. 'C157225'. The value '*' can also be used to return results that participate in at least one subset. This parameter is only meaningful for terminology=ncit"] = None,
        sort: Annotated[str | None, "The search parameter to sort results by. Optional."] = None,
        ascending: Annotated[bool, "Sort ascending (if True) or descending (if False). Default: True"] = True,
        fromRecord: Annotated[int, "Start index of the search results (for pagination). Default: 0"] = 0,
        pageSize: Annotated[int, "Maximum number of results to return. Default: 10"] = 10,
    ) -> dict[str, Any]:
        """Search for concepts in the NCI EVS API.
        
        Provides flexible search capabilities ranging from simple term searches to
        complex queries with filters, sorting, and paging.
        
        Property Reference:
            For detailed information about available property codes and their usage, refer to:
            - skill://ncit-property-information/SKILL.md (for terminology='ncit')
            - skill://ncim-property-information/SKILL.md (for terminology='ncim')
            
            These skills provide comprehensive documentation of all property codes, organized by
            category (e.g., Gene and Molecular Biology, Chemical and Drug Information, Clinical
            Coding, etc.) with descriptions and usage examples.
        
        Arg Notes:
            property and value: These parameters work together to filter search results based on specific property values.
                     - 'property' specifies which property or properties to filter by (e.g., Semantic_Type, Display_Name, etc.).
                     - 'value' specifies the exact value that the property should match (e.g., 'Disease', 'Melanoma', etc.).
                     - When both are used together, the search will return concepts that have the specified property with an exact value match.
                     - Using 'term' in combination with 'property' and 'value' will further restrict results to those that also match the search term.
                     - To find the right property code to use, consult the property information skills listed above.
        
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
        
        # Get terminology value for validation
        terminology_value = to_url_value(terminology)
        
        params = {
            "term": term,
            "terminology": terminology_value,
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
            # Validate terminology-specific enum usage
            validate_enum_for_terminology(
                property,
                terminology_value,
                NCITProperty,
                NCIMProperty,
                "property"
            )
            # Convert enum or list of enums to comma-separated string
            # Determine which enum class to use based on the actual type
            if isinstance(property, list):
                enum_class = property[0].__class__ if property else NCITProperty
            else:
                enum_class = property.__class__
            params["property"] = to_enum_list_value(property, enum_class, "property")
        
        if value is not None:
            params["value"] = value
        
        if definitionSource is not None:
            # Validate terminology-specific enum usage
            validate_enum_for_terminology(
                definitionSource,
                terminology_value,
                NCITDefinitionSource,
                NCIMDefinitionSource,
                "definitionSource"
            )
            # Convert enum or list of enums to comma-separated string
            if isinstance(definitionSource, list):
                enum_class = definitionSource[0].__class__ if definitionSource else NCITDefinitionSource
            else:
                enum_class = definitionSource.__class__
            params["definitionSource"] = to_enum_list_value(definitionSource, enum_class, "definitionSource")
        
        if definitionType is not None:
            params["definitionType"] = definitionType
        
        if synonymSource is not None:
            # Validate terminology-specific enum usage
            validate_enum_for_terminology(
                synonymSource,
                terminology_value,
                NCITSynonymSource,
                NCIMSynonymSource,
                "synonymSource"
            )
            # Convert enum or list of enums to comma-separated string
            if isinstance(synonymSource, list):
                enum_class = synonymSource[0].__class__ if synonymSource else NCITSynonymSource
            else:
                enum_class = synonymSource.__class__
            params["synonymSource"] = to_enum_list_value(synonymSource, enum_class, "synonymSource")
        
        if synonymType is not None:
            params["synonymType"] = synonymType
        
        if synonymTermType is not None:
            # Validate terminology-specific enum usage
            validate_enum_for_terminology(
                synonymTermType,
                terminology_value,
                NCITSynonymTermType,
                NCIMSynonymTermType,
                "synonymTermType"
            )
            # Convert enum or list of enums to comma-separated string
            if isinstance(synonymTermType, list):
                enum_class = synonymTermType[0].__class__ if synonymTermType else NCITSynonymTermType
            else:
                enum_class = synonymTermType.__class__
            params["synonymTermType"] = to_enum_list_value(synonymTermType, enum_class, "synonymTermType")
        
        if subset is not None:
            params["subset"] = subset
        
        if sort is not None:
            params["sort"] = sort
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            return response.json()
