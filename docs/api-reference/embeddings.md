# Embeddings Module API Reference

The `empire_chain.embeddings` module provides interfaces to various embedding model providers.

## OpenAIEmbeddings

```python
from empire_chain.embeddings import OpenAIEmbeddings
```

Class for generating text embeddings using OpenAI's models.

### Constructor

```python
OpenAIEmbeddings(model_name: str = "text-embedding-ada-002")
```

**Parameters:**
- `model_name` (str): The OpenAI embedding model to use. Options include:
  - `"text-embedding-ada-002"`
  - `"text-embedding-3-small"`
  - `"text-embedding-3-large"`

### Methods

#### embed()

```python
def embed(self, text: str) -> List[float]
```

Generate an embedding for a given text input.

**Parameters:**
- `text` (str): The input text for generating embeddings.

**Returns:**
- `List[float]`: The generated embedding vector.

**Example:**
```python
embedder = OpenAIEmbeddings("text-embedding-ada-002")
embedding = embedder.embed("I like to play football.")
```

## HFEmbeddings

```python
from empire_chain.embeddings import HFEmbeddings
```

Class for generating text embeddings using Hugging Face sentence-transformers **locally**.

### Constructor

```python
HFEmbeddings(model_name: str = "all-MiniLM-L6-v2")
```

**Parameters:**
- `model_name` (str): The local Hugging Face model to use. Options include:
  - `"all-MiniLM-L6-v2"`
  - `"all-mpnet-base-v2"`

### Methods

#### embed()

```python
def embed(self, text: str) -> List[float]
```

Generate an embedding for a given text input.

**Parameters:**
- `text` (str): The input text for generating embeddings.

**Returns:**
- `List[float]`: The generated embedding vector.

**Example:**
```python
embedder = HFEmbeddings("all-MiniLM-L6-v2")
embedding = embedder.embed("He is a good boy.")
```

## HFAPIEmbeddings

```python
from empire_chain.embeddings import HFAPIEmbeddings
```

Class for generating text embeddings using the **hosted** Hugging Face embeddiing models.

### Constructor

```python
HFAPIEmbeddings(model_name: str = "all-MiniLM-L6-v2")
```

**Parameters:**
- `model_name` (str): The hosted Hugging Face model to use. Options include:
  - `"sentence-transformers/all-MiniLM-L6-v2"`
  - `"thenlper/gte-large"`

### Methods

#### embed()

```python
def embed(self, text: str) -> List[float]
```

Generate an embedding for a given text input using Hugging Face's hosted API.

**Parameters:**
- `text` (str): The input text for generating embeddings.

**Returns:**
- `List[float]`: The generated embedding vector.

**Example:**
```python
embedder = HFAPIEmbeddings("all-MiniLM-L6-v2")
embedding = embedder.embed("Machine Learning is amazing!")
```

## Common Features

All embedding classes share these common features:

### Error Handling

```python
try:
    embedder = OpenAIEmbeddings()
    embedding = embedder.embed("sample text")
except Exception as e:
    print(f"Error: {e}")
```

### Environment Variables

Required environment variables:
- OpenAI: `OPENAI_API_KEY`
- Hugging Face API: `HUGGINGFACE_API_KEY`

### Best Practices

1. **Model Selection**
   ```python
   # For high-performance embedding models by OpenAI
   embedder = OpenAIEmbeddings("text-embedding-ada-002")
   
   # For running locally (by Hugging Face sentence transformers)   
   embedder = HFEmbeddings("all-MiniLM-L6-v2")
   
   # For hosted embeddings via HuggingFace inference API
   embedder = HFAPIEmbeddings("sentence-transformers/all-MiniLM-L6-v2")
   ```

2. **Error Handling**
   ```python
   try:
       embedding = embedder.embed("sample text")
   except Exception as e:
       # Handle specific error types
       pass
   ```

3. **Environment Setup**
   ```python
   from dotenv import load_dotenv
   load_dotenv()  # Load API keys from .env
   ```

