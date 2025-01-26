# Empire Agent

The Empire Agent is a powerful tool for building AI-powered agents that can perform various tasks using registered functions.

## Basic Usage

```python
from empire_chain.agent.agent import Agent
from datetime import datetime

# Create agent
agent = Agent()

# Example function to register
def get_weather(location: str) -> str:
    return f"The weather in {location} is sunny!"

# Register function
agent.register_function(get_weather)

# Process query
result = agent.process_query("What's the weather like in Tokyo?")
print(result['result'])
```

## Available Functions

The Empire Agent supports registering any Python function that follows these guidelines:
- Has type hints for parameters
- Returns a string
- Has clear, descriptive parameter names

## Example Functions

Here are some example functions you can register with the agent:

```python
def calculate_distance(from_city: str, to_city: str) -> str:
    return f"The distance from {from_city} to {to_city} is 500km"

def get_time(timezone: str) -> str:
    return f"Current time in {timezone}: {datetime.now()}"

def translate_text(text: str, target_language: str) -> str:
    return f"Translated '{text}' to {target_language}: [translation would go here]"

def search_web(query: str, num_results: int) -> str:
    return f"Top {num_results} results for '{query}': [search results would go here]"
```

For more examples and advanced usage, check out the cookbooks in the repository. 