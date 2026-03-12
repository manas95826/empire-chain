from empire_chain.agent.agent import Agent
from empire_chain.memory.conversation_memory import ConversationBufferMemory

# Create memory instance
memory = ConversationBufferMemory()

# Create agent with memory
agent = Agent(memory=memory)

# Register a dummy function
def get_weather(location: str) -> str:
    """Get current weather in a location"""
    return f"The weather in {location} is sunny."

agent.register_function(get_weather)

# Query 1: Explicit location
out1 = agent.process_query("What's the weather in Mumbai?")
print("First:", out1)

# Query 2: Implicit context (tests memory)
out2 = agent.process_query("What about in Delhi?")
print("Second:", out2)
