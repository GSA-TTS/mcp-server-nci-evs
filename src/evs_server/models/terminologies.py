"""NCI EVS Terminology enumeration."""

from enum import Enum


class Terminology(str, Enum):
    """Enumeration of available terminologies in NCI EVS."""

    NCIT = "ncit"
    """NCI Thesaurus"""

    NCIM = "ncim"
    """NCI Metathesaurus"""

    CANMED = "canmed"
    """CanMED"""

    CHEBI = "chebi"
    """Chemical Entities of Biological Interest"""

    CTCAE5 = "ctcae5"
    """CTCAE 5"""

    DUO = "duo"
    """Data Use Ontology"""

    GO = "go"
    """Gene Ontology"""

    HGNC = "hgnc"
    """HUGO Gene Nomenclature Committee"""

    HL7V30 = "hl7v30"
    """Health Level 7 Vocabulary (V3)"""

    ICD10 = "icd10"
    """International Classification of Diseases, Tenth Revision"""

    ICD10CM = "icd10cm"
    """The International Classification of Diseases, Tenth Revision, Clinical Modification"""

    ICD9CM = "icd9cm"
    """The International Classification of Diseases, Ninth Revision, Clinical Modification"""

    LOINC = "loinc"
    """Logical Observation Identifier Names and Codes"""

    MA = "ma"
    """Mouse Anatomy: Anatomical Dictionary for the Adult Mouse"""

    MDR = "mdr"
    """Medical Dictionary for Regulatory Activities"""

    MEDRT = "medrt"
    """MED-RT"""

    MGED = "mged"
    """Microarray Gene Expression Data Ontology"""

    NDFRT = "ndfrt"
    """National Drug File Reference Terminology"""

    NPO = "npo"
    """NanoParticle Ontology"""

    OBI = "obi"
    """Ontology for Biomedical Investigations"""

    OBIB = "obib"
    """The ontology for Biobanking"""

    PDQ = "pdq"
    """Physician Data Query"""

    RADLEX = "radlex"
    """Radiology Lexicon"""

    SNOMEDCT_US = "snomedct_us"
    """SNOMED Clinical Terms"""

    UMLSSEMNET = "umlssemnet"
    """UMLS Semantic Network: UMLS Semantic Network"""

    ZFA = "zfa"
    """Zebrafish Model Organism Database"""
