"""NCI Metathesaurus synonym term type enumeration."""

from enum import Enum


class NCIMSynonymTermType(str, Enum):
    """Enumeration of NCI Metathesaurus (ncim) synonym term types.
    
    Note: This parameter can only be used when terminology is set to 'ncim'.
    """

    AB = "AB"
    """Abbreviation in any source vocabulary"""

    ACR = "ACR"
    """Acronym"""

    AD = "AD"
    """Adjective"""

    AM = "AM"
    """Short form of modifier"""

    BN = "BN"
    """Fully-specified drug brand name that can not be prescribed"""

    BPCK = "BPCK"
    """Branded Drug Delivery Device"""

    BR = "BR"
    """Binding realm"""

    CA2 = "CA2"
    """ISO 3166-1 standard country code in alpha-2 (two-letter) format"""

    CA3 = "CA3"
    """ISO 3166-1 standard country code in alpha-3 (three-letter) format"""

    CAS = "CAS"
    """CAS Registry name"""

    CC = "CC"
    """Trimmed ICPC component process"""

    CCN = "CCN"
    """Chemical code name"""

    CD = "CD"
    """Clinical Drug"""

    CDO = "CDO"
    """Concept domain"""

    CE = "CE"
    """Entry term for a Supplementary Concept"""

    CHN = "CHN"
    """Chemical structure name"""

    CMN = "CMN"
    """Common name"""

    CN = "CN"
    """LOINC official component name"""

    CNU = "CNU"
    """ISO 3166-1 standard country code in numeric (three-digit) format"""

    CO = "CO"
    """Component name (hierarchical terms)"""

    CON = "CON"
    """Code name"""

    CP = "CP"
    """ICPC component process (in original form)"""

    CPR = "CPR"
    """Concept property"""

    CR = "CR"
    """Concept relationship"""

    CS = "CS"
    """Short component process in ICPC"""

    CSD = "CSD"
    """Country subdivision name"""

    CSN = "CSN"
    """Chemical Structure Name"""

    CSY = "CSY"
    """Code system"""

    CU = "CU"
    """Common usage"""

    CX = "CX"
    """Component, with abbreviations expanded"""

    DE = "DE"
    """Descriptor"""

    DEV = "DEV"
    """Descriptor entry version"""

    DF = "DF"
    """Dose Form"""

    DFG = "DFG"
    """Dose Form Group"""

    DHT = "DHT"
    """Deprecated hierarchical term"""

    DI = "DI"
    """Disease name"""

    DN = "DN"
    """Display Name"""

    DP = "DP"
    """Drug Product"""

    DPT = "DPT"
    """Deprecated preferred term"""

    DS = "DS"
    """Short form of descriptor"""

    DSY = "DSY"
    """Deprecated synonym"""

    DT = "DT"
    """Definitional term"""

    EQ = "EQ"
    """Equivalent name"""

    ES = "ES"
    """Short form of entry term"""

    ET = "ET"
    """Entry term"""

    ETAL = "ETAL"
    """Entry Term Alias"""

    EX = "EX"
    """Expanded form of entry term"""

    FBD = "FBD"
    """Foreign brand name"""

    FI = "FI"
    """Finding name"""

    FN = "FN"
    """Full form of descriptor"""

    FSY = "FSY"
    """Foreign Synonym"""

    GPCK = "GPCK"
    """Generic Drug Delivery Device"""

    GT = "GT"
    """Glossary term"""

    HC = "HC"
    """Hierarchical class"""

    HD = "HD"
    """Hierarchical descriptor"""

    HG = "HG"
    """High Level Group Term"""

    HS = "HS"
    """Short or alternate version of hierarchical term"""

    HT = "HT"
    """Hierarchical term"""

    HX = "HX"
    """Expanded version of short hierarchical term"""

    IN = "IN"
    """Name for an ingredient"""

    IND = "IND"
    """IND code"""

    IS = "IS"
    """Obsolete Synonym"""

    LA = "LA"
    """LOINC answer"""

    LC = "LC"
    """Long common name"""

    LG = "LG"
    """LOINC group"""

    LLT = "LLT"
    """Lower Level Term"""

    LN = "LN"
    """LOINC official fully specified name"""

    LO = "LO"
    """Obsolete official fully specified name"""

    LS = "LS"
    """Expanded system/sample type"""

    LV = "LV"
    """Lexical variant"""

    MH = "MH"
    """Main heading"""

    MIN = "MIN"
    """name for a multi-ingredient"""

    MP = "MP"
    """Preferred names of modifiers"""

    MTH_ACR = "MTH_ACR"
    """MTH acronym"""

    MTH_CN = "MTH_CN"
    """MTH Component, with abbreviations expanded"""

    MTH_ET = "MTH_ET"
    """Metathesaurus entry term"""

    MTH_HG = "MTH_HG"
    """MTH High Level Group Term"""

    MTH_HT = "MTH_HT"
    """MTH Hierarchical term"""

    MTH_HX = "MTH_HX"
    """MTH Hierarchical term expanded"""

    MTH_IS = "MTH_IS"
    """Metathesaurus-supplied form of obsolete synonym"""

    MTH_LLT = "MTH_LLT"
    """MTH Lower Level Term"""

    MTH_LN = "MTH_LN"
    """MTH Official fully specified name with expanded abbreviations"""

    MTH_LO = "MTH_LO"
    """MTH Expanded LOINC obsolete fully specified name"""

    MTH_OET = "MTH_OET"
    """Metathesaurus obsolete entry term"""

    MTH_OL = "MTH_OL"
    """MTH Non-current Lower Level Term"""

    MTH_OP = "MTH_OP"
    """Metathesaurus obsolete preferred term"""

    MTH_OS = "MTH_OS"
    """MTH System Organ Class"""

    MTH_PT = "MTH_PT"
    """Metathesaurus preferred term"""

    MTH_RXN_CD = "MTH_RXN_CD"
    """RxNorm Created CD"""

    MTH_RXN_DP = "MTH_RXN_DP"
    """RxNorm Created DP"""

    MTH_SMQ = "MTH_SMQ"
    """Metathesaurus version of Standardised MedDRA Query"""

    MTH_SY = "MTH_SY"
    """MTH Designated synonym"""

    N1 = "N1"
    """Chemical Abstracts Service Type 1 name of a chemical"""

    NA = "NA"
    """Name aliases"""

    NM = "NM"
    """Name of Supplementary Concept"""

    NP = "NP"
    """Non-preferred term"""

    NPT = "NPT"
    """HL7 non-preferred for language term"""

    NS = "NS"
    """Short form of non-preferred term"""

    NSC = "NSC"
    """NSC code"""

    NX = "NX"
    """Expanded form of non-preferred term"""

    OA = "OA"
    """Obsolete abbreviation"""

    OAM = "OAM"
    """Obsolete Modifier Abbreviation"""

    ODN = "ODN"
    """Obsolete Display Name"""

    OET = "OET"
    """Obsolete entry term"""

    OF = "OF"
    """Obsolete fully specified name"""

    OL = "OL"
    """Non-current Lower Level Term"""

    OLC = "OLC"
    """Obsolete Long common name"""

    OLG = "OLG"
    """Obsolete LOINC group name"""

    OM = "OM"
    """Obsolete modifiers in HCPCS"""

    ONP = "ONP"
    """Obsolete non-preferred for language term"""

    OOSN = "OOSN"
    """Obsolete official short name"""

    OP = "OP"
    """Obsolete preferred name"""

    ORT = "ORT"
    """Obsolete related term"""

    OS = "OS"
    """System Organ Class"""

    OSN = "OSN"
    """Official short name"""

    PC = "PC"
    """Preferred \"trimmed term\" in ICPC"""

    PCE = "PCE"
    """Preferred entry term for Supplementary Concept"""

    PEP = "PEP"
    """Preferred entry term"""

    PHENO = "PHENO"
    """Phenotype"""

    PHENO_ET = "PHENO_ET"
    """Phenotype entry term"""

    PIN = "PIN"
    """Name from a precise ingredient"""

    PM = "PM"
    """Machine permutation"""

    PN = "PN"
    """Metathesaurus preferred name"""

    PS = "PS"
    """Short forms that needed full specification"""

    PSC = "PSC"
    """Protocol selection criteria"""

    PSN = "PSN"
    """Prescribable Names"""

    PT = "PT"
    """Designated preferred name"""

    PTAV = "PTAV"
    """Preferred Allelic Variant"""

    PTCS = "PTCS"
    """Preferred Clinical Synopsis"""

    PTGB = "PTGB"
    """British preferred term"""

    PX = "PX"
    """Expanded preferred terms"""

    PXQ = "PXQ"
    """Preferred qualifier term"""

    QAB = "QAB"
    """Qualifier abbreviation"""

    QEV = "QEV"
    """Qualifier entry version"""

    RAB = "RAB"
    """Root abbreviation"""

    RHT = "RHT"
    """Root hierarchical term"""

    RPT = "RPT"
    """Root preferred term"""

    RSY = "RSY"
    """Root synonym"""

    RT = "RT"
    """Related term"""

    RXN_PT = "RXN_PT"
    """Rxnorm Preferred"""

    SB = "SB"
    """Named subset of a source"""

    SBD = "SBD"
    """Semantic branded drug"""

    SBDC = "SBDC"
    """Semantic Branded Drug Component"""

    SBDF = "SBDF"
    """Semantic branded drug and form"""

    SBDFP = "SBDFP"
    """Semantic branded drug and form with precise ingredient"""

    SBDG = "SBDG"
    """Semantic branded drug group"""

    SC = "SC"
    """Special Category term"""

    SCD = "SCD"
    """Semantic Clinical Drug"""

    SCDC = "SCDC"
    """Semantic Drug Component"""

    SCDF = "SCDF"
    """Semantic clinical drug and form"""

    SCDFP = "SCDFP"
    """Semantic clinical drug and form with precise ingredient"""

    SCDG = "SCDG"
    """Semantic clinical drug group"""

    SCDGP = "SCDGP"
    """Semantic clinical drug group with precise ingredient"""

    SCN = "SCN"
    """Scientific name"""

    SD = "SD"
    """CCS single-level diagnosis categories"""

    SMQ = "SMQ"
    """Standardised MedDRA Query"""

    SP = "SP"
    """CCS single-level procedure categories"""

    SSN = "SSN"
    """Source short name"""

    SU = "SU"
    """Active Substance"""

    SY = "SY"
    """Designated synonym"""

    SYGB = "SYGB"
    """British synonym"""

    SYN = "SYN"
    """Designated alias"""

    TMSY = "TMSY"
    """Tall Man synonym"""

    TQ = "TQ"
    """Topical qualifier"""

    UCN = "UCN"
    """Unique common name"""

    UE = "UE"
    """Unique equivalent name"""

    USN = "USN"
    """Unique scientific name"""

    USY = "USY"
    """Unique synonym"""

    VAB = "VAB"
    """Versioned abbreviation"""

    VPT = "VPT"
    """Versioned preferred term"""

    VS = "VS"
    """Value Set"""

    VSY = "VSY"
    """Versioned synonym"""

    XD = "XD"
    """Expanded descriptor in AOD"""

    XM = "XM"
    """Cross mapping set"""

    XQ = "XQ"
    """Alternate name for a qualifier"""
