from abc import ABC, abstractmethod
from typing import List

class VectorStore(ABC):
    """Abstract base class for vector store implementations.
    
    This class defines the interface that all vector store implementations must follow.
    """
    
    @abstractmethod
    def add(self, text: str, embedding: List[float]) -> None:
        """Add a text and its embedding to the vector store.
        
        Args:
            text: The text to store
            embedding: The vector embedding of the text
        """
        pass

    @abstractmethod
    def query(self, query_embedding: List[float], k: int = 10) -> List[str]:
        """Query the vector store for similar texts.
        
        Args:
            query_embedding: The vector embedding to search for
            k: Number of results to return
            
        Returns:
            List of similar texts
        """
        pass

def QdrantVectorStore(*args, **kwargs):
    """Factory function for creating a QdrantVectorStore instance."""
    from empire_chain.vector_stores.qdrant import QdrantVectorStore as _QdrantVectorStore
    return _QdrantVectorStore(*args, **kwargs)

def QdrantWrapper(*args, **kwargs):
    """Factory function for creating a QdrantWrapper instance."""
    from empire_chain.vector_stores.qdrant import QdrantWrapper as _QdrantWrapper
    return _QdrantWrapper(*args, **kwargs)

__all__ = ['VectorStore', 'QdrantVectorStore', 'QdrantWrapper']