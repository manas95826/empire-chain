An orchestration framework for all your AI needs.

## Installation

```bash
pip install empire_chain
```

## Google Drive Authentication

```bash
from empire_chain.file_reader import DocumentReader

reader = DocumentReader()

text = reader.read("your_drive_link/your_file_name")

print(text)
```

## RAG Example

```python
from empire_chain.vector_stores import QdrantVectorStore
from empire_chain.embeddings import OpenAIEmbeddings
from empire_chain.llms import OpenAILLM
from empire_chain.file_reader import DocumentReader
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    
    vector_store = QdrantVectorStore(":memory:")
    embeddings = OpenAIEmbeddings("text-embedding-3-small")
    llm = OpenAILLM("gpt-4o-mini")
    reader = DocumentReader()
    
    file_path = "input.pdf"
    text = reader.read(file_path)
    
    text_embedding = embeddings.embed(text)
    vector_store.add(text, text_embedding)
    
    query = "What is the main topic of this document?"
    query_embedding = embeddings.embed(query)
    relevant_texts = vector_store.query(query_embedding, k=3)
    
    context = "\n".join(relevant_texts)
    prompt = f"Based on the following context, {query}\n\nContext: {context}"
    response = llm.generate(prompt)
    print(f"Query: {query}")
    print(f"Response: {response}")

if __name__ == "__main__":
    main()
```

# PhiData Agents

```python
from empire_chain.phidata_agents import PhiWebAgent, PhiFinanceAgent
from dotenv import load_dotenv

load_dotenv()

web_agent = PhiWebAgent()
web_agent.generate("What is the recent news about Tesla with sources?")

finance_agent = PhiFinanceAgent()
finance_agent.generate("What is the price of Tesla?")
```

## Simple Chatbot

```python
from empire_chain.streamlit import Chatbot
from empire_chain.llms import OpenAILLM

chatbot = Chatbot(llm=OpenAILLM("gpt-4o-mini"), title="Empire Chain Chatbot")
chatbot.chat()
```

## Vision Chatbot

```python
from empire_chain.streamlit import VisionChatbot

chatbot = VisionChatbot(title="Empire Chain Chatbot")
chatbot.chat()
```

## PDF Chatbot

```python
from empire_chain.streamlit import PDFChatbot
from empire_chain.llms import OpenAILLM
from empire_chain.vector_stores import QdrantVectorStore
from empire_chain.embeddings import OpenAIEmbeddings

pdf_chatbot = PDFChatbot(title="PDF Chatbot", llm=OpenAILLM("gpt-4o-mini"), vector_store=QdrantVectorStore(":memory:"), embeddings=OpenAIEmbeddings("text-embedding-3-small"))
pdf_chatbot.chat()
```

## Visualizer

```python
from empire_chain.visualizer import DataAnalyzer, ChartFactory

data = """
Empire chain has secured a $100M Series A funding round from Sequoia Capital in 2024 and a $10M Series B funding round from Tiger Global in 2025.
...
"""

analyzer = DataAnalyzer()
analyzed_data = analyzer.analyze(data)

chart = ChartFactory.create_chart('Bar Graph', analyzed_data)
chart.show()
```

## Docling

```python
from empire_chain.docling import Docling

docling = Docling()

converted_doc = docling.convert("https://arxiv.org/pdf/2408.09869")
docling.save_markdown(converted_doc, "arxiv_2408.09869.md")
```

## Podcast

```python
from empire_chain.podcast import GeneratePodcast

podcast=GeneratePodcast()
podcast.generate(topic="About boom of meal plan and recipe generation apps")
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
