from empire_chain.streamlit import PDFChatbot
from empire_chain.llms import OpenAILLM
from empire_chain.vector_stores import QdrantVectorStore
from empire_chain.embeddings import OpenAIEmbeddings

pdf_chatbot = PDFChatbot(title="PDF Chatbot", llm=OpenAILLM("gpt-4o-mini"), vector_store=QdrantVectorStore(":memory:"), embeddings=OpenAIEmbeddings("text-embedding-3-small"))
pdf_chatbot.chat()