"""
This example demonstrates how to use the QdrantVectorStore to store and query embeddings.
Requires an OpenAI API key and requirements as:
pip install empire-chain
"""
from empire_chain.vector_stores import QdrantVectorStore
from empire_chain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings("text-embedding-3-small")

vector_store = QdrantVectorStore(url=":memory:")

text = """
your text here
"""

vector_store.add(text, embeddings.embed(text))

print(vector_store.query(embeddings.embed("what's the cost of the product?"), k=1))