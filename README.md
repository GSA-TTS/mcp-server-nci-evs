# NCI EVS MCP Server

A Model Context Protocol (MCP) server providing programmatic access to the National Cancer Institute (NCI) Enterprise Vocabulary Services (EVS) API. This server enables AI assistants and other MCP clients to search, navigate, and analyze cancer terminology and biomedical concepts from NCIT (NCI Thesaurus) and NCIM (NCI Metathesaurus).

## Overview

The NCI EVS API provides access to comprehensive cancer terminology, including:
- **NCIT (NCI Thesaurus)**: A standardized vocabulary for cancer research and clinical care
- **NCIM (NCI Metathesaurus)**: An integration of multiple biomedical vocabularies including UMLS, SNOMED CT, and more

This MCP server wraps the EVS REST API, making it easy for AI assistants to:
- Search for medical concepts and terminology
- Navigate hierarchical relationships between concepts
- Access detailed concept information including properties, definitions, and synonyms
- Explore mappings between different terminology systems

## Features

- 🔍 **Full-text search** across concepts with flexible filtering
- 🌳 **Hierarchy navigation** (parents, children, descendants)
- 📊 **Detailed concept information** with configurable detail levels
- 🏷️ **Property filtering** with 70+ NCIT and 185+ NCIM properties
- 📚 **Comprehensive documentation** via skill resources
- ⚡ **FastMCP-based** for high performance and easy deployment

## Installation

### Prerequisites

- Python 3.14+
- [uv](https://docs.astral.sh/uv/) - Fast Python package installer and resolver

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Setup

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/mcp-server-nci-evs.git
cd mcp-server-nci-evs

# Create virtual environment and install dependencies
uv sync
```

## Quick Start

### Running the Server

```bash
# Run with stdio transport (for MCP clients like Claude Desktop)
uv run python -m evs_server.app

# Run with HTTP transport (for web-based clients)
PORT=8000 uv run python -m evs_server.app

# Or activate the virtual environment first
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
python -m evs_server.app
```

### Configuration for Claude Desktop

Add to your Claude Desktop configuration:

```json
{
  "mcpServers": {
    "nci-evs": {
      "command": "uv",
      "args": ["run", "python", "-m", "evs_server.app"],
      "cwd": "/path/to/mcp-server-nci-evs"
    }
  }
}
```


## Available Tools

### 1. search_concepts

Search for concepts using flexible text queries and filters.

**Parameters:**
- `term`: Search term or phrase (e.g., "melanoma")
- `terminology`: Which terminology to search ('ncit' or 'ncim')
- `type`: Match type (contains, startsWith, phrase, exactMatch, fuzzy)
- `include`: Detail level (minimal, summary, full, or specific aspects)
- `property`: Filter by specific properties (see Property Skills below)
- `value`: Value to match for property filtering
- Plus many more filtering options

**Example:**
```python
# Simple search
search_concepts(term="melanoma", terminology="ncit")

# Search with filters
search_concepts(
    term="cancer",
    terminology="ncit",
    type="startsWith",
    include="summary",
    property=NCITProperty.SEMANTIC_TYPE,
    value="Disease or Syndrome"
)
```

### 2. get_concepts

Retrieve detailed information about one or more concepts by their codes.

**Parameters:**
- `terminology`: Terminology ('ncit' or 'ncim')
- `list`: Comma-separated list of concept codes
- `include`: Detail level to return

**Example:**
```python
# Get single concept
get_concepts(terminology="ncit", list="C3224")

# Get multiple concepts with full details
get_concepts(
    terminology="ncit",
    list="C3224,C2291,C9305",
    include="full"
)
```

### 3. get_children

Get direct child concepts (one level down in hierarchy).

**Parameters:**
- `terminology`: Terminology ('ncit' or 'ncim')
- `code`: Concept code

**Returns:** Dictionary with `children`, `count`, and `parameters`

**Example:**
```python
get_children(terminology="ncit", code="C3224")
```

### 4. get_parents

Get direct parent concepts (one level up in hierarchy).

**Parameters:**
- `terminology`: Terminology ('ncit' or 'ncim')
- `code`: Concept code

**Returns:** Dictionary with `parents`, `count`, and `parameters`

**Example:**
```python
get_parents(terminology="ncit", code="C3224")
```

### 5. get_descendants

Get all descendant concepts (entire subtree) with pagination and depth control.

**Parameters:**
- `terminology`: Terminology (primarily 'ncit')
- `code`: Concept code
- `fromRecord`: Start index for pagination (default: 0)
- `pageSize`: Max results per request (default: 50000)
- `maxLevel`: Max hierarchical depth (default: 10000)

**Returns:** Dictionary with `descendants`, `count`, and `parameters`

**Example:**
```python
# Get all descendants
get_descendants(terminology="ncit", code="C3224")

# Get descendants with pagination
get_descendants(
    terminology="ncit",
    code="C3224",
    fromRecord=0,
    pageSize=100,
    maxLevel=3
)
```


## Property Reference Skills

The server includes comprehensive documentation for all available property codes via MCP skill resources:

### NCIT Property Information
- **Resource:** `skill://ncit-property-information/SKILL.md`
- **Properties:** 70 documented
- **Categories:** Core identifiers, external database references, gene/protein info, chemicals/drugs, clinical coding, nutrition, historical metadata, value set mappings

### NCIM Property Information
- **Resource:** `skill://ncim-property-information/SKILL.md`
- **Properties:** 185+ documented
- **Categories:** Core identifiers, molecular biology, chemicals/drugs, clinical coding, anatomical/imaging, nutrition, terminology mappings, deprecation tracking, publication references, SNOMED CT modules

These skills provide detailed information about each property code including descriptions, common values, and usage examples.

## Common Use Cases

### 1. Search for a Disease

```python
# Find melanoma concepts
search_concepts(term="melanoma", terminology="ncit", include="summary")
```

### 2. Get Concept Details

```python
# Get full details for a specific concept
get_concepts(terminology="ncit", list="C3224", include="full")
```

### 3. Navigate Hierarchy

```python
# Get parent concepts
parents = get_parents(terminology="ncit", code="C3224")

# Get child concepts
children = get_children(terminology="ncit", code="C3224")

# Get all descendants up to 3 levels
descendants = get_descendants(
    terminology="ncit",
    code="C3224",
    maxLevel=3
)
```

### 4. Filter by Properties

```python
# Find all diseases (by semantic type)
search_concepts(
    term="",
    terminology="ncit",
    property=NCITProperty.SEMANTIC_TYPE,
    value="Disease or Syndrome"
)

# Find concept by CAS Registry Number
search_concepts(
    term="",
    terminology="ncit",
    property=NCITProperty.CAS_REGISTRY,
    value="50-78-2"  # Aspirin
)

# Find gene by HGNC ID
search_concepts(
    term="",
    terminology="ncit",
    property=NCITProperty.HGNC_ID,
    value="HGNC:1100"  # BRCA1
)
```

### 5. Cross-Terminology Mapping

```python
# Search in both NCIT and NCIM
search_concepts(
    term="diabetes",
    terminology="ncit,ncim",
    include="summary"
)

# Find SNOMED CT concepts in NCIM
search_concepts(
    term="hypertension",
    terminology="ncim",
    property=NCIMProperty.SNOMED_ID,
    value="73211009"
)
```


## NCIT vs NCIM: When to Use Each

### Use NCIT when:
- Working with NCI Thesaurus concepts
- Need standardized cancer terminology
- Working with US federal health data standards
- Need clean, curated terminology without source conflicts

### Use NCIM when:
- Need cross-terminology mapping
- Working with UMLS or SNOMED CT concepts
- Need multilingual support (German, Spanish)
- Need to trace concept origins from multiple source vocabularies
- Working with detailed drug dosage and strength information

## Project Structure

```
mcp-server-nci-evs/
├── src/
│   └── evs_server/
│       ├── app.py                 # Main MCP server
│       ├── tools/                 # Tool implementations
│       │   ├── search_concepts.py
│       │   ├── get_concepts.py
│       │   ├── get_children.py
│       │   ├── get_parents.py
│       │   └── get_descendants.py
│       ├── models/                # Data models and enums
│       │   ├── ncit_property.py
│       │   ├── ncim_property.py
│       │   ├── terminologies.py
│       │   └── ...
│       ├── utils/                 # Utility functions
│       └── skills/                # MCP skill resources
│           ├── ncit-property-information/
│           └── ncim-property-information/
├── tests/                         # Test suite
├── pyproject.toml                 # Project configuration
└── README.md                      # This file
```

## Development

### Running Tests

```bash
# Run tests with uv
uv run pytest tests/

# Or activate the virtual environment first
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pytest tests/
```

### Adding Dependencies

```bash
# Add a new dependency
uv add package-name

# Add a development dependency
uv add --dev package-name

# Update dependencies
uv sync
```

### Adding New Tools

1. Create a new file in `src/evs_server/tools/`
2. Implement the tool following the existing pattern
3. Register it in `src/evs_server/tools/__init__.py`

Example:
```python
# src/evs_server/tools/my_tool.py
from fastmcp import FastMCP
import httpx

def register(mcp: FastMCP) -> None:
    @mcp.tool(name="my_tool")
    async def my_tool(param: str) -> dict:
        """Tool description."""
        # Implementation
        pass
```

## API Reference

This server uses the NCI EVS REST API:
- **Base URL:** https://api-evsrest.nci.nih.gov/api/v1
- **Documentation:** https://api-evsrest.nci.nih.gov/
- **Swagger UI:** https://api-evsrest.nci.nih.gov/swagger-ui.html

## Acknowledgments

- National Cancer Institute (NCI) for providing the EVS API
- FastMCP framework for MCP server implementation
- The broader MCP community

## Resources

- [NCI EVS API Documentation](https://api-evsrest.nci.nih.gov/)
- [NCI Thesaurus Browser](https://ncit.nci.nih.gov/ncitbrowser/)
- [FastMCP Documentation](https://gofastmcp.com/)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)

## Support

For issues and questions:
- Open an issue on GitHub
- Refer to the NCI EVS API documentation for API-related questions
- Check the property information skills for detailed property documentation

