# Building a RAG System

This tutorial will guide you through building a Retrieval Augmented Generation (RAG) system using Empire Chain.

## Overview

In this tutorial, we'll build a RAG system that can:
- Process PDF documents
- Convert audio queries to text
- Retrieve relevant information
- Generate contextual responses

## Prerequisites

- Empire Chain installed
- API keys configured in `.env`
- Sample PDF document
- (Optional) Audio file for voice queries

## Step-by-Step Implementation

### 1. Import Required Components

```python
from empire_chain.vector_stores import QdrantVectorStore
from empire_chain.embeddings import OpenAIEmbeddings
from empire_chain.llms import OpenAILLM
from empire_chain.file_reader import DocumentReader
from empire_chain.stt import GroqSTT
from dotenv import load_dotenv
```

### 2. Initialize Components

```python
load_dotenv()  # Load environment variables

# Initialize core components
vector_store = QdrantVectorStore(":memory:")  # In-memory vector store
embeddings = OpenAIEmbeddings("text-embedding-3-small")
llm = OpenAILLM("gpt-4")
reader = DocumentReader()
```

### 3. Process Document

```python
# Read and process the document
file_path = "input.pdf"
text = reader.read(file_path)

# Create and store embeddings
text_embedding = embeddings.embed(text)
vector_store.add(text, text_embedding)
```

### 4. Handle Queries

```python
# Text query
text_query = "What is the main topic of this document?"

# Optional: Audio query processing
stt = GroqSTT()
audio_query = stt.transcribe("audio.mp3")  # If using voice input

# Create query embedding
query_embedding = embeddings.embed(audio_query)  # or text_query
```

### 5. Retrieve and Generate

```python
# Retrieve relevant context
relevant_texts = vector_store.query(query_embedding, k=3)
context = "\n".join(relevant_texts)

# Generate response
prompt = f"Based on the following context, {text_query}\n\nContext: {context}"
response = llm.generate(prompt)

print(f"Query: {text_query}")
print(f"Response: {response}")
```

## Complete Example

Here's the complete code that puts everything together:

```python
from empire_chain.vector_stores import QdrantVectorStore
from empire_chain.embeddings import OpenAIEmbeddings
from empire_chain.llms import OpenAILLM
from empire_chain.file_reader import DocumentReader
from empire_chain.stt import GroqSTT
from dotenv import load_dotenv

def main():
    load_dotenv()
    
    # Initialize components
    vector_store = QdrantVectorStore(":memory:")
    embeddings = OpenAIEmbeddings("text-embedding-3-small")
    llm = OpenAILLM("gpt-4")
    reader = DocumentReader()
    
    # Process document
    file_path = "input.pdf"
    text = reader.read(file_path)
    text_embedding = embeddings.embed(text)
    vector_store.add(text, text_embedding)
    
    # Handle query
    text_query = "What is the main topic of this document?"
    stt = GroqSTT()
    audio_query = stt.transcribe("audio.mp3")
    query_embedding = embeddings.embed(audio_query)
    
    # Retrieve and generate
    relevant_texts = vector_store.query(query_embedding, k=3)
    context = "\n".join(relevant_texts)
    prompt = f"Based on the following context, {text_query}\n\nContext: {context}"
    response = llm.generate(prompt)
    
    print(f"Query: {text_query}")
    print(f"Response: {response}")

if __name__ == "__main__":
    main()
```

## Customization Options

- Change vector store implementation: Use `ChromaVectorStore` instead of `QdrantVectorStore`
- Adjust retrieval parameters: Modify `k` value in `vector_store.query()`
- Use different LLM models: Switch between OpenAI, Anthropic, or Groq
- Customize prompt template: Modify the prompt format for different use cases

## Next Steps

- Try the [Chat with PDF](chat-with-pdf.md) tutorial for an interactive interface
- Explore [Data Visualization](visualize_data.md) for analyzing results
- Learn about [Vector Stores](../user-guide/vector-stores.md) in depth 