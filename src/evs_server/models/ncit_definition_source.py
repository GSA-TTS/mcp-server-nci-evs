"""NCI Thesaurus definition source enumeration."""

from enum import Enum


class NCITDefinitionSource(str, Enum):
    """Enumeration of NCI Thesaurus (ncit) definition sources.
    
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

    CCPS = "CCPS"
    """Childhood Cancer Predisposition Study"""

    CDISC = "CDISC"
    """Clinical Data Interchange Standards Consortium"""

    CDISC_GLOSS = "CDISC-GLOSS"
    """CDISC Glossary Terminology"""

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

    CTEP = "CTEP"
    """Cancer Therapy Evaluation Program"""

    CARELEX = "CareLex"
    """CareLex electronic Trial Master File Terminology"""

    DICOM = "DICOM"
    """Digital Imaging Communications in Medicine"""

    DIPG_DMG = "DIPG/DMG"
    """Diffuse Intrinsic Pontine Glioma/Diffuse Midline Glioma"""

    EDQM_HC = "EDQM-HC"
    """European Directorate for the Quality of Medicines & Healthcare"""

    FDA = "FDA"
    """U.S. Food and Drug Administration"""

    FDA_NIH_MORE = "FDA-NIH-MoRE"
    """FDA-NIH-Modernizing Research and Evidence"""

    GAIA = "GAIA"
    """Global Alignment of Immunization safety Assessment in pregnancy Terminology"""

    ICDO3 = "ICDO3"
    """International Classification of Diseases for Oncology, 3rd edition"""

    ICH = "ICH"
    """International Conference on Harmonization"""

    INC = "INC"
    """International Neonatal Consortium"""

    KEGG = "KEGG"
    """KEGG Pathway Database"""

    MMHCC = "MMHCC"
    """Mouse Models of Human Cancer Consortium"""

    MRCT_CTR = "MRCT-Ctr"
    """MRCT Center Clinical Research Plain Language Glossary at Harvard and Brigham and Women's Hospital"""

    NCI = "NCI"
    """National Cancer Institute Thesaurus"""

    NCI_GLOSS = "NCI-GLOSS"
    """NCI Dictionary of Cancer Terms"""

    NICHD = "NICHD"
    """National Institute of Child Health and Human Development"""

    OORO = "OORO"
    """Operational Ontology for Radiation Oncology"""

    PCDC = "PCDC"
    """Pediatric Cancer Data Commons"""

    PQCMC = "PQCMC"
    """Pharmaceutical Quality/Chemistry, Manufacturing, and Controls"""

    UBERON = "UBERON"
    """Uber-anatomy Ontology"""

    UMD2001 = "UMD2001"
    """Universal Medical Device Nomenclature System, Version 2001"""

    UWDA142 = "UWDA142"
    """University of Washington Digital Anatomist, Version 1.4.2"""

    WHO = "WHO"
    """World Health Organization"""
