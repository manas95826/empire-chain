# LLM Integration

## Overview

Empire Chain provides seamless integration with various Large Language Models (LLMs). This guide covers how to use different LLMs, configure them, and build applications with them.

## Supported Models

- OpenAI GPT Models
- Anthropic Claude
- Local Models (via HuggingFace)
- Custom Model Integration

## Basic Usage

### Setting Up

```python
from empire_chain.docling import LLMHandler

# Initialize with OpenAI
llm = LLMHandler(provider="openai")

# Initialize with Anthropic
llm = LLMHandler(provider="anthropic")

# Initialize with local model
llm = LLMHandler(
    provider="local",
    model_path="path/to/model"
)
```

### Simple Queries

```python
# Basic completion
response = llm.complete("Tell me about AI")

# Chat completion
messages = [
    {"role": "user", "content": "What is machine learning?"}
]
response = llm.chat(messages)
```

## Advanced Features

### Model Configuration

```python
config = {
    "model": "gpt-4",
    "temperature": 0.7,
    "max_tokens": 150,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0
}

llm = LLMHandler(provider="openai", config=config)
```

### Streaming Responses

```python
for chunk in llm.stream("Tell me a story"):
    print(chunk, end="", flush=True)
```

### Function Calling

```python
functions = [{
    "name": "get_weather",
    "description": "Get weather information",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {"type": "string"},
            "unit": {"type": "string"}
        }
    }
}]

response = llm.chat(
    messages=[{"role": "user", "content": "What's the weather in London?"}],
    functions=functions
)
```

## Integration Patterns

### RAG Implementation

```python
from empire_chain.docling import RAGSystem

# Initialize RAG with specific LLM
rag = RAGSystem(llm_handler=llm)

# Add documents
rag.add_documents(["doc1.pdf", "doc2.pdf"])

# Query with context
response = rag.query("What do the documents say about AI?")
```

### Chain of Thought

```python
prompt = """
Question: {question}
Let's approach this step by step:
1) First, let's understand what we're asked
2) Then, break down the problem
3) Finally, provide the solution
"""

response = llm.complete(
    prompt.format(question="How does photosynthesis work?"),
    temperature=0.3
)
```

### Agent Implementation

```python
from empire_chain.docling import Agent

# Create an agent with tools
agent = Agent(
    llm_handler=llm,
    tools=[
        "calculator",
        "web_search",
        "code_executor"
    ]
)

# Run agent
result = agent.run("Calculate the compound interest on $1000")
```

## Best Practices

### Error Handling

```python
from empire_chain.exceptions import LLMError

try:
    response = llm.complete("Generate text")
except LLMError as e:
    print(f"LLM Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

### Rate Limiting

```python
llm = LLMHandler(
    provider="openai",
    config={
        "rate_limit": {
            "requests_per_minute": 60,
            "tokens_per_minute": 40000
        }
    }
)
```

### Caching

```python
llm = LLMHandler(
    provider="openai",
    config={
        "cache": {
            "enabled": True,
            "ttl": 3600,  # 1 hour
            "max_size": 1000
        }
    }
)
```

## Model Comparison

| Provider | Strengths | Use Cases |
|----------|-----------|-----------|
| OpenAI   | State-of-the-art performance | General purpose, code generation |
| Anthropic| Long context, reasoning | Document analysis, complex tasks |
| Local    | Privacy, no latency | Edge deployment, offline use |

## Security Considerations

1. API Key Management
```python
# Use environment variables
import os
llm = LLMHandler(
    provider="openai",
    api_key=os.getenv("OPENAI_API_KEY")
)
```

2. Content Filtering
```python
llm = LLMHandler(
    provider="openai",
    config={
        "content_filter": {
            "enabled": True,
            "level": "strict"
        }
    }
) 