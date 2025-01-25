"""
This is a simple chatbot that uses the Empire Chain library to create a chatbot.
Please run the following command to install the necessary dependencies and groq key in .env (https://console.groq.com/keys):
!pip install empire-chain streamlit
!streamlit run app.py
"""
from empire_chain.streamlit import VisionChatbot

chatbot = VisionChatbot(title="Empire Chatbot")
chatbot.chat()