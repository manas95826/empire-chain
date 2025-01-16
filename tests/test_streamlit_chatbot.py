from empire_chain.streamlit import Chatbot
from empire_chain.llms import OpenAILLM
import unittest

class TestStreamlitChatbot(unittest.TestCase):
    def test_chatbot(self):
        chatbot = Chatbot(llm=OpenAILLM("gpt-4o-mini"), title="Test Chatbot")
        chatbot.chat()

if __name__ == "__main__":
    unittest.main()