from empire_chain.streamlit import Chatbot
from empire_chain.llms import OpenAILLM
chatbot = Chatbot(llm=OpenAILLM(model="gpt-4o-mini"), title="Chatbot", chat_history=True, custom_instructions="You are a helpful assistant that can answer questions about the PDF.", verbose=True)

chatbot.chat()