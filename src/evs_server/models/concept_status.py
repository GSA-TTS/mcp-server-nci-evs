"""NCI EVS Concept Status enumeration."""

from enum import Enum


class ConceptStatus(str, Enum):
    """Enumeration of concept status values for filtering concepts.
    
    Note: This parameter can only be used when terminology is set to 'ncit'.
    """

    HEADER_CONCEPT = "Header_Concept"
    """Header concept status"""

    RETIRED_CONCEPT = "Retired_Concept"
    """Retired concept status"""

    OBSOLETE_CONCEPT = "Obsolete_Concept"
    """Obsolete concept status"""

    PROVISIONAL_CONCEPT = "Provisional_Concept"
    """Provisional concept status"""

    CONCEPT_PENDING_APPROVAL = "Concept_Pending_Approval"
    """Concept pending approval status"""
