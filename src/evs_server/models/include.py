"""NCI EVS Include parameter enumeration."""

from enum import Enum


class Include(str, Enum):
    """Enumeration of include parameter values for controlling API response detail.
    
    Values can be combined as comma-separated lists (e.g., "summary,roles").
    The "minimal" information is always included regardless of the parameter value.
    """

    # Special Include Values
    MINIMAL = "minimal"
    """Concept level information only: code, name, terminology, version, leaf, and active fields"""

    SUMMARY = "summary"
    """Minimal information plus synonyms, definitions, and properties.
    Equivalent to: "synonyms,definitions,properties"
    """

    FULL = "full"
    """All available concept parts except descendants and paths"""

    # Concept Part Include Values
    ASSOCIATIONS = "associations"
    """Include associations"""

    CHILDREN = "children"
    """Include children"""

    DEFINITIONS = "definitions"
    """Include definitions"""

    DESCENDANTS = "descendants"
    """Include concept descendants (Warning: may return large amounts of data)"""

    DISJOINT_WITH = "disjointWith"
    """Include "disjoint with" associations"""

    HISTORY = "history"
    """Include history"""

    INVERSE_ASSOCIATIONS = "inverseAssociations"
    """Include inverse associations"""

    INVERSE_ROLES = "inverseRoles"
    """Include inverse roles"""

    MAPS = "maps"
    """Include maps"""

    PARENTS = "parents"
    """Include parents"""

    PATHS = "paths"
    """Include all paths to root concept (Warning: may return large amounts of data)"""

    PROPERTIES = "properties"
    """Include properties"""

    ROLES = "roles"
    """Include roles"""

    SYNONYMS = "synonyms"
    """Include synonyms"""
