"""
This is a simple chatbot that uses the Empire Chain library to create a pdf chatbot.
Please run the following command to install the necessary dependencies and store keys in .env:
!pip install empire-chain streamlit sentence-transformers
!streamlit run app.py
"""
from empire_chain.embeddings import HFEmbeddings
from empire_chain.vector_stores import QdrantVectorStore
from empire_chain.streamlit import PDFChatbot
from empire_chain.llms.llms import GroqLLM

pdf_chatbot = PDFChatbot(title="Empire PDF Chatbot",llm=GroqLLM("llama3-8b-8192"),vector_store=QdrantVectorStore(vector_size=384),embeddings=HFEmbeddings("all-MiniLM-L6-v2"))
pdf_chatbot.chat()
