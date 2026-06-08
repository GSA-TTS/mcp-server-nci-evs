"""NCI Thesaurus property codes enumeration."""

from enum import Enum


class NCITProperty(str, Enum):
    """Enumeration of NCI Thesaurus (ncit) property codes.
    
    Note: These properties can only be used when terminology is set to 'ncit'.
    Properties can be specified as code or name in API calls.
    """

    OMIM_NUMBER = "P100"
    """OMIM_Number"""

    HOMOLOGOUS_GENE = "P101"
    """Homologous_Gene"""

    GENBANK_ACCESSION_NUMBER = "P102"
    """GenBank_Accession_Number"""

    SEMANTIC_TYPE = "P106"
    """Semantic_Type"""

    DISPLAY_NAME = "P107"
    """Display_Name"""

    PREFERRED_NAME = "P108"
    """Preferred_Name"""

    IMAGE_LINK = "P167"
    """Image_Link"""

    PUBMEDID_PRIMARY_REFERENCE = "P171"
    """PubMedID_Primary_Reference"""

    NSC_NUMBER = "P175"
    """NSC Number"""

    OLD_PARENT = "P200"
    """OLD_PARENT"""

    OLD_CHILD = "P201"
    """OLD_CHILD"""

    OLD_KIND = "P203"
    """OLD_KIND"""

    OLD_ROLE = "P204"
    """OLD_ROLE"""

    UMLS_CUI = "P207"
    """UMLS_CUI"""

    NCI_META_CUI = "P208"
    """NCI_META_CUI"""

    CAS_REGISTRY = "P210"
    """CAS_Registry"""

    GO_ANNOTATION = "P211"
    """GO_Annotation"""

    KEGG_ID = "P215"
    """KEGG_ID"""

    BIOCARTA_ID = "P216"
    """BioCarta_ID"""

    ACCEPTED_THERAPEUTIC_USE_FOR = "P302"
    """Accepted_Therapeutic_Use_For"""

    CONCEPT_STATUS = "P310"
    """Concept_Status"""

    SNP_ID = "P315"
    """SNP_ID"""

    RELATIVE_ENZYME_ACTIVITY = "P316"
    """Relative_Enzyme_Activity"""

    FDA_TABLE = "P317"
    """FDA_Table"""

    FDA_UNII_CODE = "P319"
    """FDA_UNII_Code"""

    OID = "P320"
    """OID"""

    ENTREZGENE_ID = "P321"
    """EntrezGene_ID"""

    CONTRIBUTING_SOURCE = "P322"
    """Contributing_Source"""

    ALT_DEFINITION = "P325"
    """ALT_DEFINITION"""

    PDQ_OPEN_TRIAL_SEARCH_ID = "P329"
    """PDQ_Open_Trial_Search_ID"""

    PDQ_CLOSED_TRIAL_SEARCH_ID = "P330"
    """PDQ_Closed_Trial_Search_ID"""

    NCBI_TAXON_ID = "P331"
    """NCBI_Taxon_ID"""

    MGI_ACCESSION_ID = "P332"
    """MGI_Accession_ID"""

    USE_FOR = "P333"
    """Use_For"""

    ICD_O_3_CODE = "P334"
    """ICD-O-3_Code"""

    CHEMICAL_FORMULA = "P350"
    """Chemical_Formula"""

    US_RECOMMENDED_INTAKE = "P351"
    """US_Recommended_Intake"""

    TOLERABLE_LEVEL = "P352"
    """Tolerable_Level"""

    INFOODS = "P353"
    """INFOODS"""

    USDA_ID = "P354"
    """USDA_ID"""

    UNIT = "P355"
    """Unit"""

    ESSENTIAL_AMINO_ACID = "P356"
    """Essential_Amino_Acid"""

    ESSENTIAL_FATTY_ACID = "P357"
    """Essential_Fatty_Acid"""

    NUTRIENT = "P358"
    """Nutrient"""

    MICRONUTRIENT = "P359"
    """Micronutrient"""

    MACRONUTRIENT = "P360"
    """Macronutrient"""

    EXTENSIBLE_LIST = "P361"
    """Extensible_List"""

    MIRBASE_ID = "P362"
    """miRBase_ID"""

    NEOPLASTIC_STATUS = "P363"
    """Neoplastic_Status"""

    OLD_ASSOCIATION = "P364"
    """OLD_ASSOCIATION"""

    LEGACY_CONCEPT_NAME = "P366"
    """Legacy Concept Name"""

    PID_ID = "P367"
    """PID_ID"""

    CHEBI_ID = "P368"
    """CHEBI_ID"""

    HGNC_ID = "P369"
    """HGNC_ID"""

    NICHD_HIERARCHY_TERM = "P371"
    """NICHD_Hierarchy_Term"""

    PUBLISH_VALUE_SET = "P372"
    """Publish_Value_Set"""

    VALUE_SET_LOCATION = "P374"
    """Value_Set_Location"""

    MAPS_TO = "P375"
    """Maps_To"""

    TERM_BROWSER_VALUE_SET_DESCRIPTION = "P376"
    """Term_Browser_Value_Set_Description"""

    VALUE_SET_PAIR = "P398"
    """Value_Set_Pair"""

    NCI_DRUG_DICTIONARY_ID = "P399"
    """NCI_Drug_Dictionary_ID"""

    CLINVAR_VARIATION_ID = "P400"
    """ClinVar_Variation_ID"""

    FULL_SYN = "P90"
    """FULL_SYN"""

    SUBSOURCE = "P92"
    """Subsource"""

    SWISS_PROT = "P93"
    """Swiss_Prot"""

    GENE_ENCODES_PRODUCT = "P96"
    """Gene_Encodes_Product"""

    DEFINITION = "P97"
    """DEFINITION"""

    DESIGN_NOTE = "P98"
    """DesignNote"""

    XREF = "oboInOwl:hasDbXref"
    """xRef"""

    DEPRECATED = "owl:deprecated"
    """deprecated"""
