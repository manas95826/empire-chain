# Tools

Empire Chain provides a collection of utility tools for various tasks.

## File Reader

A versatile document reader supporting multiple file formats:

```python
from empire_chain.tools.file_reader import DocumentReader

reader = DocumentReader()

# Read from Google Drive
text = reader.read("https://drive.google.com/file/d/1t0Itw6oGO2iVusp=sharing")

# Read local PDF
text = reader.read("input.pdf")
```

Supported file formats:
- PDF files (.pdf)
- Microsoft Word documents (.docx)
- Text files (.txt)
- JSON files (.json)
- CSV files (.csv)
- Google Drive files (.gdrive)

## Website Crawler

Crawl websites and extract content in various formats:

```python
from empire_chain.tools.crawl4ai import Crawler

crawler = Crawler()
content = crawler.crawl(
    url="https://www.example.com",
    format="markdown"
)
```

## Speech to Text

Convert audio to text using different providers:

```python
from empire_chain.stt.stt import GroqSTT, HuggingFaceSTT

# Using Groq
groq_stt = GroqSTT()
text = groq_stt.transcribe("audio.mp3")

# Using HuggingFace
hf_stt = HuggingFaceSTT()
text = hf_stt.transcribe("audio.mp3")
```

## Installation

```bash
# Base installation
pip install empire-chain

# Crawler dependencies
pip install crawl4ai

# Speech-to-text dependencies
pip install kokoro_onnx  # Note: Model download may take time
```

For more examples and advanced usage, check out the tools cookbooks in the repository. 