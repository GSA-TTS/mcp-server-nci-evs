# EVS MCP Server Skills

This directory contains skill documentation for the NCI EVS (Enterprise Vocabulary Services) MCP server. Skills provide detailed reference information about properties that can be used when searching and filtering concepts through the EVS API.

## Available Skills

### 1. NCIT Property Information
**Location**: `ncit-property-information/SKILL.md`  
**Size**: 16KB  
**Properties Documented**: 70

Reference guide for NCI Thesaurus (NCIT) property codes. Use this when working with `terminology="ncit"` in the search_concepts tool.

**Key Categories**:
- Core Identifiers (Display_Name, Preferred_Name, Semantic_Type, etc.)
- External Database References (UMLS_CUI, OMIM_Number, ICD-O-3_Code, etc.)
- Gene and Protein Information (HGNC_ID, EntrezGene_ID, GenBank_Accession_Number, etc.)
- Chemical and Drug Information (CAS_Registry, FDA_UNII_Code, Chemical_Formula, etc.)
- Clinical and Medical Information (Neoplastic_Status, ClinVar_Variation_ID, etc.)
- Nutrition Information (Nutrient, Micronutrient, US_Recommended_Intake, etc.)
- Historical and Metadata (OLD_PARENT, Legacy Concept Name, Contributing_Source, etc.)
- Value Sets and Mappings (Publish_Value_Set, Maps_To, Value_Set_Pair, etc.)

### 2. NCIM Property Information
**Location**: `ncim-property-information/SKILL.md`  
**Size**: 28KB  
**Properties Documented**: 185+

Reference guide for NCI Metathesaurus (NCIM) property codes. Use this when working with `terminology="ncim"` in the search_concepts tool.

**Key Categories**:
- Core Identifiers and Metadata (CODE, Semantic_Type, ACTIVE, etc.)
- Gene and Molecular Biology (AA_GI, CDNA_REFSEQ, GenBank_Accession_Number, etc.)
- Chemical and Drug Information (CAS_Registry, FDA_UNII_CODE, drug strength properties, etc.)
- Clinical and Medical Coding (SNOMED_ID, ICD-O-3_Code, ClinVar_Variation_ID, etc.)
- Anatomical and Imaging (FMAID, TALAIRACH, FREESURFER, JHU atlases, etc.)
- Nutrition and Food Data (Nutrient, USDA_ID, US_Recommended_Intake, etc.)
- Terminology Management and Mapping (MAPSET*, MTH_MAP*, UMLSREL, etc.)
- Deprecation and Version Control (DEPRECATION_*, REPLACED_BY, EFFECTIVE_TIME, etc.)
- Publication and Reference Data (PubMedID, HAS_AUTHORS, HAS_PUBLICATION, etc.)
- SNOMED CT and Module Properties (MODULE_ID, DEFINITION_STATUS_ID, etc.)

## Usage

These skills are designed to be exposed as MCP resources through a Skills Provider. They provide comprehensive reference documentation for all available property codes in both NCIT and NCIM terminologies.

### When to Use NCIT vs NCIM

**Use NCIT** (`terminology="ncit"`) when:
- Working with NCI Thesaurus concepts
- Need standardized cancer terminology
- Working with US federal health data standards
- Need clean, curated terminology without source conflicts

**Use NCIM** (`terminology="ncim"`) when:
- Need cross-terminology mapping
- Working with UMLS or SNOMED CT concepts
- Need multilingual support (German, Spanish)
- Need to trace concept origins from multiple source vocabularies
- Working with detailed drug dosage and strength information

## Integration with MCP Server

To expose these skills as MCP resources, use FastMCP's Skills Provider:

```python
from pathlib import Path
from fastmcp import FastMCP
from fastmcp.server.providers.skills import SkillsDirectoryProvider

mcp = FastMCP("EVS Server")
mcp.add_provider(SkillsDirectoryProvider(
    roots=Path(__file__).parent / "skills"
))
```

This will expose resources like:
- `skill://ncit-property-information/SKILL.md`
- `skill://ncim-property-information/SKILL.md`

## Quick Reference

### Most Common NCIT Properties
- `P106` (Semantic_Type) - Concept category
- `P107` (Display_Name) - User-facing name
- `P310` (Concept_Status) - Active/retired status
- `P207` (UMLS_CUI) - UMLS identifier
- `P334` (ICD-O-3_Code) - Cancer classification

### Most Common NCIM Properties
- `Semantic_Type` - Concept category
- `CODE` - Source vocabulary code
- `ACTIVE` - Active/inactive status
- `SNOMED_ID` - SNOMED CT identifier
- `MODULE_ID` - SNOMED CT module

## Related Tools

- **search_concepts**: Search and filter concepts using these properties
- **get_concepts**: Retrieve detailed concept information including property values
