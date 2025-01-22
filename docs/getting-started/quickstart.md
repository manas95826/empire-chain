# Quick Start Guide

This guide will help you get started with Empire Chain by walking through some common use cases.

## Basic Setup

First, make sure you have Empire Chain installed and your environment configured:

```python
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
```

## 1. Simple LLM Integration

```python
from empire_chain.llms import OpenAILLM

# Initialize the LLM
llm = OpenAILLM("gpt-4")

# Generate text
response = llm.generate("What are the key principles of AI safety?")
print(response)
```

## 2. Document Processing

```python
from empire_chain.file_reader import DocumentReader

# Initialize the document reader
reader = DocumentReader()

# Read a PDF file
text = reader.read("document.pdf")
print(text)
```

## 3. Building a Simple Chatbot

```python
from empire_chain.streamlit import Chatbot
from empire_chain.llms import OpenAILLM

# Create a chatbot
chatbot = Chatbot(
    llm=OpenAILLM("gpt-4"),
    title="My First Chatbot"
)

# Launch the chatbot
chatbot.chat()
```

## 4. RAG Implementation

```python
from empire_chain.vector_stores import QdrantVectorStore
from empire_chain.embeddings import OpenAIEmbeddings
from empire_chain.llms import OpenAILLM
from empire_chain.file_reader import DocumentReader

# Initialize components
vector_store = QdrantVectorStore(":memory:")
embeddings = OpenAIEmbeddings("text-embedding-3-small")
llm = OpenAILLM("gpt-4")
reader = DocumentReader()

# Process document
text = reader.read("knowledge_base.pdf")
text_embedding = embeddings.embed(text)
vector_store.add(text, text_embedding)

# Query the system
query = "What are the main points in the document?"
query_embedding = embeddings.embed(query)
relevant_texts = vector_store.query(query_embedding, k=3)

# Generate response
context = "\n".join(relevant_texts)
response = llm.generate(f"Based on this context, {query}\n\nContext: {context}")
print(response)
```

## 5. Web Crawling

```python
from empire_chain.crawl4ai import Crawler

# Initialize crawler
crawler = Crawler()

# Crawl a website
data = crawler.crawl("https://example.com")
print(data)
```

## 6. Data Visualization

```python
from empire_chain.visualizer import DataAnalyzer, ChartFactory

# Analyze data
analyzer = DataAnalyzer()
data = """
The company saw revenue growth of $1M in Q1, $1.5M in Q2, 
$2M in Q3, and $2.5M in Q4 of 2023.
"""
analyzed_data = analyzer.analyze(data)

# Create and display chart
chart = ChartFactory.create_chart('Line Graph', analyzed_data)
chart.show()
```

## 7. Using PhiData Agents

```python
from empire_chain.phidata_agents import PhiWebAgent, PhiFinanceAgent

# Create agents
web_agent = PhiWebAgent()
finance_agent = PhiFinanceAgent()

# Use agents
news = web_agent.generate("What are the latest developments in AI?")
stock_analysis = finance_agent.generate("Analyze recent NVIDIA stock performance")
```

## Next Steps

- Explore more examples in our [Cookbooks](../tutorials/empire-rag.md)
- Learn about [Core Concepts](../user-guide/core-concepts.md)
- Check out the [API Reference](../api-reference/docling.md)

For more detailed examples, visit our [GitHub repository](https://github.com/manas95826/empire-chain/tree/main/cookbooks). 