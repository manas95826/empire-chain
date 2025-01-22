# Vector Stores API Reference

The `empire_chain.vector_stores` module provides interfaces to various vector databases for efficient similarity search.

## QdrantVectorStore

```python
from empire_chain.vector_stores import QdrantVectorStore
```

Class for interacting with Qdrant vector database.

### Constructor

```python
QdrantVectorStore(location: str = ":memory:", collection_name: str = "default")
```

**Parameters:**
- `location` (str): Location of the Qdrant database
  - `:memory:` for in-memory storage
  - URL or path for persistent storage
- `collection_name` (str): Name of the collection to use

### Methods

#### add()

```python
def add(self, text: str, embedding: List[float]) -> None
```

Add text and its embedding to the store.

**Parameters:**
- `text` (str): The text to store
- `embedding` (List[float]): Vector representation of the text

**Example:**
```python
store = QdrantVectorStore(":memory:")
store.add("Sample text", embedding_vector)
```

#### query()

```python
def query(self, embedding: List[float], k: int = 3) -> List[str]
```

Retrieve similar texts based on embedding.

**Parameters:**
- `embedding` (List[float]): Query vector
- `k` (int): Number of results to return

**Returns:**
- List[str]: List of similar texts

**Example:**
```python
similar_texts = store.query(query_embedding, k=5)
```

#### delete()

```python
def delete(self, ids: List[str]) -> None
```

Delete entries by their IDs.

**Parameters:**
- `ids` (List[str]): List of IDs to delete

#### clear()

```python
def clear(self) -> None
```

Clear all entries from the store.

## ChromaVectorStore

```python
from empire_chain.vector_stores import ChromaVectorStore
```

Class for interacting with ChromaDB.

### Constructor

```python
ChromaVectorStore(path: Optional[str] = None, collection_name: str = "default")
```

**Parameters:**
- `path` (Optional[str]): Path for persistent storage
- `collection_name` (str): Name of the collection

### Methods

#### add()

```python
def add(self, text: str, embedding: List[float]) -> None
```

Add text and its embedding to ChromaDB.

**Parameters:**
- `text` (str): The text to store
- `embedding` (List[float]): Vector representation of the text

**Example:**
```python
store = ChromaVectorStore()
store.add("Sample text", embedding_vector)
```

#### query()

```python
def query(self, embedding: List[float], k: int = 3) -> List[str]
```

Retrieve similar texts from ChromaDB.

**Parameters:**
- `embedding` (List[float]): Query vector
- `k` (int): Number of results to return

**Returns:**
- List[str]: List of similar texts

**Example:**
```python
similar_texts = store.query(query_embedding, k=5)
```

## Common Usage Patterns

### Basic RAG Setup

```python
from empire_chain.vector_stores import QdrantVectorStore
from empire_chain.embeddings import OpenAIEmbeddings

# Initialize components
store = QdrantVectorStore(":memory:")
embeddings = OpenAIEmbeddings("text-embedding-3-small")

# Add documents
text = "Your document text here"
embedding = embeddings.embed(text)
store.add(text, embedding)

# Query
query = "Your query here"
query_embedding = embeddings.embed(query)
results = store.query(query_embedding, k=3)
```

### Persistent Storage

```python
# Qdrant with persistent storage
qdrant_store = QdrantVectorStore(
    location="path/to/storage",
    collection_name="my_documents"
)

# ChromaDB with persistent storage
chroma_store = ChromaVectorStore(
    path="path/to/storage",
    collection_name="my_documents"
)
```

### Error Handling

```python
try:
    store = QdrantVectorStore(":memory:")
    store.add(text, embedding)
except Exception as e:
    print(f"Error: {e}")
```

## Best Practices

1. **Memory Management**
   ```python
   # For development/testing
   store = QdrantVectorStore(":memory:")
   
   # For production
   store = QdrantVectorStore("path/to/persistent/storage")
   ```

2. **Batch Operations**
   ```python
   # Add multiple documents efficiently
   for text, embedding in zip(texts, embeddings):
       store.add(text, embedding)
   ```

3. **Collection Management**
   ```python
   # Use separate collections for different purposes
   docs_store = QdrantVectorStore(collection_name="documents")
   qa_store = QdrantVectorStore(collection_name="qa_pairs")
   ``` 