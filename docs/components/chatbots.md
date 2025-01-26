# Chatbots

Empire Chain provides several types of chatbots that can be easily integrated into your applications.

## Simple Chatbot

The basic chatbot implementation using Streamlit:

```python
from empire_chain.streamlit import Chatbot
from empire_chain.llms.llms import OpenAILLM

# Create and run chatbot
chatbot = Chatbot(
    title="Empire Chatbot",
    llm=OpenAILLM("gpt-4o-mini")
)
chatbot.chat()
```

## Vision Chatbot

Chat with images using multimodal models:

```python
from empire_chain.streamlit import VisionChatbot

# Create and run vision chatbot
chatbot = VisionChatbot(title="Empire Vision Chatbot")
chatbot.chat()
```

## PDF Chatbot

Chat with PDF documents using RAG:

```python
from empire_chain.streamlit import PDFChatbot
from empire_chain.llms.llms import OpenAILLM
from empire_chain.vector_stores import QdrantVectorStore
from empire_chain.embeddings import OpenAIEmbeddings

# Create and run PDF chatbot
pdf_chatbot = PDFChatbot(
    title="PDF Chatbot",
    llm=OpenAILLM("gpt-4o-mini"),
    vector_store=QdrantVectorStore(":memory:"),
    embeddings=OpenAIEmbeddings("text-embedding-3-small")
)
pdf_chatbot.chat()
```

## Features

- **Simple Chatbot**: Basic text-based conversation
- **Vision Chatbot**: Image understanding and discussion
- **PDF Chatbot**: Document-based conversation using RAG
- **Customizable UI**: Built with Streamlit for easy deployment
- **Multiple LLM Support**: OpenAI, Anthropic, Groq

## Running the Chatbots

1. Install dependencies:
```bash
pip install empire-chain streamlit
```

2. Run the chatbot:
```bash
streamlit run app.py
```

For more examples and advanced usage, check out the chatbot cookbooks in the repository. 