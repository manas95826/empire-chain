from typing import List, Optional, Dict, Any
from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance, 
    VectorParams, 
    PointStruct,
    HnswConfigDiff, 
    OptimizersConfigDiff,
    WalConfigDiff,
    QuantizationConfig,
    ScalarQuantization,
    ProductQuantization,
    ScalarType,
    CompressionRatio,
)
import uuid
from empire_chain.vector_stores import VectorStore

def get_default_hnsw_config() -> HnswConfigDiff:
    """Get default HNSW index configuration."""
    return HnswConfigDiff(
        m=16,  # Number of edges per node in the index graph
        ef_construct=100,  # Size of the dynamic candidate list for constructing the index
        full_scan_threshold=10000,  # Number of points after which to enable full scan
        max_indexing_threads=0,  # Auto-detect number of threads
        on_disk=False,  # Store index in RAM
    )

def get_default_optimizer_config() -> OptimizersConfigDiff:
    """Get default optimizer configuration."""
    return OptimizersConfigDiff(
        deleted_threshold=0.2,  # Minimal fraction of deleted vectors for optimization
        vacuum_min_vector_number=1000,  # Minimal number of vectors for optimization
        default_segment_number=0,  # Auto-detect optimal segment number
        max_segment_size=None,  # Default segment size
        memmap_threshold=None,  # Default memmap threshold
        indexing_threshold=20000,  # Minimal number of vectors for indexing
        flush_interval_sec=5,  # Interval between force flushes
        max_optimization_threads=0,  # Auto-detect number of threads
    )

def get_default_wal_config() -> WalConfigDiff:
    """Get default Write-Ahead-Log configuration."""
    return WalConfigDiff(
        wal_capacity_mb=32,  # Size of WAL segment
        wal_segments_ahead=0,  # Number of WAL segments to create ahead
    )

def get_default_quantization_config() -> QuantizationConfig:
    """Get default quantization configuration."""
    return QuantizationConfig(
        scalar=ScalarQuantization(
            type=ScalarType.INT8,  # 8-bit quantization
            always_ram=True,  # Keep quantized vectors in RAM
            quantile=0.99,  # Quantile for quantization
        ),
        product=ProductQuantization(
            compression=CompressionRatio.X4,  # 4x compression
            always_ram=True,  # Keep quantized vectors in RAM
        ),
    )

class QdrantWrapper:
    """Wrapper class for Qdrant client operations."""
    
    def __init__(
        self,
        url: str = None,
        prefer_grpc: bool = True,
        timeout: Optional[float] = None,
    ):
        """Initialize Qdrant client.
        
        Args:
            url: Qdrant server URL. If None, uses in-memory storage.
            prefer_grpc: Whether to prefer gRPC over HTTP. Defaults to True.
            timeout: Timeout for operations in seconds. None means no timeout.
        """
        if url == ":memory:" or url is None:
            self.client = QdrantClient(":memory:", prefer_grpc=prefer_grpc, timeout=timeout)
        else:
            self.client = QdrantClient(url=url, prefer_grpc=prefer_grpc, timeout=timeout)
    
    def create_collection(
        self,
        name: str,
        vector_size: int = 1536,
        distance: Distance = Distance.COSINE,
        hnsw_config: Optional[HnswConfigDiff] = None,
        wal_config: Optional[WalConfigDiff] = None,
        optimizers_config: Optional[OptimizersConfigDiff] = None,
        shard_number: int = 1,
        replication_factor: int = 1,
        write_consistency_factor: int = 1,
        on_disk_payload: bool = False,
        quantization_config: Optional[QuantizationConfig] = None,
        on_disk: bool = False,
        init_from: Optional[str] = None,
    ) -> None:
        """Create a new collection in Qdrant with customizable parameters.
        
        Args:
            name: Name of the collection
            vector_size: Size of the vectors to store
            distance: Distance function to use (COSINE, DOT, EUCLID, MANHATTAN)
            hnsw_config: HNSW index configuration parameters
            wal_config: Write-Ahead-Log related configuration
            optimizers_config: Parameters for optimization processes
            shard_number: Number of shards in the collection. Default is 1.
            replication_factor: Number of replicas for each shard. Default is 1.
            write_consistency_factor: How many replicas should confirm write. Default is 1.
            on_disk_payload: If true, payload will be stored on disk. Default is False.
            quantization_config: Vector quantization configuration
            on_disk: If true, vectors will be stored on disk using memmaps. Default is False.
            init_from: Initialize collection from existing collection
            
        Raises:
            RuntimeError: If collection creation fails
        """
        try:
            # Use default configurations if not provided
            hnsw_config = hnsw_config or get_default_hnsw_config()
            wal_config = wal_config or get_default_wal_config()
            optimizers_config = optimizers_config or get_default_optimizer_config()
            
            vectors_config = VectorParams(
                size=vector_size, 
                distance=distance,
                on_disk=on_disk
            )
            
            self.client.create_collection(
                collection_name=name,
                vectors_config=vectors_config,
                hnsw_config=hnsw_config,
                wal_config=wal_config,
                optimizers_config=optimizers_config,
                shard_number=shard_number,
                replication_factor=replication_factor,
                write_consistency_factor=write_consistency_factor,
                on_disk_payload=on_disk_payload,
                quantization_config=quantization_config,
                init_from=init_from,
            )
        except Exception as e:
            raise RuntimeError(f"Error creating collection: {e}")
            
    def upsert(self, collection_name: str, points: List[PointStruct], wait: bool = True) -> None:
        """Insert or update points in the collection.
        
        Args:
            collection_name: Name of the collection
            points: List of points to upsert
            wait: Whether to wait for changes to be applied. Default is True.
            
        Raises:
            RuntimeError: If upsert operation fails
        """
        try:
            self.client.upsert(
                collection_name=collection_name,
                points=points,
                wait=wait
            )
        except Exception as e:
            raise RuntimeError(f"Failed to upsert points: {e}")
        
    def search(
        self,
        collection_name: str,
        query_vector: List[float],
        limit: int = 10,
        offset: int = 0,
        score_threshold: Optional[float] = None,
        query_filter: Optional[Dict[str, Any]] = None,
        with_payload: bool = True,
        with_vectors: bool = False,
    ):
        """Search for similar vectors in the collection.
        
        Args:
            collection_name: Name of the collection
            query_vector: Vector to search for
            limit: Maximum number of results to return. Default is 10.
            offset: Number of records to skip. Default is 0.
            score_threshold: Minimal score threshold. Default is None.
            query_filter: Filter conditions for search. Default is None.
            with_payload: Whether to return payload. Default is True.
            with_vectors: Whether to return vectors. Default is False.
            
        Returns:
            List of search results
            
        Raises:
            RuntimeError: If search operation fails
        """
        try:
            return self.client.search(
                collection_name=collection_name,
                query_vector=query_vector,
                limit=limit,
                offset=offset,
                score_threshold=score_threshold,
                query_filter=query_filter,
                with_payload=with_payload,
                with_vectors=with_vectors,
            )
        except Exception as e:
            raise RuntimeError(f"Failed to perform search: {e}")

class QdrantVectorStore(VectorStore):
    """A vector store implementation using Qdrant.
    
    This class provides a simple interface for storing and querying text embeddings using Qdrant.
    It comes with sensible defaults for all settings, making it easy to use out of the box.
    
    Default Configuration:
        - Storage: In-memory (`:memory:`)
        - Collection name: "default"
        - Vector size: 1536 (compatible with many embedding models)
        - Distance metric: COSINE
        - Storage type: RAM (not on disk)
        - Query results: Top 10 by default
        - Point IDs: Automatically generated UUIDs
        
    HNSW Index Defaults:
        - m: 16 (edges per node)
        - ef_construct: 100 (candidates for index construction)
        - full_scan_threshold: 10000
        - max_indexing_threads: Auto-detected
        - on_disk: False (stored in RAM)
        
    Optimizer Defaults:
        - deleted_threshold: 0.2
        - vacuum_min_vector_number: 1000
        - indexing_threshold: 20000
        - flush_interval_sec: 5
        - max_optimization_threads: Auto-detected
        
    WAL (Write-Ahead-Log) Defaults:
        - wal_capacity_mb: 32
        - wal_segments_ahead: 0
        
    Example:
        ```python
        # Simple usage with all defaults
        store = QdrantVectorStore()
        
        # Add text with its embedding
        store.add(text="Hello world", embedding=[0.1, 0.2, ..., 0.9])
        
        # Query similar texts
        similar_texts = store.query(query_embedding=[0.15, 0.25, ..., 0.95])
        ```
    """
    
    def __init__(
        self,
        url: str = None,
        collection_name: str = "default",
        vector_size: int = 1536,
        distance: Distance = Distance.COSINE,
        on_disk: bool = False,
        hnsw_config: Optional[HnswConfigDiff] = None,
        quantization_config: Optional[QuantizationConfig] = None,
    ):
        """Initialize QdrantVectorStore with customizable parameters.
        
        Args:
            url: Qdrant server URL. If None, uses in-memory storage.
            collection_name: Name of the collection. Default is "default".
            vector_size: Size of the vectors to store. Default is 1536 (standard for many embedding models).
            distance: Distance function to use. Default is COSINE similarity.
            on_disk: If true, vectors will be stored on disk. Default is False (RAM storage).
            hnsw_config: HNSW index configuration parameters. Default uses optimal settings for most cases.
            quantization_config: Vector quantization configuration. Default is None (no quantization).
        
        Note:
            - In-memory storage (url=None) is perfect for testing and small datasets
            - For production with large datasets, provide a server URL and set on_disk=True
            - The default vector_size of 1536 works with many popular embedding models
            - COSINE distance is recommended for normalized embeddings
        """
        self.client = QdrantWrapper(url)
        self.collection_name = collection_name
        self.client.create_collection(
            name=collection_name,
            vector_size=vector_size,
            distance=distance,
            on_disk=on_disk,
            hnsw_config=hnsw_config,
            quantization_config=quantization_config,
        )

    def add(self, text: str, embedding: List[float]) -> None:
        """Add a text and its embedding to the store.
        
        Args:
            text: Text to store
            embedding: Vector embedding of the text. Should match the vector_size 
                      specified during initialization (default: 1536 dimensions)
            
        Raises:
            RuntimeError: If add operation fails
            
        Note:
            - Each text is automatically assigned a UUID
            - The embedding should be normalized if using COSINE distance
            - The operation waits for confirmation by default
        """
        point_id = str(uuid.uuid4())
        point = PointStruct(
            id=point_id,
            vector=embedding,
            payload={"text": text}
        )
        self.client.upsert(self.collection_name, [point])

    def query(
        self,
        query_embedding: List[float],
        k: int = 10,
        score_threshold: Optional[float] = None,
        filter: Optional[Dict[str, Any]] = None,
    ) -> List[str]:
        """Query for similar texts.
        
        Args:
            query_embedding: Vector embedding to search for. Should match the vector_size 
                           specified during initialization (default: 1536 dimensions)
            k: Number of results to return. Default is 10.
            score_threshold: Minimal similarity threshold. Default is None (no threshold).
            filter: Filter conditions for search. Default is None (no filtering).
            
        Returns:
            List of similar texts, ordered by similarity (most similar first)
            
        Raises:
            RuntimeError: If query operation fails
            
        Note:
            - Results are automatically sorted by similarity score
            - The query embedding should be normalized if using COSINE distance
            - The search includes payload by default but excludes vectors
            - No offset is used by default (starts from the first result)
        """
        response = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_embedding,
            limit=k,
            score_threshold=score_threshold,
            query_filter=filter,
        )
        return [hit.payload["text"] for hit in response] 