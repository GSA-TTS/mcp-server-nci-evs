---
name: ncim-property-information
description: NCI Metathesaurus (NCIM) property codes reference guide for filtering and searching concepts in the EVS API
---

# NCIM Property Information

This skill provides detailed information about NCI Metathesaurus (NCIM) property codes that can be used when searching and filtering concepts in the NCI EVS API.

## Overview

Properties in NCIM are attributes that provide additional information about concepts from the NCI Metathesaurus, which integrates multiple source vocabularies. When using the `search_concepts` tool, you can filter results by specific properties using the `property` parameter along with the `value` parameter.

**Important**: These properties can only be used when `terminology` is set to `'ncim'`.

## Property Categories

Properties are organized into logical categories for easier reference:

1. **Core Identifiers and Metadata**
2. **Gene and Molecular Biology**
3. **Chemical and Drug Information**
4. **Clinical and Medical Coding**
5. **Anatomical and Imaging**
6. **Nutrition and Food Data**
7. **Terminology Management and Mapping**
8. **Deprecation and Version Control**
9. **Publication and Reference Data**
10. **SNOMED CT and Module Properties**

---

## Core Identifiers and Metadata

### CODE

**Name**: `CODE`  
**Description**: The source vocabulary code for the concept.

---

### Semantic_Type

**Name**: `Semantic_Type`  
**Description**: UMLS semantic type classification for the concept. Used for filtering by concept categories.

**Common Values**:
- Disease or Syndrome
- Neoplastic Process
- Pharmacologic Substance
- Therapeutic or Preventive Procedure

---

### COMMENT

**Name**: `COMMENT`  
**Description**: Editorial or explanatory comments about the concept.

---

### ACTIVE

**Name**: `ACTIVE`  
**Description**: Indicates whether the concept is currently active in the source terminology.

---

### CLASS_ROLE

**Name**: `CLASS_ROLE`  
**Description**: Classification role of the concept in its source terminology.

---

### CLASS_SOURCE

**Name**: `CLASS_SOURCE`  
**Description**: The source terminology that provided the classification.

---

### Contributing_Source

**Name**: `Contributing_Source`  
**Description**: Organization or source that contributed the concept or information.

---

### DATE_CREATED

**Name**: `DATE_CREATED`  
**Description**: Date when the concept was first created.

---

### DATE_FIRST_PUBLISHED

**Name**: `DATE_FIRST_PUBLISHED`  
**Description**: Date when the concept was first published.

---

### DATE_LAST_MODIFIED

**Name**: `DATE_LAST_MODIFIED`  
**Description**: Date of the most recent modification to the concept.

---

### LAST_REVIEW_ACTION

**Name**: `LAST_REVIEW_ACTION`  
**Description**: The most recent review action taken on the concept.

---

### LAST_REVIEW_DATE

**Name**: `LAST_REVIEW_DATE`  
**Description**: Date of the most recent review of the concept.

---

### CITE

**Name**: `CITE`  
**Description**: Citation information for the concept or its definition.

---

### ORIG_STY

**Name**: `ORIG_STY`  
**Description**: Original semantic type assignment.

---

### RDF_ID

**Name**: `RDF_ID`  
**Description**: Resource Description Framework identifier.

---

## Gene and Molecular Biology

### AA_GI

**Name**: `AA_GI`  
**Description**: Amino acid GenInfo Identifier.

---

### AA_REFSEQ

**Name**: `AA_REFSEQ`  
**Description**: Amino acid RefSeq identifier.

---

### CDNA_GI

**Name**: `CDNA_GI`  
**Description**: Complementary DNA GenInfo Identifier.

---

### CDNA_REFSEQ

**Name**: `CDNA_REFSEQ`  
**Description**: Complementary DNA RefSeq identifier.

---

### CDS_EXON_END

**Name**: `CDS_EXON_END`  
**Description**: Coding sequence exon end position.

---

### CDS_EXON_SRT

**Name**: `CDS_EXON_SRT`  
**Description**: Coding sequence exon start position.

---

### GEN_EXON_END

**Name**: `GEN_EXON_END`  
**Description**: Genomic exon end position.

---

### GEN_EXON_SRT

**Name**: `GEN_EXON_SRT`  
**Description**: Genomic exon start position.

---

### GEN_GI

**Name**: `GEN_GI`  
**Description**: Genomic GenInfo Identifier.

---

### GEN_INTR_END

**Name**: `GEN_INTR_END`  
**Description**: Genomic intron end position.

---

### GEN_INTR_SRT

**Name**: `GEN_INTR_SRT`  
**Description**: Genomic intron start position.

---

### GEN_REFSEQ

**Name**: `GEN_REFSEQ`  
**Description**: Genomic RefSeq identifier.

---

### GenBank_Accession_Number

**Name**: `GenBank_Accession_Number`  
**Description**: GenBank accession number for DNA/RNA sequences.

---

### Gene_Encodes_Product

**Name**: `Gene_Encodes_Product`  
**Description**: Product encoded by the gene (protein or RNA).

---

### Homologous_Gene

**Name**: `Homologous_Gene`  
**Description**: Reference to genes that share common evolutionary ancestry.

---

### HGNC_ID

**Name**: `HGNC_ID`  
**Description**: HUGO Gene Nomenclature Committee identifier.

---

### EntrezGene_ID

**Name**: `EntrezGene_ID`  
**Description**: NCBI Entrez Gene database identifier.

---

### Locus_ID

**Name**: `Locus_ID`  
**Description**: Genetic locus identifier.

---

### Swiss_Prot

**Name**: `Swiss_Prot`  
**Description**: Swiss-Prot protein sequence database identifier.

---

### MGI_Accession_ID

**Name**: `MGI_Accession_ID`  
**Description**: Mouse Genome Informatics accession identifier.

---

### NCBI_Taxon_ID

**Name**: `NCBI_Taxon_ID`  
**Description**: NCBI Taxonomy database identifier for organisms.

---

### SNP_ID

**Name**: `SNP_ID`  
**Description**: Single Nucleotide Polymorphism identifier.

---

### miRBase_ID

**Name**: `miRBase_ID`  
**Description**: miRBase database identifier for microRNA.

---

### OMIM_NUMBER

**Name**: `OMIM_Number`  
**Description**: Online Mendelian Inheritance in Man number for genetic disorders.

---

### OMIM_ALLELE

**Name**: `OMIM_ALLELE`  
**Description**: OMIM allele variant identifier.

---

### KEGG_ID

**Name**: `KEGG_ID`  
**Description**: Kyoto Encyclopedia of Genes and Genomes pathway identifier.

---

### BioCarta_ID

**Name**: `BioCarta_ID`  
**Description**: BioCarta pathway database identifier.

---

### PID_ID

**Name**: `PID_ID`  
**Description**: Pathway Interaction Database identifier.

---

### PID

**Name**: `PID`  
**Description**: Pathway identifier.

---

### Relative_Enzyme_Activity

**Name**: `Relative_Enzyme_Activity`  
**Description**: Relative enzymatic activity level or measurement.

---

### CHRM_BND_ORD

**Name**: `CHRM_BND_ORD`  
**Description**: Chromosome band order.

---

### AAL

**Name**: `AAL`  
**Description**: Automated Anatomical Labeling atlas identifier.

---


## Chemical and Drug Information

### CAS_Registry

**Name**: `CAS_Registry`  
**Description**: Chemical Abstracts Service Registry Number for chemical substances.

---

### Chemical_Formula

**Name**: `Chemical_Formula`  
**Description**: Molecular formula of the chemical compound.

---

### CHEBI_ID

**Name**: `CHEBI_ID`  
**Description**: Chemical Entities of Biological Interest database identifier.

---

### ATOMIC_NUMBER

**Name**: `ATOMIC_NUMBER`  
**Description**: Atomic number for chemical elements.

---

### FDA_UNII_CODE

**Name**: `FDA_UNII_Code`  
**Description**: FDA Unique Ingredient Identifier code.

---

### FDA_TABLE

**Name**: `FDA_Table`  
**Description**: FDA regulatory table classification.

---

### NSC_NUMBER

**Name**: `NSC_Number`  
**Description**: National Service Center number for chemical compounds in the NCI DTP.

---

### NCI_DRUG_DICTIONARY_ID

**Name**: `NCI_Drug_Dictionary_ID`  
**Description**: Identifier in the NCI Drug Dictionary.

---

### Accepted_Therapeutic_Use_For

**Name**: `Accepted_Therapeutic_Use_For`  
**Description**: Accepted medical conditions or indications for therapeutic use.

---

### Use_For

**Name**: `Use_For`  
**Description**: General usage or application of the concept.

---

### CONCENTRATION_STRENGTH_DENOMINATOR_VALUE

**Name**: `CONCENTRATION_STRENGTH_DENOMINATOR_VALUE`  
**Description**: Denominator value for drug concentration strength (e.g., per mL).

---

### CONCENTRATION_STRENGTH_NUMERATOR_VALUE

**Name**: `CONCENTRATION_STRENGTH_NUMERATOR_VALUE`  
**Description**: Numerator value for drug concentration strength (e.g., mg).

---

### PRESENTATION_STRENGTH_DENOMINATOR_VALUE

**Name**: `PRESENTATION_STRENGTH_DENOMINATOR_VALUE`  
**Description**: Denominator value for drug presentation strength.

---

### PRESENTATION_STRENGTH_NUMERATOR_VALUE

**Name**: `PRESENTATION_STRENGTH_NUMERATOR_VALUE`  
**Description**: Numerator value for drug presentation strength.

---

### COUNT_OF_ACTIVE_INGREDIENT

**Name**: `COUNT_OF_ACTIVE_INGREDIENT`  
**Description**: Number of active ingredients in the drug product.

---

### COUNT_OF_BASE_OF_ACTIVE_INGREDIENT

**Name**: `COUNT_OF_BASE_OF_ACTIVE_INGREDIENT`  
**Description**: Number of base forms of active ingredients.

---

### IS_SOLVENT

**Name**: `IS_SOLVENT`  
**Description**: Indicates whether the substance is a solvent.

---


## Clinical and Medical Coding

### ICD-O-3_Code

**Name**: `ICD-O-3_Code`  
**Description**: International Classification of Diseases for Oncology, 3rd Edition code.

---

### ICD-O-3_CODE

**Name**: `ICD-O-3_CODE`  
**Description**: Alternative form of ICD-O-3 code.

---

### CTV3ID

**Name**: `CTV3ID`  
**Description**: Clinical Terms Version 3 identifier (Read Codes).

---

### SNOMED_ID

**Name**: `SNOMED_ID`  
**Description**: SNOMED CT identifier.

---

### Neoplastic_Status

**Name**: `Neoplastic_Status`  
**Description**: Whether the condition is neoplastic (cancerous) or non-neoplastic.

---

### PDQ_Open_Trial_Search_ID

**Name**: `PDQ_Open_Trial_Search_ID`  
**Description**: Physician Data Query identifier for searching open clinical trials.

---

### PDQ_Closed_Trial_Search_ID

**Name**: `PDQ_Closed_Trial_Search_ID`  
**Description**: Physician Data Query identifier for searching closed clinical trials.

---

### ClinVar_Variation_ID

**Name**: `ClinVar_Variation_ID`  
**Description**: ClinVar database identifier for genetic variations.

---

### INCLUSION_TERM

**Name**: `INCLUSION_TERM`  
**Description**: Terms included within the scope of the concept.

---

### Axis

**Name**: `Axis`  
**Description**: Classification axis for medical coding systems.

---

### CMA_LABEL

**Name**: `CMA_LABEL`  
**Description**: Clinical modification axis label.

---

### PRIMARY_SOC

**Name**: `PRIMARY_SOC`  
**Description**: Primary System Organ Class classification.

---

### PRIMARY_PATH

**Name**: `PRIMARY_PATH`  
**Description**: Primary classification path.

---

### INTL_SOC_SORT_ORDER

**Name**: `INTL_SOC_SORT_ORDER`  
**Description**: International System Organ Class sort order.

---

### SMQ_ALGORITHM

**Name**: `SMQ_ALGORITHM`  
**Description**: Standardized MedDRA Query algorithm.

---

### SMQ_LEVEL

**Name**: `SMQ_LEVEL`  
**Description**: Standardized MedDRA Query hierarchical level.

---

### SMQ_NOTE

**Name**: `SMQ_NOTE`  
**Description**: Notes about the Standardized MedDRA Query.

---

### SMQ_SOURCE

**Name**: `SMQ_SOURCE`  
**Description**: Source of the Standardized MedDRA Query.

---

### SMQ_STATUS

**Name**: `SMQ_STATUS`  
**Description**: Status of the Standardized MedDRA Query.

---

### SMQ_TERM_LEVEL

**Name**: `SMQ_TERM_LEVEL`  
**Description**: Term level within the Standardized MedDRA Query.

---

### PT_IN_VERSION

**Name**: `PT_IN_VERSION`  
**Description**: Preferred term in version.

---

### SOS

**Name**: `SOS`  
**Description**: System Organ System classification.

---

### PXC

**Name**: `PXC`  
**Description**: Procedure cross-reference code.

---

### IAN

**Name**: `IAN`  
**Description**: International Article Number.

---

### IS_RARE

**Name**: `IS_RARE`  
**Description**: Indicates whether the disease is classified as rare.

---

### RARE_DISEASE_URL

**Name**: `RARE_DISEASE_URL`  
**Description**: URL for rare disease information resources.

---


## Anatomical and Imaging

### FMAID

**Name**: `FMAID`  
**Description**: Foundational Model of Anatomy identifier.

---

### FREESURFER

**Name**: `FREESURFER`  
**Description**: FreeSurfer brain imaging software atlas identifier.

---

### TALAIRACH

**Name**: `TALAIRACH`  
**Description**: Talairach coordinate system reference for brain mapping.

---

### JHU_DTI-81

**Name**: `JHU_DTI-81`  
**Description**: Johns Hopkins University DTI-81 white matter atlas identifier.

---

### JHU_WHITE-MATTER_TRACTOGRAPHY_ATLAS

**Name**: `JHU_WHITE-MATTER_TRACTOGRAPHY_ATLAS`  
**Description**: Johns Hopkins University white matter tractography atlas identifier.

---

## Nutrition and Food Data

### Nutrient

**Name**: `Nutrient`  
**Description**: Indicates whether the substance is a nutrient.

---

### Micronutrient

**Name**: `Micronutrient`  
**Description**: Indicates whether the substance is a micronutrient (vitamins, minerals).

---

### Macronutrient

**Name**: `Macronutrient`  
**Description**: Indicates whether the substance is a macronutrient (carbohydrates, proteins, fats).

---

### Essential_Amino_Acid

**Name**: `Essential_Amino_Acid`  
**Description**: Indicates whether the amino acid is essential in the diet.

---

### Essential_Fatty_Acid

**Name**: `Essential_Fatty_Acid`  
**Description**: Indicates whether the fatty acid is essential in the diet.

---

### US_Recommended_Intake

**Name**: `US_Recommended_Intake`  
**Description**: United States recommended daily intake amount.

---

### Tolerable_Level

**Name**: `Tolerable_Level`  
**Description**: Maximum tolerable intake level before adverse effects.

---

### INFOODS

**Name**: `INFOODS`  
**Description**: International Network of Food Data Systems identifier.

---

### USDA_ID

**Name**: `USDA_ID`  
**Description**: United States Department of Agriculture nutrient database identifier.

---

### Unit

**Name**: `Unit`  
**Description**: Unit of measurement for the substance or quantity.

---

### UNIT_SYMBOL

**Name**: `UNIT_SYMBOL`  
**Description**: Standard symbol for the unit of measurement.

---


## Terminology Management and Mapping

### MAPSETRSAB

**Name**: `MAPSETRSAB`  
**Description**: Mapping set root source abbreviation.

---

### MAPSETSID

**Name**: `MAPSETSID`  
**Description**: Mapping set source identifier.

---

### MAPSETVERSION

**Name**: `MAPSETVERSION`  
**Description**: Version of the mapping set.

---

### MAPSETVSAB

**Name**: `MAPSETVSAB`  
**Description**: Mapping set versioned source abbreviation.

---

### MTH_MAPFROMCOMPLEXITY

**Name**: `MTH_MAPFROMCOMPLEXITY`  
**Description**: Metathesaurus mapping-from complexity indicator.

---

### MTH_MAPFROMEXHAUSTIVE

**Name**: `MTH_MAPFROMEXHAUSTIVE`  
**Description**: Metathesaurus mapping-from exhaustive indicator.

---

### MTH_MAPSETCOMPLEXITY

**Name**: `MTH_MAPSETCOMPLEXITY`  
**Description**: Metathesaurus mapping set complexity indicator.

---

### MTH_MAPTOCOMPLEXITY

**Name**: `MTH_MAPTOCOMPLEXITY`  
**Description**: Metathesaurus mapping-to complexity indicator.

---

### MTH_MAPTOEXHAUSTIVE

**Name**: `MTH_MAPTOEXHAUSTIVE`  
**Description**: Metathesaurus mapping-to exhaustive indicator.

---

### FROMRSAB

**Name**: `FROMRSAB`  
**Description**: Source abbreviation for the mapping origin.

---

### FROMVSAB

**Name**: `FROMVSAB`  
**Description**: Versioned source abbreviation for the mapping origin.

---

### TORSAB

**Name**: `TORSAB`  
**Description**: Target root source abbreviation for mapping.

---

### TOVSAB

**Name**: `TOVSAB`  
**Description**: Target versioned source abbreviation for mapping.

---

### NCIRELA

**Name**: `NCIRELA`  
**Description**: NCI relationship attribute.

---

### UMLSREL

**Name**: `UMLSREL`  
**Description**: UMLS relationship type.

---

### UMLSRELA

**Name**: `UMLSRELA`  
**Description**: UMLS relationship attribute.

---

### DB_XR_ID

**Name**: `DB_XR_ID`  
**Description**: Database cross-reference identifier.

---

### Extensible_List

**Name**: `Extensible_List`  
**Description**: Indicates whether the list or value set is extensible.

---

### Publish_Value_Set

**Name**: `Publish_Value_Set`  
**Description**: Indicates whether the concept is published as part of a value set.

---

### Term_Browser_Value_Set_Description

**Name**: `Term_Browser_Value_Set_Description`  
**Description**: Description of the value set as displayed in the term browser.

---

### Value_Set_Pair

**Name**: `Value_Set_Pair`  
**Description**: Paired value set relationships.

---

### TRANS_DETAIL

**Name**: `TRANS_DETAIL`  
**Description**: Translation detail information.

---

### IS_SPANISH

**Name**: `IS_SPANISH`  
**Description**: Indicates whether the term is in Spanish.

---

### PREFERRED_NAME_GERMAN

**Name**: `PREFERRED_NAME_GERMAN`  
**Description**: Preferred name in German.

---

### SYNONYM_GERMAN

**Name**: `SYNONYM_GERMAN`  
**Description**: Synonym in German.

---

### MISSPELLING_OF_TERM

**Name**: `MISSPELLING_OF_TERM`  
**Description**: Indicates the correct spelling of a misspelled term.

---

### UNSANCTIONED_TERM

**Name**: `UNSANCTIONED_TERM`  
**Description**: Terms that are not officially sanctioned.

---


## Deprecation and Version Control

### DEPRECATION_IN_VERSION

**Name**: `DEPRECATION_IN_VERSION`  
**Description**: Version in which the concept was deprecated.

---

### DEPRECATION_OLD_PARENT

**Name**: `DEPRECATION_OLD_PARENT`  
**Description**: Previous parent concept before deprecation.

---

### DEPRECATION_OLD_RESTRICTION

**Name**: `DEPRECATION_OLD_RESTRICTION`  
**Description**: Previous restrictions before deprecation.

---

### DEPRECATION_REASON

**Name**: `DEPRECATION_REASON`  
**Description**: Reason for deprecating the concept.

---

### DEPRECATION_REPLACEMENT_TERM

**Name**: `DEPRECATION_REPLACEMENT_TERM`  
**Description**: Replacement term for the deprecated concept.

---

### REPLACED_BY

**Name**: `REPLACED_BY`  
**Description**: Concept that replaces this deprecated concept.

---

### REPLACED_WITH_TERM

**Name**: `REPLACED_WITH_TERM`  
**Description**: Term that replaces this deprecated term.

---

### SPLIT_TO_TERM

**Name**: `SPLIT_TO_TERM`  
**Description**: Terms resulting from splitting this concept.

---

### RADLEX_VERSION_OF_CLASS_CHANGE

**Name**: `RADLEX_VERSION_OF_CLASS_CHANGE`  
**Description**: RadLex version where the class change occurred.

---

### EFFECTIVE_TIME

**Name**: `EFFECTIVE_TIME`  
**Description**: Date and time when the concept becomes effective.

---


## Publication and Reference Data

### PubMedID_Primary_Reference

**Name**: `PubMedID_Primary_Reference`  
**Description**: PubMed identifier for the primary research article or reference.

---

### HAS_PUBLICATION

**Name**: `HAS_PUBLICATION`  
**Description**: Associated publication information.

---

### HAS_PUBLISHER

**Name**: `HAS_PUBLISHER`  
**Description**: Publisher information.

---

### HAS_AUTHORS

**Name**: `HAS_AUTHORS`  
**Description**: Author information for publications.

---

### HAS_EDITOR

**Name**: `HAS_EDITOR`  
**Description**: Editor information for publications.

---

### HAS_TITLE

**Name**: `HAS_TITLE`  
**Description**: Publication title.

---

### HAS_YEAR

**Name**: `HAS_YEAR`  
**Description**: Year of publication.

---

### HAS_VOLUME

**Name**: `HAS_VOLUME`  
**Description**: Volume number of publication.

---

### HAS_ISSUE

**Name**: `HAS_ISSUE`  
**Description**: Issue number of publication.

---

### HAS_PAGES

**Name**: `HAS_PAGES`  
**Description**: Page numbers in publication.

---

### HAS_TEXT

**Name**: `HAS_TEXT`  
**Description**: Associated text content.

---

### HAS_DESCRIPTION

**Name**: `HAS_DESCRIPTION`  
**Description**: Descriptive text about the concept.

---

### HAS_ACCESSION

**Name**: `HAS_ACCESSION`  
**Description**: Accession identifier.

---

### HAS_ACCESSION_VERSION

**Name**: `HAS_ACCESSION_VERSION`  
**Description**: Version of the accession identifier.

---

### HAS_ID

**Name**: `HAS_ID`  
**Description**: General identifier property.

---

### HAS_VERSION

**Name**: `HAS_VERSION`  
**Description**: Version information.

---

### HAS_VALUE

**Name**: `HAS_VALUE`  
**Description**: Associated value.

---

### HAS_ORDER

**Name**: `HAS_ORDER`  
**Description**: Order or sequence number.

---

### HAS_NAME

**Name**: `HAS_NAME`  
**Description**: Name property.

---

### HAS_FIRST_NAME

**Name**: `HAS_FIRST_NAME`  
**Description**: First name of a person.

---

### HAS_LAST_NAME

**Name**: `HAS_LAST_NAME`  
**Description**: Last name of a person.

---

### HAS_MID_INITIALS

**Name**: `HAS_MID_INITIALS`  
**Description**: Middle initials of a person.

---

### HAS_ADDRESS

**Name**: `HAS_ADDRESS`  
**Description**: Address information.

---

### HAS_EMAIL

**Name**: `HAS_EMAIL`  
**Description**: Email address.

---

### HAS_PHONE

**Name**: `HAS_PHONE`  
**Description**: Phone number.

---

### HAS_FAX

**Name**: `HAS_FAX`  
**Description**: Fax number.

---

### HAS_TOLL_FREE_PHONE

**Name**: `HAS_TOLL_FREE_PHONE`  
**Description**: Toll-free phone number.

---

### HAS_GARD_PAGE

**Name**: `HAS_GARD_PAGE`  
**Description**: Genetic and Rare Diseases Information Center page URL.

---

### HAS_HUMAN_READABLE_URI

**Name**: `HAS_HUMAN_READABLE_URI`  
**Description**: URI intended for human reading.

---

### HAS_MACHINE_READABLE_URI

**Name**: `HAS_MACHINE_READABLE_URI`  
**Description**: URI intended for machine processing.

---

### HAS_MAKE

**Name**: `HAS_MAKE`  
**Description**: Manufacturer or make information.

---

### HAS_MODEL

**Name**: `HAS_MODEL`  
**Description**: Model information.

---


## SNOMED CT and Module Properties

### MODULE_ID

**Name**: `MODULE_ID`  
**Description**: SNOMED CT module identifier.

---

### MODULE_NAME

**Name**: `MODULE_NAME`  
**Description**: SNOMED CT module name.

---

### DEFAULT_MODULE_ID

**Name**: `DEFAULT_MODULE_ID`  
**Description**: Default SNOMED CT module identifier.

---

### DEFAULT_LANGUAGECODE

**Name**: `DEFAULT_LANGUAGECODE`  
**Description**: Default language code for the terminology.

---

### DEFINITION_STATUS_ID

**Name**: `DEFINITION_STATUS_ID`  
**Description**: SNOMED CT definition status identifier (primitive vs defined).

---

### DESCRIPTION_FORMAT

**Name**: `DESCRIPTION_FORMAT`  
**Description**: Format of the description text.

---

### DESCRIPTION_LENGTH

**Name**: `DESCRIPTION_LENGTH`  
**Description**: Length of the description text.

---

### REFSET_PATTERN

**Name**: `REFSET_PATTERN`  
**Description**: SNOMED CT reference set pattern.

---

### Design_Note

**Name**: `Design_Note`  
**Description**: Design or editorial notes about the concept.

---

### DESIGN_NOTE

**Name**: `DESIGN_NOTE`  
**Description**: Design or editorial notes (alternate form).

---


## Usage Examples

### Example 1: Search by Semantic Type

Search for all NCIM concepts with Semantic_Type of "Pharmacologic Substance":

```python
search_concepts(
    term="drug",
    terminology="ncim",
    property=NCIMProperty.SEMANTIC_TYPE,
    value="Pharmacologic Substance"
)
```

### Example 2: Filter by CAS Registry Number

Find a chemical compound by its CAS Registry Number in the metathesaurus:

```python
search_concepts(
    term="",
    terminology="ncim",
    property=NCIMProperty.CAS_REGISTRY,
    value="50-78-2"  # Aspirin
)
```

### Example 3: Search by Gene Identifier

Search for concepts related to a specific gene using EntrezGene ID:

```python
search_concepts(
    term="",
    terminology="ncim",
    property=NCIMProperty.ENTREZGENE_ID,
    value="672"  # BRCA1
)
```

### Example 4: Filter by SNOMED CT Module

Find concepts from a specific SNOMED CT module:

```python
search_concepts(
    term="diabetes",
    terminology="ncim",
    property=NCIMProperty.MODULE_ID,
    value="900000000000207008"  # SNOMED CT core module
)
```

### Example 5: Search Active Concepts

Find only active (non-deprecated) concepts:

```python
search_concepts(
    term="hypertension",
    terminology="ncim",
    property=NCIMProperty.ACTIVE,
    value="1"
)
```

### Example 6: Find Rare Diseases

Find concepts classified as rare diseases:

```python
search_concepts(
    term="",
    terminology="ncim",
    property=NCIMProperty.IS_RARE,
    value="true"
)
```

### Example 7: Search by SNOMED ID

Find concepts with a specific SNOMED CT identifier:

```python
search_concepts(
    term="",
    terminology="ncim",
    property=NCIMProperty.SNOMED_ID,
    value="73211009"  # Diabetes mellitus
)
```

## Notes

- Properties can be specified using their names exactly as shown (e.g., `CAS_Registry`, `Semantic_Type`)
- When using the `property` parameter with `search_concepts`, you should also provide a `value` parameter to filter by specific property values
- Not all concepts have values for all properties
- NCIM integrates multiple source vocabularies, so property availability varies by source
- The `term` parameter works together with `property` and `value` to further restrict results
- Property values are case-sensitive in most cases
- NCIM includes concepts from UMLS, SNOMED CT, and many other source terminologies

## Property Selection Tips

1. **For Cross-Terminology Searching**: Use source-specific IDs like `SNOMED_ID`, `CTV3ID`
2. **For Gene Research**: Use `HGNC_ID`, `EntrezGene_ID`, `GenBank_Accession_Number`
3. **For Drug Information**: Use `FDA_UNII_CODE`, `CAS_Registry`, `NCI_Drug_Dictionary_ID`
4. **For Clinical Coding**: Use `ICD-O-3_Code`, `SNOMED_ID`, `Neoplastic_Status`
5. **For Anatomy**: Use `FMAID`, `TALAIRACH`, `FREESURFER` for anatomical structures
6. **For Mapping**: Use the `MAPSET*` and `MTH_MAP*` properties for terminology mappings
7. **For Version Control**: Use deprecation properties to track concept history
8. **For Multilingual**: Use `IS_SPANISH`, `PREFERRED_NAME_GERMAN`, `SYNONYM_GERMAN`

## Differences from NCIT Properties

NCIM (NCI Metathesaurus) differs from NCIT (NCI Thesaurus) in several ways:

- **Integration**: NCIM integrates concepts from multiple source vocabularies (UMLS, SNOMED CT, etc.)
- **Mapping Properties**: NCIM has extensive mapping properties for cross-terminology alignment
- **Module Properties**: NCIM includes SNOMED CT module and structure properties
- **Multilingual**: NCIM has properties for German and Spanish translations
- **Source Tracking**: NCIM tracks the contributing source for each concept
- **Complexity**: NCIM has more granular properties for drug dosage forms and strengths

## Related Tools

- **search_concepts**: Main tool for searching and filtering concepts using these properties
- **get_concepts**: Retrieve detailed information about specific concepts, including their property values

## Quick Reference: Most Commonly Used NCIM Properties

| Property | Use Case |
|----------|----------|
| Semantic_Type | Filter by concept category |
| CODE | Source vocabulary code |
| ACTIVE | Filter active/inactive concepts |
| CAS_Registry | Chemical identification |
| FDA_UNII_CODE | Drug identification |
| SNOMED_ID | SNOMED CT cross-reference |
| ICD-O-3_Code | Cancer classification |
| HGNC_ID | Gene identification |
| EntrezGene_ID | Gene database reference |
| MODULE_ID | SNOMED CT module |
| Contributing_Source | Source terminology |
| Neoplastic_Status | Cancer vs non-cancer |

## Quick Reference: NCIM-Specific Properties

Properties unique or especially important in NCIM:

| Property | Use Case |
|----------|----------|
| MODULE_ID | SNOMED CT module identification |
| MAPSET* properties | Terminology mapping metadata |
| MTH_MAP* properties | Metathesaurus mapping complexity |
| IS_SPANISH | Spanish language terms |
| SYNONYM_GERMAN | German translations |
| FROMRSAB / TORSAB | Mapping source and target |
| HAS_GARD_PAGE | Rare disease information |
| REFSET_PATTERN | SNOMED CT reference sets |
