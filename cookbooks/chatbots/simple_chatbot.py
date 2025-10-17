"""
This is a simple chatbot that uses the Empire Chain library to create a chatbot.
Please run the following command to install the necessary dependencies and store keys in .env:
!pip install empire-chain streamlit
!streamlit run app.py
"""
from empire_chain.streamlit import Chatbot
from empire_chain.llms.llms import GroqLLM

chatbot = Chatbot(title="Empire Chatbot", llm=GroqLLM("llama3-8b-8192"), chat_history=False, verbose=False)
chatbot.chat()
