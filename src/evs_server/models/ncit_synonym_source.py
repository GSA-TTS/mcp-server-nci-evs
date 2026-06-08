"""NCI Thesaurus synonym source enumeration."""

from enum import Enum


class NCITSynonymSource(str, Enum):
    """Enumeration of NCI Thesaurus (ncit) synonym sources.
    
    Note: This parameter can only be used when terminology is set to 'ncit'.
    """

    ACC_AHA = "ACC/AHA"
    """American College of Cardiology / American Heart Association"""

    BIOCARTA = "BIOCARTA"
    """BioCarta online maps of molecular pathways, adapted for NCI use"""

    BRIDG = "BRIDG"
    """Biomedical Research Integrated Domain Model Group"""

    BRIDG_3_0_3 = "BRIDG 3.0.3"
    """Biomedical Research Integrated Domain Model Group, version 3.0.3"""

    BRIDG_5_3 = "BRIDG 5.3"
    """Biomedical Research Integrated Domain Model Group, version 5.3"""

    CBDD = "CBDD"
    """Chemical Biology and Drug Development"""

    CCPS = "CCPS"
    """Childhood Cancer Predisposition Study"""

    CDC = "CDC"
    """U.S. Centers for Disease Control and Prevention"""

    CDISC = "CDISC"
    """Clinical Data Interchange Standards Consortium"""

    CDISC_GLOSS = "CDISC-GLOSS"
    """CDISC Glossary Terminology"""

    CPTAC = "CPTAC"
    """Clinical Proteomic Tumor Analysis Consortium"""

    CRCH = "CRCH"
    """Cancer Research Center of Hawaii Nutrition Terminology"""

    CTCAE = "CTCAE"
    """Common Terminology Criteria for Adverse Events"""

    CTCAE_3_0 = "CTCAE 3.0"
    """Common Terminology Criteria for Adverse Events, version 3.0"""

    CTCAE_5_0 = "CTCAE 5.0"
    """Common Terminology Criteria for Adverse Events, version 5.0"""

    CTCAE_6_0 = "CTCAE 6.0"
    """Common Terminology Criteria for Adverse Events, version 6.0"""

    CTDC = "CTDC"
    """Clinical Trials Data Commons"""

    CTEP = "CTEP"
    """Cancer Therapy Evaluation Program"""

    CTRP = "CTRP"
    """Clinical Trials Reporting Program"""

    CARELEX = "CareLex"
    """CareLex electronic Trial Master File Terminology"""

    CELLOSAURUS = "Cellosaurus"
    """Cellosaurus - a knowledge resource on cell lines"""

    DCP = "DCP"
    """NCI Division of Cancer Prevention Program"""

    DICOM = "DICOM"
    """Digital Imaging Communications in Medicine"""

    DIPG_DMG = "DIPG/DMG"
    """Diffuse Intrinsic Pontine Glioma/Diffuse Midline Glioma"""

    DTP = "DTP"
    """NCI Developmental Therapeutics Program"""

    EDQM_HC = "EDQM-HC"
    """European Directorate for the Quality of Medicines & Healthcare"""

    FDA = "FDA"
    """U.S. Food and Drug Administration"""

    FDA_NIH_MORE = "FDA-NIH-MoRE"
    """FDA-NIH-Modernizing Research and Evidence"""

    GAIA = "GAIA"
    """Global Alignment of Immunization safety Assessment in pregnancy Terminology"""

    GDC = "GDC"
    """Genomic Data Commons"""

    GENC = "GENC"
    """Geopolitical Entities, Names, and Codes Terminology"""

    HGNC = "HGNC"
    """HUGO Gene Nomenclature Committee"""

    HL7 = "HL7"
    """Health Level Seven International"""

    HEMONC = "HemOnc"
    """HemOnc.org (A Free Hematology/Oncology Reference)"""

    ICD_10 = "ICD-10"
    """International Classification of Diseases, Tenth Revision"""

    ICDC = "ICDC"
    """International Cancer Genome Consortium"""

    ICH = "ICH"
    """International Conference on Harmonization"""

    INC = "INC"
    """International Neonatal Consortium"""

    JAX = "JAX"
    """Jackson Laboratories Mouse Terminology, adapted for NCI use"""

    KEGG = "KEGG"
    """KEGG Pathway Database"""

    MRCT_CTR = "MRCT-Ctr"
    """MRCT Center Clinical Research Plain Language Glossary at Harvard and Brigham and Women's Hospital"""

    NCI = "NCI"
    """National Cancer Institute Thesaurus"""

    NCI_GLOSS = "NCI-GLOSS"
    """NCI Dictionary of Cancer Terms"""

    NCPDP = "NCPDP"
    """National Council for Prescription Drug Programs"""

    NDC = "NDC"
    """National Drug Code"""

    NICHD = "NICHD"
    """National Institute of Child Health and Human Development"""

    OORO = "OORO"
    """Operational Ontology for Radiation Oncology"""

    ORCHESTRA = "ORCHESTRA"
    """Multinational project funded by the European Commission to advance the knowledge of the SARS-CoV-2 infection and its long-term effects"""

    PCDC = "PCDC"
    """Pediatric Cancer Data Commons"""

    PI_RADS = "PI-RADS"
    """Prostate Imaging-Reporting and Data System"""

    PID = "PID"
    """NCI Nature Pathway Interaction Database"""

    PRO_CTCAE = "PRO-CTCAE"
    """PRO-CTCAE (Patient Reported Outcomes version of Common Terminology Criteria for Adverse Events)"""

    RENI = "RENI"
    """Registry Nomenclature Information System"""

    SEER = "SEER"
    """Surveillance, Epidemiology, and End Results Program"""

    SERONET = "SeroNet"
    """NCI Serological Sciences Network for COVID-19"""

    UBERON = "UBERON"
    """Uber-anatomy Ontology"""

    UCUM = "UCUM"
    """Unified Code for Units of Measure"""

    WHO = "WHO"
    """World Health Organization"""

    ZFIN = "ZFin"
    """Zebrafish Information Network"""

    CADSR = "caDSR"
    """Cancer Data Standards Registry and Repository"""

    MCODE = "mCode"
    """Minimal Common Oncology Data Elements"""
