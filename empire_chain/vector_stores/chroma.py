import chromadb
import uuid
from empire_chain.vector_stores import VectorStore

class ChromaVectorStore(VectorStore):
    def __init__(self, client: chromadb.Client):
        super().__init__(client)
        self.collection_name = "default"
        self.collection = self.client.create_collection(name=self.collection_name)

    def add(self, text: str, embedding: list[float]):
        doc_id = str(uuid.uuid4())
        self.collection.add(
            documents=[text],
            embeddings=[embedding],
            metadatas=[{"source": "user"}],
            ids=[doc_id]
        )

    def query(self, query_embedding: list[float], k: int = 10):
        response = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=k
        )
        return response["documents"][0] 