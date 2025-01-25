"""
This is a simple chatbot that uses the Empire Chain library to create a chatbot.
Please run the following command to install the necessary dependencies and store keys in .env:
!pip install empire-chain streamlit
!streamlit run app.py
"""
from empire_chain.streamlit import Chatbot
from empire_chain.llms.llms import OpenAILLM

chatbot = Chatbot(title="Empire Chatbot", llm=OpenAILLM("gpt-4o-mini"))
chatbot.chat()