"""
This example demonstrates how to use the QdrantVectorStore to store and query embeddings.
Requires an OpenAI API key and requirements as:
pip install empire-chain
"""
from empire_chain.vector_stores import QdrantVectorStore
from empire_chain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

store = QdrantVectorStore()

text = "your_text_here"
embedding = OpenAIEmbeddings("text-embedding-3-small")
store.add(text=text, embedding=embedding)

similar_texts = store.query("your_query_here")  # Returns top 10 similar texts by default