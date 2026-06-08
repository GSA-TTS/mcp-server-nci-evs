"""NCI Metathesaurus definition source enumeration."""

from enum import Enum


class NCIMDefinitionSource(str, Enum):
    """Enumeration of NCI Metathesaurus (ncim) definition sources.
    
    Note: This parameter can only be used when terminology is set to 'ncim'.
    """

    ACC_AHA = "ACC-AHA"
    """American College of Cardiology/American Heart Association Clinical Data Terminology"""

    AOT = "AOT"
    """Authorized Osteopathic Thesaurus"""

    BRIDG = "BRIDG"
    """Biomedical Research Integrated Domain Group Model"""

    BRIDG_3_0_3 = "BRIDG_3_0_3"
    """Biomedical Research Integrated Domain Group Model, 3.0.3"""

    BRIDG_5_3 = "BRIDG_5_3"
    """Biomedical Research Integrated Domain Group Model, 5.3"""

    BIOC = "BioC"
    """BioCarta online maps of molecular pathways, adapted for NCI use"""

    CARELEX = "CARELEX"
    """Content Archive Resource Exchange Lexicon"""

    CCPS = "CCPS"
    """Childhood Cancer Predisposition Study"""

    CDISC = "CDISC"
    """Clinical Data Interchange Standards Consortium"""

    CDISC_GLOSS = "CDISC-GLOSS"
    """Clinical Data Interchange Standards Consortium Glossary Terms"""

    CRCH = "CRCH"
    """Cancer Research Center of Hawaii Nutrition Terminology"""

    CSP = "CSP"
    """CRISP Thesaurus"""

    CTCAE = "CTCAE"
    """Common Terminology Criteria for Adverse Events"""

    CTCAE_3 = "CTCAE_3"
    """Common Terminology Criteria for Adverse Events 3.0"""

    CTCAE_5 = "CTCAE_5"
    """Common Terminology Criteria for Adverse Events 5.0"""

    CTEP = "CTEP"
    """Cancer Therapy Evaluation Program"""

    CTEP_SDC = "CTEP-SDC"
    """Cancer Therapy Evaluation Program - Simple Disease Classification"""

    DICOM = "DICOM"
    """Digital Imaging Communications in Medicine"""

    DIPG_DMG = "DIPG_DMG"
    """Diffuse Intrinsic Pontine Glioma/Diffuse Midline Glioma Terminology"""

    EDQM_HC = "EDQM-HC"
    """European Directorate for the Quality of Medicines & Healthcare"""

    FDA = "FDA"
    """U.S. Food and Drug Administration"""

    FDA_NIH_MORE = "FDA-NIH-MoRE"
    """FDA-NIH Modernizing Research and Evidence Glossary"""

    FMA = "FMA"
    """Foundational Model of Anatomy Ontology"""

    GAIA = "GAIA"
    """Global Alignment of Immunization Safety Assessment in pregnancy"""

    GARD = "GARD"
    """Genetic and Rare Diseases Information Center"""

    GO = "GO"
    """Gene Ontology"""

    HL7V3_0 = "HL7V3.0"
    """HL7 Vocabulary Version 3.0"""

    HPO = "HPO"
    """Human Phenotype Ontology"""

    ICH = "ICH"
    """International Conference on Harmonization"""

    INC = "INC"
    """International Neonatal Consortium"""

    KEGG = "KEGG"
    """KEGG Pathway Database"""

    LNC = "LNC"
    """LOINC"""

    MCM = "MCM"
    """McMaster University Epidemiology Terms"""

    MDR = "MDR"
    """Medical Dictionary for Regulatory Activities Terminology (MedDRA)"""

    MEDLINEPLUS = "MEDLINEPLUS"
    """MedlinePlus Health Topics"""

    MGED = "MGED"
    """MGED Ontology"""

    MRCT_CTR = "MRCT-Ctr"
    """MRCT Center Clinical Research Plain Language Glossary"""

    MSH = "MSH"
    """Medical Subject Headings"""

    NCI = "NCI"
    """National Cancer Institute Thesaurus"""

    NCI_GLOSS = "NCI-GLOSS"
    """NCI Dictionary of Cancer Terms"""

    NICHD = "NICHD"
    """National Institute of Child Health and Human Development"""

    NPO = "NPO"
    """NPO: NanoParticle Ontology for Cancer Nanotechnology Research"""

    OORO = "OORO"
    """Operational Ontology for Radiation Oncology"""

    PCDC = "PCDC"
    """Pediatric Cancer Data Commons"""

    PDQ = "PDQ"
    """Physician Data Query"""

    PNDS = "PNDS"
    """Perioperative Nursing Data Set"""

    RADLEX = "RADLEX"
    """RadLex"""

    SNOMEDCT_US = "SNOMEDCT_US"
    """US Edition of SNOMED CT"""

    SPN = "SPN"
    """Standard Product Nomenclature"""

    UBERON = "UBERON"
    """UBERON Ontology"""

    UMD = "UMD"
    """UMDNS: product category thesaurus"""

    UWDA = "UWDA"
    """University of Washington Digital Anatomist"""

    WHO = "WHO"
    """World Health Organization (WHO) Terminology"""
