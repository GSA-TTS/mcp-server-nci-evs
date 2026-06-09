---
name: ncit-property-information
description: NCI Thesaurus (NCIT) property codes reference guide for filtering and searching concepts in the EVS API
---

# NCIT Property Information

This skill provides detailed information about NCI Thesaurus (NCIT) property codes that can be used when searching and filtering concepts in the NCI EVS API.

## Overview

Properties in NCIT are attributes that provide additional information about concepts. When using the `search_concepts` tool, you can filter results by specific properties using the `property` parameter along with the `value` parameter.

**Important**: These properties can only be used when `terminology` is set to `'ncit'`.

## Property Categories

Properties are organized into logical categories for easier reference:

1. **Core Identifiers** - Basic naming and identification
2. **External Database References** - Links to other databases
3. **Gene and Protein Information** - Molecular biology references
4. **Chemical and Drug Information** - Pharmaceutical and chemical data
5. **Clinical and Medical Information** - Medical terminology and classifications
6. **Nutrition Information** - Dietary and nutritional properties
7. **Historical and Metadata** - Legacy and administrative properties
8. **Value Sets and Mappings** - Terminology management

---

## Core Identifiers

### P106 - Semantic_Type

**Code**: `P106`  
**Name**: `Semantic_Type`  
**Description**: UMLS semantic type classification for the concept. Commonly used for filtering by concept categories like 'Disease', 'Drug', etc.

**Common Values**:
- Disease or Syndrome
- Neoplastic Process
- Pharmacologic Substance
- Therapeutic or Preventive Procedure

---

### P107 - Display_Name

**Code**: `P107`  
**Name**: `Display_Name`  
**Description**: The human-readable name used for displaying the concept in user interfaces.

---

### P108 - Preferred_Name

**Code**: `P108`  
**Name**: `Preferred_Name`  
**Description**: The officially preferred name for the concept.

---

### P97 - DEFINITION

**Code**: `P97`  
**Name**: `DEFINITION`  
**Description**: The primary textual definition of the concept.

---

### P325 - ALT_DEFINITION

**Code**: `P325`  
**Name**: `ALT_DEFINITION`  
**Description**: Alternative definition of the concept from different sources or perspectives.

---

### P90 - FULL_SYN

**Code**: `P90`  
**Name**: `FULL_SYN`  
**Description**: Full synonym information including source and term type.

---

### P310 - Concept_Status

**Code**: `P310`  
**Name**: `Concept_Status`  
**Description**: Current status of the concept (e.g., active, retired, obsolete).

---

## External Database References

### P207 - UMLS_CUI

**Code**: `P207`  
**Name**: `UMLS_CUI`  
**Description**: Unified Medical Language System Concept Unique Identifier.

---

### P208 - NCI_META_CUI

**Code**: `P208`  
**Name**: `NCI_META_CUI`  
**Description**: NCI Metathesaurus Concept Unique Identifier.

---

### P100 - OMIM_Number

**Code**: `P100`  
**Name**: `OMIM_Number`  
**Description**: Online Mendelian Inheritance in Man (OMIM) number reference for genetic disorders and genes.

---

### P334 - ICD-O-3_Code

**Code**: `P334`  
**Name**: `ICD-O-3_Code`  
**Description**: International Classification of Diseases for Oncology, 3rd Edition code.

---

### P320 - OID

**Code**: `P320`  
**Name**: `OID`  
**Description**: Object Identifier for HL7 and other healthcare standards.

---

### P167 - Image_Link

**Code**: `P167`  
**Name**: `Image_Link`  
**Description**: URL link to associated images or visual representations of the concept.

---

### P171 - PubMedID_Primary_Reference

**Code**: `P171`  
**Name**: `PubMedID_Primary_Reference`  
**Description**: PubMed identifier for the primary research article or reference related to this concept.

---

### oboInOwl:hasDbXref - xRef

**Code**: `oboInOwl:hasDbXref`  
**Name**: `xRef`  
**Description**: Cross-reference to external database entries.

---

## Gene and Protein Information

### P101 - Homologous_Gene

**Code**: `P101`  
**Name**: `Homologous_Gene`  
**Description**: Reference to genes that share common evolutionary ancestry.

---

### P102 - GenBank_Accession_Number

**Code**: `P102`  
**Name**: `GenBank_Accession_Number`  
**Description**: GenBank accession number for DNA/RNA sequences.

---

### P321 - EntrezGene_ID

**Code**: `P321`  
**Name**: `EntrezGene_ID`  
**Description**: NCBI Entrez Gene database identifier.

---

### P93 - Swiss_Prot

**Code**: `P93`  
**Name**: `Swiss_Prot`  
**Description**: Swiss-Prot protein sequence database identifier.

---

### P96 - Gene_Encodes_Product

**Code**: `P96`  
**Name**: `Gene_Encodes_Product`  
**Description**: Product encoded by the gene (protein or RNA).

---

### P369 - HGNC_ID

**Code**: `P369`  
**Name**: `HGNC_ID`  
**Description**: HUGO Gene Nomenclature Committee identifier.

---

### P331 - NCBI_Taxon_ID

**Code**: `P331`  
**Name**: `NCBI_Taxon_ID`  
**Description**: NCBI Taxonomy database identifier for organisms.

---

### P332 - MGI_Accession_ID

**Code**: `P332`  
**Name**: `MGI_Accession_ID`  
**Description**: Mouse Genome Informatics accession identifier.

---

### P315 - SNP_ID

**Code**: `P315`  
**Name**: `SNP_ID`  
**Description**: Single Nucleotide Polymorphism identifier.

---

### P362 - miRBase_ID

**Code**: `P362`  
**Name**: `miRBase_ID`  
**Description**: miRBase database identifier for microRNA.

---

### P211 - GO_Annotation

**Code**: `P211`  
**Name**: `GO_Annotation`  
**Description**: Gene Ontology annotation for molecular function, biological process, or cellular component.

---

### P215 - KEGG_ID

**Code**: `P215`  
**Name**: `KEGG_ID`  
**Description**: Kyoto Encyclopedia of Genes and Genomes pathway identifier.

---

### P216 - BioCarta_ID

**Code**: `P216`  
**Name**: `BioCarta_ID`  
**Description**: BioCarta pathway database identifier.

---

### P367 - PID_ID

**Code**: `P367`  
**Name**: `PID_ID`  
**Description**: Pathway Interaction Database identifier.

---

### P316 - Relative_Enzyme_Activity

**Code**: `P316`  
**Name**: `Relative_Enzyme_Activity`  
**Description**: Relative enzymatic activity level or measurement.

---

## Chemical and Drug Information

### P210 - CAS_Registry

**Code**: `P210`  
**Name**: `CAS_Registry`  
**Description**: Chemical Abstracts Service Registry Number for chemical substances.

---

### P350 - Chemical_Formula

**Code**: `P350`  
**Name**: `Chemical_Formula`  
**Description**: Molecular formula of the chemical compound.

---

### P319 - FDA_UNII_Code

**Code**: `P319`  
**Name**: `FDA_UNII_Code`  
**Description**: FDA Unique Ingredient Identifier code.

---

### P317 - FDA_Table

**Code**: `P317`  
**Name**: `FDA_Table`  
**Description**: FDA regulatory table classification.

---

### P175 - NSC_Number

**Code**: `P175`  
**Name**: `NSC Number`  
**Description**: National Service Center number for chemical compounds in the NCI DTP (Developmental Therapeutics Program).

---

### P368 - CHEBI_ID

**Code**: `P368`  
**Name**: `CHEBI_ID`  
**Description**: Chemical Entities of Biological Interest database identifier.

---

### P302 - Accepted_Therapeutic_Use_For

**Code**: `P302`  
**Name**: `Accepted_Therapeutic_Use_For`  
**Description**: Accepted medical conditions or indications for therapeutic use.

---

### P333 - Use_For

**Code**: `P333`  
**Name**: `Use_For`  
**Description**: General usage or application of the concept.

---

### P399 - NCI_Drug_Dictionary_ID

**Code**: `P399`  
**Name**: `NCI_Drug_Dictionary_ID`  
**Description**: Identifier in the NCI Drug Dictionary.

---

## Clinical and Medical Information

### P363 - Neoplastic_Status

**Code**: `P363`  
**Name**: `Neoplastic_Status`  
**Description**: Whether the condition is neoplastic (cancerous) or non-neoplastic.

---

### P329 - PDQ_Open_Trial_Search_ID

**Code**: `P329`  
**Name**: `PDQ_Open_Trial_Search_ID`  
**Description**: Physician Data Query identifier for searching open clinical trials.

---

### P330 - PDQ_Closed_Trial_Search_ID

**Code**: `P330`  
**Name**: `PDQ_Closed_Trial_Search_ID`  
**Description**: Physician Data Query identifier for searching closed clinical trials.

---

### P400 - ClinVar_Variation_ID

**Code**: `P400`  
**Name**: `ClinVar_Variation_ID`  
**Description**: ClinVar database identifier for genetic variations.

---

### P371 - NICHD_Hierarchy_Term

**Code**: `P371`  
**Name**: `NICHD_Hierarchy_Term`  
**Description**: National Institute of Child Health and Human Development hierarchy classification term.

---

## Nutrition Information

### P358 - Nutrient

**Code**: `P358`  
**Name**: `Nutrient`  
**Description**: Indicates whether the substance is a nutrient.

---

### P359 - Micronutrient

**Code**: `P359`  
**Name**: `Micronutrient`  
**Description**: Indicates whether the substance is a micronutrient (vitamins, minerals).

---

### P360 - Macronutrient

**Code**: `P360`  
**Name**: `Macronutrient`  
**Description**: Indicates whether the substance is a macronutrient (carbohydrates, proteins, fats).

---

### P356 - Essential_Amino_Acid

**Code**: `P356`  
**Name**: `Essential_Amino_Acid`  
**Description**: Indicates whether the amino acid is essential in the diet.

---

### P357 - Essential_Fatty_Acid

**Code**: `P357`  
**Name**: `Essential_Fatty_Acid`  
**Description**: Indicates whether the fatty acid is essential in the diet.

---

### P351 - US_Recommended_Intake

**Code**: `P351`  
**Name**: `US_Recommended_Intake`  
**Description**: United States recommended daily intake amount.

---

### P352 - Tolerable_Level

**Code**: `P352`  
**Name**: `Tolerable_Level`  
**Description**: Maximum tolerable intake level before adverse effects.

---

### P353 - INFOODS

**Code**: `P353`  
**Name**: `INFOODS`  
**Description**: International Network of Food Data Systems identifier.

---

### P354 - USDA_ID

**Code**: `P354`  
**Name**: `USDA_ID`  
**Description**: United States Department of Agriculture nutrient database identifier.

---

### P355 - Unit

**Code**: `P355`  
**Name**: `Unit`  
**Description**: Unit of measurement for the substance or quantity.

---

## Historical and Metadata

### P200 - OLD_PARENT

**Code**: `P200`  
**Name**: `OLD_PARENT`  
**Description**: Historical reference to previous parent concepts before reclassification.

---

### P201 - OLD_CHILD

**Code**: `P201`  
**Name**: `OLD_CHILD`  
**Description**: Historical reference to previous child concepts before reclassification.

---

### P203 - OLD_KIND

**Code**: `P203`  
**Name**: `OLD_KIND`  
**Description**: Historical reference to previous concept kind classification.

---

### P204 - OLD_ROLE

**Code**: `P204`  
**Name**: `OLD_ROLE`  
**Description**: Historical reference to previous role classification.

---

### P364 - OLD_ASSOCIATION

**Code**: `P364`  
**Name**: `OLD_ASSOCIATION`  
**Description**: Historical reference to previous association relationships.

---

### P366 - Legacy Concept Name

**Code**: `P366`  
**Name**: `Legacy Concept Name`  
**Description**: Previous or legacy name for the concept.

---

### P322 - Contributing_Source

**Code**: `P322`  
**Name**: `Contributing_Source`  
**Description**: Organization or source that contributed the concept or information.

---

### P92 - Subsource

**Code**: `P92`  
**Name**: `Subsource`  
**Description**: Specific subsource within a larger contributing source.

---

### P98 - DesignNote

**Code**: `P98`  
**Name**: `DesignNote`  
**Description**: Design or editorial notes about the concept.

---

### owl:deprecated - deprecated

**Code**: `owl:deprecated`  
**Name**: `deprecated`  
**Description**: Indicates whether the concept has been deprecated.

---

## Value Sets and Mappings

### P372 - Publish_Value_Set

**Code**: `P372`  
**Name**: `Publish_Value_Set`  
**Description**: Indicates whether the concept is published as part of a value set.

---

### P374 - Value_Set_Location

**Code**: `P374`  
**Name**: `Value_Set_Location`  
**Description**: Location or URL where the value set can be accessed.

---

### P376 - Term_Browser_Value_Set_Description

**Code**: `P376`  
**Name**: `Term_Browser_Value_Set_Description`  
**Description**: Description of the value set as displayed in the term browser.

---

### P398 - Value_Set_Pair

**Code**: `P398`  
**Name**: `Value_Set_Pair`  
**Description**: Paired value set relationships.

---

### P375 - Maps_To

**Code**: `P375`  
**Name**: `Maps_To`  
**Description**: Mapping to concepts in other terminologies or coding systems.

---

### P361 - Extensible_List

**Code**: `P361`  
**Name**: `Extensible_List`  
**Description**: Indicates whether the list or value set is extensible.

---

## Usage Examples

### Example 1: Search by Semantic Type

Search for all concepts with Semantic_Type of "Disease or Syndrome":

```python
search_concepts(
    term="cancer",
    terminology="ncit",
    property=NCITProperty.SEMANTIC_TYPE,
    value="Disease or Syndrome"
)
```

### Example 2: Filter by CAS Registry Number

Find a chemical compound by its CAS Registry Number:

```python
search_concepts(
    term="",
    terminology="ncit",
    property=NCITProperty.CAS_REGISTRY,
    value="50-78-2"  # Aspirin
)
```

### Example 3: Search by Gene Symbol

Search for concepts related to a specific gene:

```python
search_concepts(
    term="BRCA1",
    terminology="ncit",
    property=NCITProperty.HGNC_ID,
    value="HGNC:1100"
)
```

### Example 4: Filter by FDA UNII Code

Find a drug by its FDA Unique Ingredient Identifier:

```python
search_concepts(
    term="",
    terminology="ncit",
    property=NCITProperty.FDA_UNII_CODE,
    value="R16CO5Y76E"  # Aspirin UNII
)
```

### Example 5: Search Active Concepts Only

Find active (non-deprecated) concepts:

```python
search_concepts(
    term="melanoma",
    terminology="ncit",
    property=NCITProperty.CONCEPT_STATUS,
    value="Concept_Status_Active"
)
```

### Example 6: Filter Neoplastic Concepts

Find only neoplastic (cancerous) conditions:

```python
search_concepts(
    term="tumor",
    terminology="ncit",
    property=NCITProperty.NEOPLASTIC_STATUS,
    value="Neoplastic"
)
```

## Notes

- Properties can be specified using either the code (e.g., `P106`) or the name (e.g., `Semantic_Type`)
- When using the `property` parameter with `search_concepts`, you should also provide a `value` parameter to filter by specific property values
- Not all concepts have values for all properties
- The `term` parameter works together with `property` and `value` to further restrict results
- Multiple properties can be used by making separate API calls and combining results
- Property values are case-sensitive in most cases

## Property Selection Tips

1. **For General Searching**: Use `Semantic_Type` to filter by broad categories
2. **For Clinical Use**: Use `ICD-O-3_Code`, `Concept_Status`, or `Neoplastic_Status`
3. **For Drugs**: Use `FDA_UNII_Code`, `CAS_Registry`, or `NCI_Drug_Dictionary_ID`
4. **For Genes**: Use `HGNC_ID`, `EntrezGene_ID`, or `GenBank_Accession_Number`
5. **For Chemicals**: Use `CAS_Registry`, `CHEBI_ID`, or `Chemical_Formula`
6. **For Cross-Referencing**: Use `UMLS_CUI`, `Maps_To`, or various database-specific IDs

## Related Tools

- **search_concepts**: Main tool for searching and filtering concepts using these properties
- **get_concepts**: Retrieve detailed information about specific concepts, including their property values

## Quick Reference: Most Commonly Used Properties

| Property | Code | Use Case |
|----------|------|----------|
| Semantic_Type | P106 | Filter by concept category |
| Display_Name | P107 | User-facing names |
| Preferred_Name | P108 | Official names |
| Concept_Status | P310 | Filter active/retired concepts |
| UMLS_CUI | P207 | Cross-reference to UMLS |
| CAS_Registry | P210 | Chemical identification |
| FDA_UNII_Code | P319 | Drug identification |
| ICD-O-3_Code | P334 | Cancer classification |
| Neoplastic_Status | P363 | Cancer vs non-cancer |
| HGNC_ID | P369 | Gene identification |
