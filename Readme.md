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

## Features

- 🤖 Multiple LLM Support (OpenAI, Anthropic, Groq)
- 📚 Vector Store Integration (Qdrant, ChromaDB)
- 🔍 Advanced Document Processing
- 🎙️ Speech-to-Text Capabilities
- 🌐 Web Crawling with crawl4ai
- 📊 Data Visualization
- 🎯 RAG Applications
- 🤝 PhiData Agent Integration
- 💬 Interactive Chatbots
- 🤖 Agentic Framework

## Installation

```bash
pip install empire-chain
```

## Core Components

### Agent

```python
from empire_chain.agent import Agent
from dotenv import load_dotenv

load_dotenv()

def get_weather(location: str) -> str:
    """Simulated weather function"""
    return f"The weather in {location} is sunny!"

def calculate_distance(from_city: str, to_city: str) -> str:
    """Simulated distance calculator"""
    return f"The distance from {from_city} to {to_city} is 500km"

agent = Agent()
agent.register_function(get_weather)
agent.register_function(calculate_distance)
result = agent.process_query("What's the weather like in New York?")
print(result)
```

### Document Processing

```python
from empire_chain.file_reader import DocumentReader

reader = DocumentReader()
text = reader.read("your_file_path")  # Supports PDF, DOCX, and more
```

### Speech-to-Text

```python
from empire_chain.stt import GroqSTT

stt = GroqSTT()
text = stt.transcribe("audio_file.mp3")
```

### LLM Integration

```python
from empire_chain.llms import OpenAILLM, AnthropicLLM, GroqLLM

openai_llm = OpenAILLM("gpt-4")
anthropic_llm = AnthropicLLM("claude-3-sonnet")
groq_llm = GroqLLM("mixtral-8x7b")
```

### Vector Stores

```python
from empire_chain.vector_stores import QdrantVectorStore, ChromaVectorStore
from empire_chain.embeddings import OpenAIEmbeddings

vector_store = QdrantVectorStore(":memory:")
embeddings = OpenAIEmbeddings("text-embedding-3-small")
```

### Web Crawling

```python
from empire_chain.crawl4ai import Crawler

crawler = Crawler()
data = crawler.crawl("https://example.com")
```

### Data Visualization

```python
from empire_chain.visualizer import DataAnalyzer, ChartFactory

analyzer = DataAnalyzer()
analyzed_data = analyzer.analyze(your_data)
chart = ChartFactory.create_chart('Bar Graph', analyzed_data)
chart.show()
```

### Interactive Chatbots

```python
from empire_chain.streamlit import Chatbot, VisionChatbot, PDFChatbot

# Simple Chatbot
chatbot = Chatbot(llm=OpenAILLM("gpt-4"), title="Empire Chain Chatbot")
chatbot.chat()

# Vision Chatbot
vision_bot = VisionChatbot(title="Vision Assistant")
vision_bot.chat()

# PDF Chatbot
pdf_bot = PDFChatbot(
    title="PDF Assistant",
    llm=OpenAILLM("gpt-4"),
    vector_store=QdrantVectorStore(":memory:"),
    embeddings=OpenAIEmbeddings("text-embedding-3-small")
)
pdf_bot.chat()
```

### PhiData Agents

```python
from empire_chain.phidata_agents import PhiWebAgent, PhiFinanceAgent

web_agent = PhiWebAgent()
finance_agent = PhiFinanceAgent()

web_results = web_agent.generate("What are the latest AI developments?")
finance_results = finance_agent.generate("Analyze TSLA stock performance")
```

## Example Cookbooks

Check out our cookbooks directory for complete examples:
- RAG Applications (`cookbooks/empire_rag.py`)
- Web Crawling (`cookbooks/crawler.py`)
- Document Processing (`cookbooks/generalized_read_file.py`)
- Topic to Podcast (`cookbooks/topic-to-podcast.py`)
- Data Visualization (`cookbooks/visualize_data.py`)
- Chatbot Examples (`cookbooks/simple_chatbot.py`, `cookbooks/chat_with_image.py`, `cookbooks/chat_with_pdf.py`)
- PhiData Agent Usage (`cookbooks/phi_agents.py`)

## Contributing

```bash
git clone https://github.com/manas95826/empire-chain.git
cd empire-chain
pip install -e .
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.