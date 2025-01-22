# Installation Guide

## Requirements

Empire Chain requires Python 3.10 or later.

## Installation

You can install Empire Chain using pip:

```bash
pip install empire-chain
```

## Dependencies

Empire Chain comes with the following core dependencies:

### LLM Providers
- `openai` - OpenAI API client
- `anthropic` - Anthropic API client
- `groq` - Groq API client

### Vector Stores
- `qdrant-client` - Qdrant vector database client
- `chromadb` - ChromaDB vector database
- `sentence-transformers` - For embeddings generation

### Document Processing
- `PyPDF2` - PDF processing
- `python-docx` - Word document processing
- `docling` - Document analysis

### Web and Data
- `crawl4ai` - Web crawling
- `duckduckgo-search` - Web search capabilities
- `yfinance` - Financial data access

### Visualization and UI
- `streamlit` - Interactive UI components
- `matplotlib` - Data visualization
- `Pillow` - Image processing

### Audio Processing
- `soundfile` - Audio file handling
- `kokoro_onnx` - Speech processing

### Utilities
- `phidata` - Agent framework
- `python-dotenv` - Environment management
- `numpy` - Numerical computations
- `tqdm` - Progress bars

## Environment Setup

1. Create a `.env` file in your project root:

```bash
touch .env
```

2. Add your API keys (as needed):

```env
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
GROQ_API_KEY=your_groq_key
```

## Verifying Installation

You can verify your installation by running:

```python
from empire_chain.llms import OpenAILLM
from empire_chain.vector_stores import QdrantVectorStore
from empire_chain.embeddings import OpenAIEmbeddings

# These imports should work without errors if installation is successful
```

## Next Steps

- Check out the [Quick Start Guide](quickstart.md) to begin using Empire Chain
- Explore [Example Cookbooks](../tutorials/empire-rag.md) for practical examples
- Read about [Core Concepts](../user-guide/core-concepts.md) to understand the framework 