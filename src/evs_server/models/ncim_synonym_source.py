"""NCI Metathesaurus synonym source enumeration."""

from enum import Enum


class NCIMSynonymSource(str, Enum):
    """Enumeration of NCI Metathesaurus (ncim) synonym sources.
    
    Note: This parameter can only be used when terminology is set to 'ncim'.
    """

    ACC_AHA = "ACC-AHA"
    """American College of Cardiology/American Heart Association Clinical Data Terminology"""

    AOD = "AOD"
    """Alcohol and Other Drug Thesaurus"""

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

    CBDD = "CBDD"
    """Chemical Biology and Drug Development Vocabulary"""

    CBO = "CBO"
    """Clinical Bioinformatics Ontology"""

    CCPS = "CCPS"
    """Childhood Cancer Predisposition Study"""

    CCSR_ICD10CM = "CCSR_ICD10CM"
    """Clinical Classifications Software Refined for ICD-10-CM"""

    CCSR_ICD10PCS = "CCSR_ICD10PCS"
    """Clinical Classifications Software Refined for ICD-10-PCS"""

    CDC = "CDC"
    """U.S. Centers for Disease Control and Prevention"""

    CDCREC = "CDCREC"
    """Race & Ethnicity - CDC"""

    CDISC = "CDISC"
    """Clinical Data Interchange Standards Consortium"""

    CDISC_GLOSS = "CDISC-GLOSS"
    """Clinical Data Interchange Standards Consortium Glossary Terms"""

    CELLOSAURUS = "CELLOSAURUS"
    """Cellosaurus"""

    COSTAR = "COSTAR"
    """COSTAR"""

    CPTAC = "CPTAC"
    """Clinical Proteomic Tumor Analysis Consortium"""

    CRCH = "CRCH"
    """Cancer Research Center of Hawaii Nutrition Terminology"""

    CSP = "CSP"
    """CRISP Thesaurus"""

    CST = "CST"
    """COSTART"""

    CTCAE = "CTCAE"
    """Common Terminology Criteria for Adverse Events"""

    CTCAE_3 = "CTCAE_3"
    """Common Terminology Criteria for Adverse Events 3.0"""

    CTCAE_5 = "CTCAE_5"
    """Common Terminology Criteria for Adverse Events 5.0"""

    CTDC = "CTDC"
    """Clinical Trial Data Commons"""

    CTEP = "CTEP"
    """Cancer Therapy Evaluation Program"""

    CTEP_SDC = "CTEP-SDC"
    """Cancer Therapy Evaluation Program - Simple Disease Classification"""

    CTRP = "CTRP"
    """Clinical Trials Reporting Program"""

    CVX = "CVX"
    """Vaccines Administered"""

    DCP = "DCP"
    """NCI Division of Cancer Prevention Program"""

    DICOM = "DICOM"
    """Digital Imaging Communications in Medicine"""

    DIPG_DMG = "DIPG_DMG"
    """Diffuse Intrinsic Pontine Glioma/Diffuse Midline Glioma Terminology"""

    DRUGBANK = "DRUGBANK"
    """DrugBank"""

    DTP = "DTP"
    """NCI Developmental Therapeutics Program"""

    DXP = "DXP"
    """DXplain"""

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

    GDC = "GDC"
    """NCI Genomic Data Commons"""

    GENC = "GENC"
    """Geopolitical Entities, Names, and Codes Standard"""

    GO = "GO"
    """Gene Ontology"""

    HCPCS = "HCPCS"
    """Healthcare Common Procedure Coding System"""

    HGNC = "HGNC"
    """HUGO Gene Nomenclature Committee"""

    HL7V3_0 = "HL7V3.0"
    """HL7 Vocabulary Version 3.0"""

    HPO = "HPO"
    """Human Phenotype Ontology"""

    HEMONC = "HemOnc"
    """Hematology-Oncology (HemOnc) Chemotherapy Regimen Vocabulary"""

    ICD_10 = "ICD-10"
    """International Classification of Diseases, 10th Edition"""

    ICD10 = "ICD10"
    """ICD10"""

    ICD10CM = "ICD10CM"
    """International Classification of Diseases, 10th Edition, Clinical Modification"""

    ICD10PCS = "ICD10PCS"
    """ICD-10-PCS"""

    ICD9CM = "ICD9CM"
    """International Classification of Diseases, Ninth Revision, Clinical Modification"""

    ICDC = "ICDC"
    """NCI Integrated Canine Data Commons"""

    ICDO = "ICDO"
    """International Classification of Disease for Oncology"""

    ICH = "ICH"
    """International Conference on Harmonization"""

    ICPC = "ICPC"
    """International Classification of Primary Care"""

    INC = "INC"
    """International Neonatal Consortium"""

    ISO3166_2 = "ISO3166-2"
    """International Organization for Standardization 3166-2"""

    JAX = "JAX"
    """Jackson Laboratories Mouse Terminology, adapted for NCI use"""

    KEGG = "KEGG"
    """KEGG Pathway Database"""

    LNC = "LNC"
    """LOINC"""

    MCM = "MCM"
    """McMaster University Epidemiology Terms"""

    MDBCAC = "MDBCAC"
    """Mitelman Database of Chromosome Aberrations in Cancer"""

    MDR = "MDR"
    """Medical Dictionary for Regulatory Activities Terminology (MedDRA)"""

    MED_RT = "MED-RT"
    """Medication Reference Terminology"""

    MEDLINEPLUS = "MEDLINEPLUS"
    """MedlinePlus Health Topics"""

    MGED = "MGED"
    """MGED Ontology"""

    MRCT_CTR = "MRCT-Ctr"
    """MRCT Center Clinical Research Plain Language Glossary"""

    MSH = "MSH"
    """Medical Subject Headings"""

    MTH = "MTH"
    """UMLS Metathesaurus"""

    MTHCMSFRF = "MTHCMSFRF"
    """Metathesaurus CMS Formulary Reference File"""

    MTHICD9 = "MTHICD9"
    """International Classification of Diseases, Ninth Revision, Clinical Modification, Metathesaurus additional entry terms"""

    MTHMST = "MTHMST"
    """Metathesaurus Version of Minimal Standard Terminology Digestive Endoscopy"""

    MTHSPL = "MTHSPL"
    """Metathesaurus FDA Structured Product Labels"""

    MVX = "MVX"
    """Manufacturers of Vaccines"""

    NCBI = "NCBI"
    """NCBI Taxonomy"""

    NCI = "NCI"
    """National Cancer Institute Thesaurus"""

    NCI_GLOSS = "NCI-GLOSS"
    """NCI Dictionary of Cancer Terms"""

    NCI_HGNC = "NCI-HGNC"
    """NCI HUGO Gene Nomenclature Committee"""

    NCI_HL7 = "NCI-HL7"
    """NCI Health Level 7"""

    NCIMTH = "NCIMTH"
    """NCIMTH"""

    NCPDP = "NCPDP"
    """National Council for Prescription Drug Programs"""

    NDC = "NDC"
    """National Drug Code"""

    NICHD = "NICHD"
    """National Institute of Child Health and Human Development"""

    NPO = "NPO"
    """NPO: NanoParticle Ontology for Cancer Nanotechnology Research"""

    OMIM = "OMIM"
    """Online Mendelian Inheritance in Man"""

    OORO = "OORO"
    """Operational Ontology for Radiation Oncology"""

    ORCHESTRA = "ORCHESTRA"
    """ORCHESTRA"""

    PCDC = "PCDC"
    """Pediatric Cancer Data Commons"""

    PDQ = "PDQ"
    """Physician Data Query"""

    PI_RADS = "PI-RADS"
    """Prostate Imaging Reporting and Data System"""

    PID = "PID"
    """National Cancer Institute Nature Pathway Interaction Database"""

    PMA = "PMA"
    """Portfolio Management Application"""

    PNDS = "PNDS"
    """Perioperative Nursing Data Set"""

    PRO_CTCAE = "PRO-CTCAE"
    """Patient Reported Outcomes version of Common Terminology Criteria for Adverse Events"""

    QMR = "QMR"
    """Quick Medical Reference (QMR)"""

    RADLEX = "RADLEX"
    """RadLex"""

    RENI = "RENI"
    """Registry Nomenclature Information System"""

    RXNORM = "RXNORM"
    """RxNorm Vocabulary"""

    SNOMEDCT_US = "SNOMEDCT_US"
    """US Edition of SNOMED CT"""

    SOP = "SOP"
    """Source of Payment Typology"""

    SPN = "SPN"
    """Standard Product Nomenclature"""

    SRC = "SRC"
    """Metathesaurus Source Terminology Names"""

    SERONET = "SeroNet"
    """Serological Sciences Network Terminology"""

    UBERON = "UBERON"
    """UBERON Ontology"""

    UCUM = "UCUM"
    """Unified Code for Units of Measure"""

    UMD = "UMD"
    """UMDNS: product category thesaurus"""

    USP = "USP"
    """USP Compendial Nomenclature"""

    USPMG = "USPMG"
    """USP Medicare Model Guidelines"""

    UWDA = "UWDA"
    """University of Washington Digital Anatomist"""

    VANDF = "VANDF"
    """Veterans Health Administration National Drug File"""

    WHO = "WHO"
    """World Health Organization (WHO) Terminology"""

    ZFIN = "ZFIN"
    """Zebrafish Model Organism Database"""

    CADSR = "caDSR"
    """Cancer Data Standards Registry and Repository"""

    MCODE = "mCode"
    """Minimal Common Oncology Data Elements"""
