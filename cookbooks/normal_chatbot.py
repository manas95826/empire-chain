from empire_chain.streamlit import Chatbot
from empire_chain.llms import OpenAILLM

chatbot = Chatbot(llm=OpenAILLM("gpt-4o-mini"), title="Empire Chain Chatbot")
chatbot.chat()