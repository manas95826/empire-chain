from datetime import datetime
from empire_chain.agent import Agent
from dotenv import load_dotenv

load_dotenv()

def get_weather(location: str) -> str:
    """Simulated weather function"""
    return f"The weather in {location} is sunny!"

def calculate_distance(from_city: str, to_city: str) -> str:
    """Simulated distance calculator"""
    return f"The distance from {from_city} to {to_city} is 500km"

def get_time(timezone: str = "UTC") -> str:
    """Get current time in given timezone"""
    return f"Current time in {timezone}: {datetime.now()}"

def translate_text(text: str, target_language: str) -> str:
    """Simulated translation function"""
    return f"Translated '{text}' to {target_language}: [translation would go here]"

def search_web(query: str, num_results: int = 5) -> str:
    """Simulated web search"""
    return f"Top {num_results} results for '{query}': [search results would go here]"

def main():
    # Create agent
    agent = Agent()
    
    # Register multiple functions
    agent.register_function(
        name="get_weather",
        func=get_weather,
        description="Get the current weather for a specific location",
        parameters=["location"]
    )
    
    agent.register_function(
        name="calculate_distance",
        func=calculate_distance,
        description="Calculate the distance between two cities",
        parameters=["from_city", "to_city"]
    )
    
    agent.register_function(
        name="get_time",
        func=get_time,
        description="Get the current time in a specific timezone",
        parameters=["timezone"]
    )
    
    agent.register_function(
        name="translate_text",
        func=translate_text,
        description="Translate text to a target language",
        parameters=["text", "target_language"]
    )
    
    agent.register_function(
        name="search_web",
        func=search_web,
        description="Search the web for information",
        parameters=["query", "num_results"]
    )
    
    # Example queries
    queries = [
        "What's the weather like in Tokyo?",
        "How far is London from Paris?",
        "What time is it in EST?",
        "Translate 'Hello World' to Spanish",
        "Search for latest news about AI"
    ]
    
    # Process multiple queries
    for query in queries:
        try:
            result = agent.process_query(query)
            print(f"\nQuery: {query}")
            print(f"Result: {result['result']}")
        except Exception as e:
            print(f"Error processing query '{query}': {str(e)}")

if __name__ == "__main__":
    main()