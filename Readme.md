# ⚔️🔗 EmpireChain

⚡ An orchestration framework for all your AI needs ⚡

```
    ███████╗███╗   ███╗██████╗ ██╗██████╗ ███████╗
    ██╔════╝████╗ ████║██╔══██╗██║██╔══██╗██╔════╝
    █████╗  ██╔████╔██║██████╔╝██║██████╔╝█████╗  
    ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██║██╔══██╗██╔══╝  
    ███████╗██║ ╚═╝ ██║██║     ██║██║  ██║███████╗
    ╚══════╝╚═╝     ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝
     ██████╗██╗  ██╗ █████╗ ██╗███╗   ██╗
    ██╔════╝██║  ██║██╔══██╗██║████╗  ██║
    ██║     ███████║███████║██║██╔██╗ ██║
    ██║     ██╔══██║██╔══██║██║██║╚██╗██║
    ╚██████╗██║  ██║██║  ██║██║██║ ╚████║
     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝
    =============================================
         🔗 Chain Your AI Dreams Together 🔗
    =============================================
```

<p align="center">
  <a href="https://pypi.org/project/empire-chain/">
    <img src="https://img.shields.io/pypi/v/empire-chain" alt="PyPI version">
  </a>
  <a href="https://pypi.org/project/empire-chain/">
    <img src="https://img.shields.io/pypi/dm/empire-chain" alt="PyPI downloads">
  </a>
  <a href="https://github.com/manas95826/empire-chain/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License">
  </a>
  <a href="https://github.com/manas95826/empire-chain/stargazers">
    <img src="https://img.shields.io/github/stars/manas95826/empire-chain" alt="GitHub stars">
  </a>
</p>

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
from empire_chain.stt import GroqSTT
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
    
    text_query = "What is the main topic of this document?"
    audio_query = stt.transcribe("audio.mp3")
    query_embedding = embeddings.embed(audio_query)
    relevant_texts = vector_store.query(query_embedding, k=3)
    
    context = "\n".join(relevant_texts)
    prompt = f"Based on the following context, {text_query}\n\nContext: {context}"
    response = llm.generate(prompt)
    print(f"Query: {text_query}")
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
docling.generate("What is the main topic of this document?")
```

## Contributing

```bash
git clone https://github.com/manas95826/empire-chain.git
cd empire-chain
pip install -e .
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

