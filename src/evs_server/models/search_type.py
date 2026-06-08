"""NCI EVS Search Type enumeration."""

from enum import Enum


class SearchType(str, Enum):
    """Enumeration of search type values for controlling search behavior.
    
    These values determine how the search query is matched against concepts
    in the NCI EVS API.
    """

    CONTAINS = "contains"
    """Search for terms containing the query string"""

    MATCH = "match"
    """Exact match search"""

    STARTS_WITH = "startsWith"
    """Search for terms starting with the query string"""

    PHRASE = "phrase"
    """Phrase search - matches the exact phrase"""

    AND = "AND"
    """Boolean AND search - all terms must be present"""

    OR = "OR"
    """Boolean OR search - any term must be present"""

    FUZZY = "fuzzy"
    """Fuzzy search - matches similar terms with spelling variations"""
