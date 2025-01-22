# Chat with PDF Tutorial

This tutorial will show you how to create an interactive chatbot that can answer questions about PDF documents.

## Overview

The PDF chatbot combines several Empire Chain components:
- Document processing for PDF files
- Vector store for efficient retrieval
- LLM for generating responses
- Streamlit interface for interaction

## Prerequisites

- Empire Chain installed
- API keys configured in `.env`
- PDF document(s) for analysis

## Implementation

### 1. Import Required Components

```python
from empire_chain.streamlit import PDFChatbot
from empire_chain.llms import OpenAILLM
from empire_chain.vector_stores import QdrantVectorStore
from empire_chain.embeddings import OpenAIEmbeddings
```

### 2. Initialize and Launch Chatbot

```python
# Create the chatbot with all necessary components
pdf_chatbot = PDFChatbot(
    title="PDF Assistant",
    llm=OpenAILLM("gpt-4"),
    vector_store=QdrantVectorStore(":memory:"),
    embeddings=OpenAIEmbeddings("text-embedding-3-small")
)

# Launch the interactive interface
pdf_chatbot.chat()
```

## How It Works

1. **Document Upload**: The chatbot provides a file upload interface for PDF documents
2. **Processing**: When a document is uploaded:
   - Text is extracted using `DocumentReader`
   - Text is split into chunks
   - Chunks are embedded and stored in the vector store
3. **Query Processing**: When a user asks a question:
   - The question is embedded
   - Similar chunks are retrieved from the vector store
   - Context and question are sent to the LLM
4. **Response**: The LLM generates a response based on the retrieved context

## Customization Options

### Using Different LLM Models

```python
# Using Anthropic
from empire_chain.llms import AnthropicLLM
chatbot = PDFChatbot(
    title="PDF Assistant",
    llm=AnthropicLLM("claude-3-sonnet"),
    vector_store=QdrantVectorStore(":memory:"),
    embeddings=OpenAIEmbeddings("text-embedding-3-small")
)

# Using Groq
from empire_chain.llms import GroqLLM
chatbot = PDFChatbot(
    title="PDF Assistant",
    llm=GroqLLM("mixtral-8x7b"),
    vector_store=QdrantVectorStore(":memory:"),
    embeddings=OpenAIEmbeddings("text-embedding-3-small")
)
```

### Using Different Vector Stores

```python
# Using ChromaDB
from empire_chain.vector_stores import ChromaVectorStore
chatbot = PDFChatbot(
    title="PDF Assistant",
    llm=OpenAILLM("gpt-4"),
    vector_store=ChromaVectorStore(),
    embeddings=OpenAIEmbeddings("text-embedding-3-small")
)
```

## Complete Example

Here's a complete example with all components configured:

```python
from empire_chain.streamlit import PDFChatbot
from empire_chain.llms import OpenAILLM
from empire_chain.vector_stores import QdrantVectorStore
from empire_chain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

def main():
    # Load environment variables
    load_dotenv()
    
    # Create and configure the chatbot
    chatbot = PDFChatbot(
        title="PDF Assistant",
        llm=OpenAILLM("gpt-4"),
        vector_store=QdrantVectorStore(":memory:"),
        embeddings=OpenAIEmbeddings("text-embedding-3-small")
    )
    
    # Launch the interface
    chatbot.chat()

if __name__ == "__main__":
    main()
```

## Best Practices

1. **Memory Management**: Use `:memory:` for temporary storage or configure persistent storage for production
2. **Model Selection**: Choose models based on your needs:
   - GPT-4 for highest accuracy
   - Claude for longer context
   - Mixtral for faster responses
3. **Error Handling**: The chatbot includes built-in error handling for:
   - File upload issues
   - Processing errors
   - API failures

## Next Steps

- Try the [Chat with Images](chat-with-images.md) tutorial
- Learn about [Data Visualization](visualize_data.md)
- Explore [Vector Store Options](../user-guide/vector-stores.md) 