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
  <a href="https://pepy.tech/project/empire-chain">
    <img src="https://static.pepy.tech/badge/empire-chain" alt="PyPI downloads">
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

# Empire Chain Components

## Empire Agent

```python
"""
This is a simple example of how to use the Empire Agent.
Please run the following command to install the necessary dependencies and store keys in .env:
!pip install empire-chain
"""
from datetime import datetime
from empire_chain.agent.agent import Agent
from dotenv import load_dotenv

load_dotenv()

def get_weather(location: str) -> str:
    return f"The weather in {location} is sunny!"

def calculate_distance(from_city: str, to_city: str) -> str:
    return f"The distance from {from_city} to {to_city} is 500km"

def get_time(timezone: str) -> str:
    return f"Current time in {timezone}: {datetime.now()}"

def translate_text(text: str, target_language: str) -> str:
    return f"Translated '{text}' to {target_language}: [translation would go here]"

def search_web(query: str, num_results: int) -> str:
    return f"Top {num_results} results for '{query}': [search results would go here]"

def main():
    # Create agent
    agent = Agent()
    
    # Register functions
    functions = [
        get_weather,
        calculate_distance,
        get_time,
        translate_text,
        search_web
    ]
    
    for func in functions:
        agent.register_function(func)
    
    # Example queries
    queries = [
        "What's the weather like in Tokyo?",
        "How far is London from Paris?",
        "What time is it in EST timezone?",
        "Translate 'Hello World' to Spanish",
        "Search for latest news about AI and show 3 results"
    ]
    
    # Process queries
    for query in queries:
        try:
            result = agent.process_query(query)
            print(f"\nQuery: {query}")
            print(f"Result: {result['result']}")
        except Exception as e:
            print(f"Error processing query '{query}': {str(e)}")

if __name__ == "__main__":
    main()
```

## RAG

```python
from empire_chain.vector_stores import QdrantVectorStore
from empire_chain.embeddings import OpenAIEmbeddings
from empire_chain.llms.llms import GroqLLM
from empire_chain.tools.file_reader import DocumentReader
import os
from dotenv import load_dotenv
from empire_chain.stt.stt import GroqSTT

def main(if_audio_input: bool = False):
    load_dotenv()
    
    vector_store = QdrantVectorStore(":memory:")
    embeddings = OpenAIEmbeddings("text-embedding-3-small")
    llm = GroqLLM("llama3-8b-8192")
    reader = DocumentReader()
    
    file_path = "input.pdf"
    text = reader.read(file_path)
    
    text_embedding = embeddings.embed(text)
    vector_store.add(text, text_embedding)
    
    text_query = "What is the main topic of this document?"
    if if_audio_input:
        stt = GroqSTT()
        audio_query = stt.transcribe("audio.mp3")
        query_embedding = embeddings.embed(audio_query)
    else:
        query_embedding = embeddings.embed(text_query)
    relevant_texts = vector_store.query(query_embedding, k=3)
    
    context = "\n".join(relevant_texts)
    prompt = f"Based on the following context, {text_query}\n\nContext: {context}"
    response = llm.generate(prompt)
    print(f"Query: {text_query}")
    print(f"Response: {response}")

if __name__ == "__main__":
    main(if_audio_input=False)
```

## Chatbots

### Simple Chatbot

```python
"""
This is a simple chatbot that uses the Empire Chain library to create a chatbot.
Please run the following command to install the necessary dependencies and store keys in .env:
!pip install empire-chain streamlit
!streamlit run app.py
"""
from empire_chain.streamlit import Chatbot
from empire_chain.llms.llms import OpenAILLM

chatbot = Chatbot(title="Empire Chatbot", llm=OpenAILLM("gpt-4o-mini"))
chatbot.chat()
```

### Chat with Image

```python
"""
This is a simple chatbot that uses the Empire Chain library to create a chatbot.
Please run the following command to install the necessary dependencies and groq key in .env (https://console.groq.com/keys):
!pip install empire-chain streamlit
!streamlit run app.py
"""
from empire_chain.streamlit import VisionChatbot

chatbot = VisionChatbot(title="Empire Chatbot")
chatbot.chat()
```

### Chat with PDF

```python
"""
This is a simple chatbot that uses the Empire Chain library to create a pdf chatbot.
Please run the following command to install the necessary dependencies and store keys in .env:
!pip install empire-chain streamlit
!streamlit run app.py
"""
from empire_chain.streamlit import PDFChatbot
from empire_chain.llms.llms import OpenAILLM
from empire_chain.vector_stores import QdrantVectorStore
from empire_chain.embeddings import OpenAIEmbeddings

pdf_chatbot = PDFChatbot(title="PDF Chatbot", llm=OpenAILLM("gpt-4o-mini"), vector_store=QdrantVectorStore(":memory:"), embeddings=OpenAIEmbeddings("text-embedding-3-small"))
pdf_chatbot.chat()
```

## PhiData Agents

### Web Agent

```python
"""
This is a simple example of how to use the WebAgent class to generate web data.
Please run the following command to install the necessary dependencies and store keys in .env:
!pip install empire-chain phidata duckduckgo-search
"""
from empire_chain.phidata.web_agent import WebAgent

web_agent = WebAgent()

web_agent.generate("What is the price of Tesla?")
```

### Finance Agent

```python
"""
This is a simple example of how to use the PhiFinanceAgent class to generate financial data.
Please run the following command to install the necessary dependencies and store keys in .env:
!pip install empire-chain phidata yfinance
"""
from empire_chain.phidata.finance_agent import PhiFinanceAgent

finance_agent = PhiFinanceAgent()

finance_agent.generate("Analyze TSLA stock performance")
```

## Tools

### File Reader

```python
"""
This is a simple file reader that uses the Empire Chain library to read a file.
It supports 
1. PDF files (.pdf)
2. Microsoft Word documents (.docx)
3. Text files (.txt)
4. JSON files (.json)
5. CSV files (.csv)
6. Google Drive files (.gdrive)
"""
from empire_chain.tools.file_reader import DocumentReader
reader = DocumentReader()

text = reader.read("https://drive.google.com/file/d/1t0Itw6oGO2iVusp=sharing")
print(text)

text = reader.read("input.pdf")
print(text)
```

### Website Crawler

```python
"""
This is a simple crawler that uses the Empire Chain library to crawl a website and save the content as markdown.
Please run the following command to install the necessary dependencies and store keys in .env:
!pip install empire-chain crawl4ai
"""
from empire_chain.tools.crawl4ai import Crawler

crawler = Crawler()
result = crawler.crawl(url="https://www.geekroom.in", format="markdown")
print(result)
```

### Speech to Text

```python
from empire_chain.stt.stt import GroqSTT
from empire_chain.stt.stt import HuggingFaceSTT
from dotenv import load_dotenv
import os
load_dotenv()

stt = GroqSTT()
text = stt.transcribe("audio.mp3")
print(text)

stt = HuggingFaceSTT()
text = stt.transcribe("audio.mp3")
print(text)
```

## Cool Stuff

### Visualize Data

```python
"""
This is a simple example of how to use the DataAnalyzer and ChartFactory classes to visualize data.
Please run the following command to install the necessary dependencies and store keys in .env:
!pip install empire-chain matplotlib

_chart_types = {
        'Line Chart': LineChart,
        'Pie Chart': PieChart,
        'Bar Graph': BarGraph,
        'Scatter Plot': ScatterChart,
        'Histogram': Histogram,
        'Box Plot': BoxPlot
    }
Please adhere to the naming convention for the chart type.
"""
from empire_chain.cool_stuff.visualizer import DataAnalyzer, ChartFactory

data = """
Empire chain got a fund raise of $100M from a new investor in 2024 and $50M from a new investor in 2023.
"""
    
analyzer = DataAnalyzer()
analyzed_data = analyzer.analyze(data)
        
chart = ChartFactory.create_chart('Bar Chart', analyzed_data)
chart.show()
```

### Text to Podcast

```python
"""
This is a simple example of how to use the GeneratePodcast class to generate a podcast.
Please run the following command to install the necessary dependencies and store keys in .env:
!pip install empire-chain kokoro_onnx (It might take a while to download the model files)
"""
from empire_chain.cool_stuff.podcast import GeneratePodcast

podcast=GeneratePodcast()
podcast.generate(topic="About boom of meal plan and recipe generation apps")
```

## Contributing

```bash
git clone https://github.com/manas95826/empire-chain.git
cd empire-chain
pip install -e .
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.