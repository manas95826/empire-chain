# RAG (Retrieval-Augmented Generation)

Empire Chain provides a powerful RAG implementation that combines document processing, vector stores, and LLMs for enhanced question-answering capabilities.

## Basic Usage

```python
from empire_chain.vector_stores import QdrantVectorStore
from empire_chain.embeddings import OpenAIEmbeddings
from empire_chain.llms.llms import GroqLLM
from empire_chain.tools.file_reader import DocumentReader
from empire_chain.stt.stt import GroqSTT

# Initialize components
vector_store = QdrantVectorStore(":memory:")
embeddings = OpenAIEmbeddings("text-embedding-3-small")
llm = GroqLLM("llama3-8b-8192")
reader = DocumentReader()

# Read and process document
file_path = "input.pdf"
text = reader.read(file_path)

# Create and store embeddings
text_embedding = embeddings.embed(text)
vector_store.add(text, text_embedding)

# Process query
text_query = "What is the main topic of this document?"
query_embedding = embeddings.embed(text_query)
relevant_texts = vector_store.query(query_embedding, k=3)

# Generate response
context = "\n".join(relevant_texts)
prompt = f"Based on the following context, {text_query}\n\nContext: {context}"
response = llm.generate(prompt)
```

## Audio Input Support

Empire Chain's RAG system also supports audio input through speech-to-text conversion:

```python
# Initialize STT
stt = GroqSTT()

# Convert audio to text
audio_query = stt.transcribe("audio.mp3")
query_embedding = embeddings.embed(audio_query)

# Process as before...
```

## Supported Components

- **Vector Stores**: Qdrant, ChromaDB
- **Embeddings**: OpenAI, HuggingFace
- **LLMs**: OpenAI, Anthropic, Groq
- **Document Types**: PDF, DOCX, TXT, JSON, CSV, Google Drive files

For more examples and advanced usage, check out the RAG cookbooks in the repository. 