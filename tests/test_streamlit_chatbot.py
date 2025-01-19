from empire_chain.streamlit import Chatbot, VisionChatbot, PDFChatbot
from empire_chain.llms import OpenAILLM
from empire_chain.vector_stores import QdrantVectorStore
from empire_chain.embeddings import OpenAIEmbeddings
import unittest
import streamlit as st
from unittest.mock import MagicMock, patch
from PIL import Image
import io
import numpy as np

class TestStreamlitChatbot(unittest.TestCase):
    def setUp(self):
        self.llm = OpenAILLM("gpt-4o-mini")
        
    def test_chatbot_initialization(self):
        chatbot = Chatbot(llm=self.llm, title="Test Chatbot")
        self.assertEqual(chatbot.title, "Test Chatbot")
        self.assertEqual(chatbot.llm, self.llm)
        self.assertTrue(chatbot.chat_history)
        
    def test_chatbot_initialization_no_history(self):
        chatbot = Chatbot(llm=self.llm, title="Test Chatbot", chat_history=False)
        self.assertFalse(chatbot.chat_history)
        
    @patch('streamlit.chat_input')
    @patch('streamlit.chat_message')
    def test_chatbot_chat_flow(self, mock_chat_message, mock_chat_input):
        chatbot = Chatbot(llm=self.llm, title="Test Chatbot")
        mock_chat_input.return_value = "Hello"
        mock_response = MagicMock()
        mock_response.markdown = MagicMock()
        mock_chat_message.return_value.__enter__.return_value = mock_response
        
        with patch.object(self.llm, 'generate', return_value="Hi there!"):
            chatbot.chat()
            self.llm.generate.assert_called_once()

class TestVisionChatbot(unittest.TestCase):
    def setUp(self):
        self.test_image = Image.new('RGB', (100, 100), color='red')
        
    def test_vision_chatbot_initialization(self):
        chatbot = VisionChatbot(title="Test Vision Chatbot")
        self.assertEqual(chatbot.title, "Test Vision Chatbot")
        self.assertTrue(chatbot.chat_history)
        
    def test_vision_chatbot_initialization_no_history(self):
        chatbot = VisionChatbot(title="Test Vision Chatbot", chat_history=False)
        self.assertFalse(chatbot.chat_history)
        
    def test_convert_image_to_base64(self):
        chatbot = VisionChatbot(title="Test Vision Chatbot")
        base64_image = chatbot.convert_image_to_base64(self.test_image)
        self.assertTrue(base64_image.startswith("data:image/png;base64,"))
        
    @patch('streamlit.file_uploader')
    @patch('streamlit.chat_input')
    @patch('streamlit.chat_message')
    def test_vision_chatbot_chat_flow(self, mock_chat_message, mock_chat_input, mock_file_uploader):
        chatbot = VisionChatbot(title="Test Vision Chatbot")
        
        mock_file = MagicMock()
        mock_file.read = MagicMock(return_value=self.test_image.tobytes())
        mock_file_uploader.return_value = mock_file
        
        mock_chat_input.return_value = "What's in this image?"
        mock_response = MagicMock()
        mock_response.markdown = MagicMock()
        mock_chat_message.return_value.__enter__.return_value = mock_response
        
        with patch.object(Image, 'open', return_value=self.test_image), \
             patch.object(chatbot, 'process_image_query', return_value="I see a red image"):
            chatbot.chat()
            chatbot.process_image_query.assert_called_once()

class TestPDFChatbot(unittest.TestCase):
    def setUp(self):
        self.llm = OpenAILLM("gpt-4-mini")
        self.vector_store = QdrantVectorStore()
        self.embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
        # Create a mock embedding vector of correct size (1536)
        self.mock_embedding = np.random.rand(1536).tolist()
        
    def test_pdf_chatbot_initialization(self):
        chatbot = PDFChatbot(
            title="Test PDF Chatbot",
            llm=self.llm,
            vector_store=self.vector_store,
            embeddings=self.embeddings
        )
        self.assertEqual(chatbot.title, "Test PDF Chatbot")
        self.assertEqual(chatbot.llm, self.llm)
        self.assertEqual(chatbot.vector_store, self.vector_store)
        self.assertEqual(chatbot.embeddings, self.embeddings)
        self.assertTrue(chatbot.chat_history)
        
    def test_pdf_chatbot_initialization_no_history(self):
        chatbot = PDFChatbot(
            title="Test PDF Chatbot",
            llm=self.llm,
            vector_store=self.vector_store,
            embeddings=self.embeddings,
            chat_history=False
        )
        self.assertFalse(chatbot.chat_history)
        
    @patch('streamlit.file_uploader')
    @patch('streamlit.chat_input')
    @patch('streamlit.chat_message')
    def test_pdf_chatbot_chat_flow(self, mock_chat_message, mock_chat_input, mock_file_uploader):
        chatbot = PDFChatbot(
            title="Test PDF Chatbot",
            llm=self.llm,
            vector_store=self.vector_store,
            embeddings=self.embeddings
        )
        
        mock_file = MagicMock()
        mock_file.read = MagicMock(return_value=b"fake pdf content")
        mock_file_uploader.return_value = mock_file
        
        mock_chat_input.return_value = "What's in this document?"
        mock_response = MagicMock()
        mock_response.markdown = MagicMock()
        mock_chat_message.return_value.__enter__.return_value = mock_response
        
        with patch('empire_chain.file_reader.DocumentReader.read', return_value="Test document content"), \
             patch.object(self.embeddings, 'embed', return_value=self.mock_embedding), \
             patch.object(self.vector_store, 'query', return_value=["Relevant text"]), \
             patch.object(self.llm, 'generate', return_value="This is a test document"):
            chatbot.chat()
            self.llm.generate.assert_called_once()

if __name__ == "__main__":
    unittest.main()