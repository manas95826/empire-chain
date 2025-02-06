# Vector Stores

Empire Chain provides robust vector store implementations for efficient similarity search and retrieval. The primary implementation is based on Qdrant, a high-performance vector database.

## QdrantVectorStore

The `QdrantVectorStore` class provides a simple interface for storing and querying text embeddings with sensible defaults.

### Quick Start

```python
from empire_chain.vector_stores import QdrantVectorStore
from empire_chain.embeddings import OpenAIEmbeddings

# Initialize components
store = QdrantVectorStore()
embeddings = OpenAIEmbeddings("text-embedding-3-small")

# Add text with its embedding
text = "Hello world"
text_embedding = embeddings.embed(text)
store.add(text=text, embedding=text_embedding)

# Query similar texts
query = "What is this about?"
query_embedding = embeddings.embed(query)
similar_texts = store.query(query_embedding)  # Returns top 10 similar texts
```

### Default Configuration

The `QdrantVectorStore` comes with carefully chosen defaults suitable for most use cases:

#### Basic Settings
- Storage: In-memory (uses local memory)
- Collection name: "default"
- Vector size: 1536 (compatible with many embedding models)
- Distance metric: COSINE
- Storage type: RAM (not on disk)
- Query results: Top 10 by default
- Point IDs: Automatically generated UUIDs

#### HNSW Index Settings
- m: 16 (edges per node)
- ef_construct: 100 (candidates for index construction)
- full_scan_threshold: 10000
- max_indexing_threads: Auto-detected
- on_disk: False (stored in RAM)

#### Optimizer Settings
- deleted_threshold: 0.2
- vacuum_min_vector_number: 1000
- indexing_threshold: 20000
- flush_interval_sec: 5
- max_optimization_threads: Auto-detected

#### WAL (Write-Ahead-Log) Settings
- wal_capacity_mb: 32
- wal_segments_ahead: 0

### Advanced Usage

For more control over the vector store configuration:

```python
from empire_chain.vector_stores import QdrantVectorStore
from qdrant_client.models import Distance

# Create a store with custom settings
store = QdrantVectorStore(
    url="localhost:6333",            # Qdrant server URL
    collection_name="my_vectors",    # Custom collection name
    vector_size=768,                 # For smaller embeddings
    distance=Distance.EUCLID,        # Euclidean distance
    on_disk=True,                    # Store vectors on disk
)

# Add text with its embedding
store.add(
    text="Important document",
    embedding=[...],  # Your embedding
)

# Query with filters and threshold
similar_texts = store.query(
    query_embedding=[...],           # Your query embedding
    k=5,                            # Return top 5 results
    score_threshold=0.8,            # Minimum similarity score
    filter={"category": "important"} # Optional filtering
)
```

### Production Recommendations

When using QdrantVectorStore in production:

1. **Storage Configuration**
   - Use a persistent Qdrant server instead of in-memory storage
   - Consider enabling on-disk storage for large datasets
   - Configure proper backup and snapshot strategies

2. **Performance Optimization**
   - Adjust HNSW index parameters based on your dataset size
   - Use appropriate vector size for your embedding model
   - Consider enabling vector quantization for large collections

3. **Resource Management**
   - Monitor memory usage and disk space
   - Configure appropriate shard numbers for distributed setups
   - Set up proper replication for high availability

### Integration with RAG

QdrantVectorStore works seamlessly with the RAG (Retrieval-Augmented Generation) pipeline:

```python
from empire_chain.vector_stores import QdrantVectorStore
from empire_chain.embeddings import OpenAIEmbeddings
from empire_chain.llms import OpenAILLM

# Initialize components
store = QdrantVectorStore()
embeddings = OpenAIEmbeddings()
llm = OpenAILLM()

# Add documents to the store
documents = ["doc1", "doc2", "doc3"]
for doc in documents:
    embedding = embeddings.embed(doc)
    store.add(doc, embedding)

# Query and generate
query = "What are the key points?"
query_embedding = embeddings.embed(query)
relevant_docs = store.query(query_embedding, k=3)
response = llm.generate(f"Context: {relevant_docs}\nQuery: {query}")
```

### Error Handling

The QdrantVectorStore implements robust error handling:

```python
try:
    store = QdrantVectorStore()
    store.add(text="example", embedding=[...])
except RuntimeError as e:
    print(f"Failed to add text: {e}")
```

Common errors are handled gracefully with descriptive error messages.

### Best Practices

1. **Vector Normalization**
   - Always normalize embeddings when using COSINE distance
   - Use consistent embedding dimensions

2. **Performance**
   - Batch operations when adding multiple points
   - Use appropriate index settings for your dataset size
   - Consider payload size impact on performance

3. **Resource Management**
   - Monitor memory usage with large collections
   - Use disk storage for large datasets
   - Implement proper cleanup procedures

4. **Security**
   - Use proper authentication in production
   - Implement access controls
   - Regular backup procedures

For more examples and advanced usage, check out the [cookbooks](https://github.com/manas95826/empire-chain/tree/main/cookbooks) in the repository. 