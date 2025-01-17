from empire_chain.streamlit import Chatbot
from empire_chain.llms import OpenAILLM

chatbot = Chatbot(title="Empire Chatbot", llm=OpenAILLM("gpt-4o-mini"))
chatbot.chat()