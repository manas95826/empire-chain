import chromadb
from typing import List, Dict, Optional
from empire_chain.vector_stores import VectorStore



def get_default_hnsw_config() -> Dict[str, any]:
    """Get default HNSW index configuration."""
    return {
        "hnsw:space": "l2",  # Distance metric: 'l2', 'cosine', or 'ip'
        "hnsw:construction_ef": 100,  # Controls the number of neighbors explored during index construction
        "hnsw:M": 16,  # Maximum number of connections for each element in the graph
        "hnsw:search_ef": 100,  # Controls the number of neighbors explored during search

    }

class ChromaDBWrapper:
    """Wrapper for ChromaDB client operations"""

    def __init__(
            self,
            chroma_client : str = None,
            persist_dir: str = None,
            host: str = "localhost",
            port: int = 8080,
    ):
        """Initialize ChromaDB client wrapper
        
        Args:
            chroma_client: ChromaDB client
            persist_dir: Directory to persist ChromaDB data , if None uses in-memory storage
            host: ChromaDB server host
            port: ChromaDB server port
        """
        if chroma_client == "persistent":
            if not persist_dir:
                raise ValueError("Persist directory required for persistent client")
            self.client = chromadb.PersistentClient(path=persist_dir)
        if chroma_client == "http":
            self.client = chromadb.HttpClient(host=host, port=port)
        else:
            self.client = chromadb.Client()
        
    def create_collection(
            self,
            name: str,
            emd_fn: Optional[callable] = None,
            metadata: Optional[Dict[str,any]] = None,
    ):
        """Create a collection in ChromaDB with customizable EMD function
        
        Args:
            name: Collection name
            emd_fn: Embd function
            metadata: Collection metadata
        """
        metadata = get_default_hnsw_config()
        try:
            return self.client.create_collection(
                name=name,
                embedding_function=emd_fn,
                metadata=metadata,
            )
        except Exception as e:
            raise Exception(f"Error creating collection:{e}")
        
    def insert(
            self,
            collection: str,
            documents: List[str],
            id: List[str],
            embeddings: Optional[List[List[float]]] = None,
            metadata: Optional[Dict[str, str]] = None,
    ):
        """Add documents to a collection
        
        Args:
            documents: List of documents
            id: List of ids
            embeddings: List of embeddings
            metadata: Document metadata
        """
        try:
            collection = self.client.get_or_create_collection(collection)
            return collection.add(
                documents=documents,
                ids=id,
                embeddings=embeddings,
                metadata=metadata,
            )
        except Exception as e:
            raise Exception(f"Error adding documents to collection:{e}")
    
    def remove(
            self,
            collection:str,
            ids: Optional[List[str]] = None,
            where: Optional[Dict[str, str]] = None,
    ):
        """Remove documents from a collection 
        
        Args:
            collection: Collection name
            ids: List of ids
            where: Filter query
        """
        try:
            collection = self.client.get_or_create_collection(collection)
            return collection.remove(
                ids=ids,
                where=where,
            )
        except Exception as e:
            raise Exception(f"Error removing documents from collection:{e}")
        
    def search(
            self,
            collection: str,
            query_embedding: List[List[float]] = None,
            query_texts: List[str] = None,
            num_results: int = 10,
            ids: List[str] = None,
            include: List[str] = None,
            where: Optional[Dict[str, str]] = None,
            where_documents: Optional[Dict[str,str]] = None,
    ):
        """Search for items in a collection
        
        Args:
            collection: Collection name
            query_embedding: Query embedding
            query_items: Query items
            num_results: Number of results to return
            ids: List of ids to return
            include: List of fields to include in response
            where: Filter query
            where_documents: Filter documents
        """
        try:
            collection = self.client.get_or_create_collection(collection)
            if query_embedding:
                return collection.query(
                    query_embeddings=query_embedding,
                    n_results = num_results,
                    where=where,
                    include=include,
                    where_documents=where_documents,
                )
            elif query_texts:
                return collection.query(
                    query_items=query_texts,
                    n_results = num_results,
                    where=where,
                    include=include,
                    where_documents=where_documents,
                )
            elif ids:
                return collection.get(
                    ids=ids,
                    include=include,
                    where=where,
                    where_documents=where_documents,
                )
            else:
                raise ValueError("Query embedding or query items required")
        except Exception as e:
            raise Exception(f"Error searching collection:{e}")
        
class ChromaVectorStore(VectorStore):
    def __init__(
            self,
            chroma_client: str = None,
            persist_dir: str = None,
            host: str = "localhost",
            port: int = 8080,
    ):
        """Initialize ChromaDB vector store
        
        Args:
            chroma_client: ChromaDB client
            persist_dir: Directory to persist ChromaDB data , if None uses in-memory storage
            host: ChromaDB host
            port: ChromaDB port
        """
        self.client = ChromaDBWrapper(
            chroma_client=chroma_client,
            persist_dir=persist_dir,
            host=host,
            port=port,
        )
    def add(
            self,
            collection: str,
            documents: List[str],
            id: List[str],
            embeddings: Optional[List[List[float]]] = None,
            metadata: Optional[Dict[str, str]] = None,
    ):
        """Add documents to a collection
        
        Args:
            documents: List of documents
            id: List of ids
            embeddings: List of embeddings
            metadata: Document metadata
        """
        return self.client.insert(
            collection=collection,
            documents=documents,
            id=id,
            embeddings=embeddings,
            metadata=metadata,
        )
    def delete(
            self,
            collection: str,
            ids: Optional[List[str]] = None,
            where: Optional[Dict[str, str]] = None,
    ):
        """Remove documents from a collection 
        
        Args:
            collection: Collection name
            ids: List of ids
            where: Filter query
        """
        return self.client.remove(
            collection=collection,
            ids=ids,
            where=where,
    )
    def query(
            self,
            collection: str,
            query_embedding: List[List[float]] = None,
            query_texts: List[str] = None,
            num_results: int = 10,
            ids: List[str] = None,
            include: List[str] = None,
            where: Optional[Dict[str, str]] = None,
            where_documents: Optional[Dict[str,str]] = None,
    ):
        """Query a collection
        
        Args:
            collection: Collection name
            query_embedding: Query embedding
            query_items: Query items
            num_results: Number of results to return
            ids: List of ids to return
            include: List of fields to include in response
            where: Filter query
            where_documents: Filter documents
        """
        return self.client.search(
            collection=collection,
            query_embedding=query_embedding,
            query_items=query_texts,
            num_results=num_results,
            ids=ids,
            include=include,
            where=where,
            where_documents=where_documents,
        )
