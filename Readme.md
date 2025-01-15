An orchestration framework for all your AI needs.

## Installation

```bash
pip install empire_chain
```

## Usage

```python
from empire_chain import OpenAILLM, AnthropicLLM

llm = OpenAILLM("gpt-4o-mini")
response = llm.generate("What is the capital of France?")
print(response)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.