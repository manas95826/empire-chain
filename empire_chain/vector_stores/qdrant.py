from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
import uuid
from empire_chain.vector_stores import VectorStore

class QdrantWrapper:
    def __init__(self, url: str = ":memory:"):
        self.client = QdrantClient(url)
    
    def create_collection(self, name: str, vector_size: int = 1536):
        try:
            self.client.create_collection(
                collection_name=name,
                vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE)
            )
        except Exception as e:
            print(f"Error creating collection: {e}")
            
    def upsert(self, collection_name: str, points: list[PointStruct]):
        self.client.upsert(collection_name=collection_name, points=points)
        
    def search(self, collection_name: str, query_vector: list[float], limit: int = 10):
        return self.client.search(
            collection_name=collection_name,
            query_vector=query_vector,
            limit=limit
        )

class QdrantVectorStore(VectorStore):
    def __init__(self, url: str = ":memory:", vector_size: int = 1536):
        self.client = QdrantWrapper(url)
        self.collection_name = "default"
        self.client.create_collection(self.collection_name, vector_size)

    def add(self, text: str, embedding: list[float]):
        point_id = str(uuid.uuid4())
        point = PointStruct(
            id=point_id,
            vector=embedding,
            payload={"text": text}
        )
        self.client.upsert(self.collection_name, [point])

    def query(self, query_embedding: list[float], k: int = 10):
        response = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_embedding,
            limit=k
        )
        return [hit.payload["text"] for hit in response] 