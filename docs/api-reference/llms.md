# LLM Module API Reference

The `empire_chain.llms` module provides interfaces to various Language Model providers.

## OpenAILLM

```python
from empire_chain.llms import OpenAILLM
```

Class for interacting with OpenAI's language models.

### Constructor

```python
OpenAILLM(model_name: str = "gpt-4")
```

**Parameters:**
- `model_name` (str): The OpenAI model to use. Options include:
  - `"gpt-4"`
  - `"gpt-3.5-turbo"`
  - `"gpt-4-turbo"`

### Methods

#### generate()

```python
def generate(self, prompt: str) -> str
```

Generate text based on a prompt.

**Parameters:**
- `prompt` (str): The input prompt for text generation

**Returns:**
- str: The generated text response

**Example:**
```python
llm = OpenAILLM("gpt-4")
response = llm.generate("What is artificial intelligence?")
```

## AnthropicLLM

```python
from empire_chain.llms import AnthropicLLM
```

Class for interacting with Anthropic's Claude models.

### Constructor

```python
AnthropicLLM(model_name: str = "claude-3-sonnet")
```

**Parameters:**
- `model_name` (str): The Anthropic model to use. Options include:
  - `"claude-3-sonnet"`
  - `"claude-3-opus"`
  - `"claude-3-haiku"`

### Methods

#### generate()

```python
def generate(self, prompt: str) -> str
```

Generate text using Claude.

**Parameters:**
- `prompt` (str): The input prompt for text generation

**Returns:**
- str: The generated text response

**Example:**
```python
llm = AnthropicLLM("claude-3-sonnet")
response = llm.generate("Explain quantum computing")
```

## GroqLLM

```python
from empire_chain.llms import GroqLLM
```

Class for interacting with Groq's language models.

### Constructor

```python
GroqLLM(model_name: str = "mixtral-8x7b")
```

**Parameters:**
- `model_name` (str): The Groq model to use. Options include:
  - `"mixtral-8x7b"`
  - `"llama2-70b"`

### Methods

#### generate()

```python
def generate(self, prompt: str) -> str
```

Generate text using Groq.

**Parameters:**
- `prompt` (str): The input prompt for text generation

**Returns:**
- str: The generated text response

**Example:**
```python
llm = GroqLLM("mixtral-8x7b")
response = llm.generate("Write a poem about AI")
```

## Common Features

All LLM classes share these common features:

### Error Handling

```python
try:
    llm = OpenAILLM()
    response = llm.generate("prompt")
except Exception as e:
    print(f"Error: {e}")
```

### Environment Variables

Required environment variables:
- OpenAI: `OPENAI_API_KEY`
- Anthropic: `ANTHROPIC_API_KEY`
- Groq: `GROQ_API_KEY`

### Best Practices

1. **Model Selection**
   ```python
   # For complex reasoning
   llm = OpenAILLM("gpt-4")
   
   # For longer context
   llm = AnthropicLLM("claude-3-opus")
   
   # For faster responses
   llm = GroqLLM("mixtral-8x7b")
   ```

2. **Error Handling**
   ```python
   try:
       response = llm.generate(prompt)
   except Exception as e:
       # Handle specific error types
       pass
   ```

3. **Environment Setup**
   ```python
   from dotenv import load_dotenv
   load_dotenv()  # Load API keys from .env
   ``` 