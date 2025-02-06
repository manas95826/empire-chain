from typing import List, Optional
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
import uuid
from empire_chain.vector_stores import VectorStore

class QdrantWrapper:
    """Wrapper class for Qdrant client operations."""
    
    def __init__(self, url: str = ":memory:"):
        """Initialize Qdrant client.
        
        Args:
            url: Qdrant server URL. Defaults to in-memory storage.
        """
        self.client = QdrantClient(url)
    
    def create_collection(self, name: str, vector_size: int = 1536) -> None:
        """Create a new collection in Qdrant.
        
        Args:
            name: Name of the collection
            vector_size: Size of the vectors to store
            
        Raises:
            RuntimeError: If collection creation fails
        """
        try:
            self.client.create_collection(
                collection_name=name,
                vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE)
            )
        except Exception as e:
            print(f"Error creating collection: {e}")
            
    def upsert(self, collection_name: str, points: List[PointStruct]) -> None:
        """Insert or update points in the collection.
        
        Args:
            collection_name: Name of the collection
            points: List of points to upsert
            
        Raises:
            RuntimeError: If upsert operation fails
        """
        try:
            self.client.upsert(collection_name=collection_name, points=points)
        except Exception as e:
            raise RuntimeError(f"Failed to upsert points: {e}")
        
    def search(self, collection_name: str, query_vector: List[float], limit: int = 10):
        """Search for similar vectors in the collection.
        
        Args:
            collection_name: Name of the collection
            query_vector: Vector to search for
            limit: Maximum number of results to return
            
        Returns:
            List of search results
            
        Raises:
            RuntimeError: If search operation fails
        """
        try:
            return self.client.search(
                collection_name=collection_name,
                query_vector=query_vector,
                limit=limit
            )
        except Exception as e:
            raise RuntimeError(f"Failed to perform search: {e}")

class QdrantVectorStore(VectorStore):
    def __init__(self, url: str = ":memory:", vector_size: int = 1536):
        self.client = QdrantWrapper(url)
        self.collection_name = "default"
        self.client.create_collection(self.collection_name, vector_size)

    def add(self, text: str, embedding: List[float]) -> None:
        """Add a text and its embedding to the store.
        
        Args:
            text: Text to store
            embedding: Vector embedding of the text
            
        Raises:
            RuntimeError: If add operation fails
        """
        point_id = str(uuid.uuid4())
        point = PointStruct(
            id=point_id,
            vector=embedding,
            payload={"text": text}
        )
        self.client.upsert(self.collection_name, [point])

    def query(self, query_embedding: List[float], k: int = 10) -> List[str]:
        """Query for similar texts.
        
        Args:
            query_embedding: Vector embedding to search for
            k: Number of results to return
            
        Returns:
            List of similar texts
            
        Raises:
            RuntimeError: If query operation fails
        """
        response = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_embedding,
            limit=k
        )
        return [hit.payload["text"] for hit in response] 