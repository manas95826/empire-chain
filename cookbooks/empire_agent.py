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