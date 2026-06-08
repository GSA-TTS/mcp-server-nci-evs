"""NCI Thesaurus synonym term type enumeration."""

from enum import Enum


class NCITSynonymTermType(str, Enum):
    """Enumeration of NCI Thesaurus (ncit) synonym term types.
    
    Note: This parameter can only be used when terminology is set to 'ncit'.
    """

    AB = "AB"
    """Abbreviation"""

    AD = "AD"
    """Adjectival form (and other parts of grammar)"""

    AQ = "AQ"
    """*Antiquated preferred term"""

    AQS = "AQS"
    """Antiquated term, use when there are antiquated synonyms within a concept"""

    BR = "BR"
    """US brand name, which may be trademarked"""

    CA2 = "CA2"
    """ISO 3166 alpha-2 country code"""

    CA3 = "CA3"
    """ISO 3166 alpha-3 country code"""

    CI = "CI"
    """ISO country code"""

    CN = "CN"
    """Drug study code"""

    CNU = "CNU"
    """ISO 3166 numeric country code"""

    CS = "CS"
    """US State Department country code"""

    DN = "DN"
    """Display name"""

    FB = "FB"
    """Foreign brand name, which may be trademarked"""

    HD = "HD"
    """*Header (groups concepts, but not used for coding data)"""

    HT = "HT"
    """Hierarchical term"""

    LLT = "LLT"
    """Lower level term"""

    PT = "PT"
    """*Preferred term"""

    RT = "RT"
    """Related term"""

    SN = "SN"
    """Chemical structure name"""

    SY = "SY"
    """Synonym"""
