# Quick Start Guide

This guide will help you get started with Empire Chain by walking through some basic examples.

## Basic Usage

### 1. Simple Chatbot

Create a basic chatbot using Empire Chain:

```python
from empire_chain.docling import SimpleChatbot

# Initialize the chatbot
chatbot = SimpleChatbot()

# Start a conversation
response = chatbot.chat("Tell me about artificial intelligence")
print(response)
```

### 2. Processing a PDF Document

```python
from empire_chain.docling import PDFProcessor

# Initialize the PDF processor
processor = PDFProcessor("path/to/document.pdf")

# Extract text content
text = processor.extract_text()

# Get a summary
summary = processor.summarize()
```

### 3. Chat with Images

```python
from empire_chain.docling import ImageChat

# Initialize the image chat
image_chat = ImageChat()

# Load and analyze an image
response = image_chat.analyze_image(
    "path/to/image.jpg",
    "What can you tell me about this image?"
)
print(response)
```

### 4. Visualization Example

```python
from empire_chain.visualizer import DataVisualizer
import pandas as pd

# Create sample data
data = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [2, 4, 6, 8, 10]
})

# Initialize visualizer
viz = DataVisualizer(data)

# Create a line plot
viz.line_plot('x', 'y', title='Sample Plot')
```

## Building a RAG Application

Here's a complete example of building a Retrieval Augmented Generation (RAG) system:

```python
from empire_chain.docling import RAGSystem
from empire_chain.visualizer import RAGVisualizer

# Initialize the RAG system
rag = RAGSystem()

# Add documents to the knowledge base
rag.add_documents([
    "path/to/doc1.pdf",
    "path/to/doc2.pdf"
])

# Query the system
response = rag.query("What are the key findings in these documents?")

# Visualize the retrieval process
viz = RAGVisualizer(rag)
viz.show_retrieval_path()
```

## Next Steps

- Explore the [Core Concepts](../user-guide/core-concepts.md) to understand the framework better
- Check out the [Tutorials](../tutorials/simple-chatbot.md) for more detailed examples
- Read the [API Reference](../api-reference/docling.md) for comprehensive documentation

## Common Patterns

### Error Handling

```python
from empire_chain.docling import SimpleChatbot
from empire_chain.exceptions import EmpireChainError

try:
    chatbot = SimpleChatbot()
    response = chatbot.chat("Hello")
except EmpireChainError as e:
    print(f"An error occurred: {e}")
```

### Configuration

```python
from empire_chain.docling import SimpleChatbot

config = {
    "model": "gpt-3.5-turbo",
    "temperature": 0.7,
    "max_tokens": 150
}

chatbot = SimpleChatbot(config=config)
```

### Async Support

```python
import asyncio
from empire_chain.docling import AsyncChatbot

async def main():
    chatbot = AsyncChatbot()
    response = await chatbot.achat("Tell me a story")
    print(response)

asyncio.run(main())
``` 