# Document Processing

## Overview

Empire Chain provides powerful document processing capabilities through its `Docling` module. This guide covers how to process different types of documents and extract meaningful information from them.

## Supported Document Types

- PDF Documents
- Text Files
- Images (with OCR)
- Word Documents
- HTML Pages

## Basic Document Processing

### Loading Documents

```python
from empire_chain.docling import Docling

# Load a PDF document
pdf_doc = Docling("document.pdf")

# Load a text file
text_doc = Docling("document.txt")

# Load from bytes
doc = Docling(bytes_content, content_type="application/pdf")
```

### Text Extraction

```python
# Extract all text
text = doc.extract_text()

# Extract text from specific pages
text = doc.extract_text(pages=[1, 3, 5])

# Extract with layout preservation
text = doc.extract_text(preserve_layout=True)
```

### Document Analysis

```python
# Get document metadata
metadata = doc.get_metadata()

# Analyze document structure
structure = doc.analyze_structure()

# Extract tables
tables = doc.extract_tables()
```

## Advanced Features

### OCR Processing

```python
# Enable OCR for image-based PDFs
doc = Docling("scanned.pdf", config={"ocr_enabled": True})

# Extract text with OCR
text = doc.extract_text()
```

### Document Transformation

```python
# Convert to different format
doc.convert_to("docx")

# Split document
doc.split(pages=[1, 3, 5])

# Merge documents
Docling.merge(["doc1.pdf", "doc2.pdf"], output="merged.pdf")
```

### Content Extraction

```python
# Extract images
images = doc.extract_images()

# Extract tables to pandas DataFrame
tables = doc.extract_tables(output_format="pandas")

# Extract specific regions
content = doc.extract_region(bbox=(100, 100, 500, 500))
```

## Best Practices

1. **Memory Management**
   ```python
   with Docling("large.pdf") as doc:
       text = doc.extract_text()
   ```

2. **Error Handling**
   ```python
   try:
       doc = Docling("document.pdf")
       text = doc.extract_text()
   except DocumentError as e:
       print(f"Error processing document: {e}")
   ```

3. **Batch Processing**
   ```python
   from empire_chain.docling import BatchProcessor
   
   processor = BatchProcessor()
   results = processor.process_directory("docs/")
   ```

## Configuration Options

```python
config = {
    "ocr": {
        "enabled": True,
        "language": "eng",
        "dpi": 300
    },
    "extraction": {
        "preserve_layout": True,
        "include_images": False
    },
    "processing": {
        "chunk_size": 1000,
        "max_workers": 4
    }
}

doc = Docling("document.pdf", config=config)
``` 