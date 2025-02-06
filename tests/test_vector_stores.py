from empire_chain.vector_stores.qdrant import QdrantVectorStore, QdrantWrapper
from qdrant_client.models import (
    Distance,
    HnswConfigDiff,
    VectorParams,
    OptimizersConfigDiff,
    WalConfigDiff,
    QuantizationConfig,
    ScalarQuantization,
    ScalarType,
)
from unittest.mock import Mock, MagicMock, patch
import unittest
import uuid

class TestQdrantVectorStore(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.mock_wrapper = Mock()
        self.mock_hit = MagicMock()
        self.mock_hit.payload = {"text": "Hello, world!"}
        self.mock_wrapper.search.return_value = [self.mock_hit]
        
        # Create a vector store with mocked client
        with patch('empire_chain.vector_stores.qdrant.QdrantWrapper') as mock_wrapper_class:
            mock_wrapper_class.return_value = self.mock_wrapper
            self.vector_store = QdrantVectorStore()

    def test_initialization_default(self):
        """Test initialization with default parameters."""
        with patch('empire_chain.vector_stores.qdrant.QdrantWrapper') as mock_wrapper:
            store = QdrantVectorStore()
            mock_wrapper.assert_called_once_with(None)
            mock_wrapper.return_value.create_collection.assert_called_once()

    def test_initialization_custom(self):
        """Test initialization with custom parameters."""
        with patch('empire_chain.vector_stores.qdrant.QdrantWrapper') as mock_wrapper:
            # Create a proper quantization config using dictionary format
            quantization_config = {
                "scalar": {
                    "type": ScalarType.INT8,
                    "quantile": 0.99,
                    "always_ram": True
                }
            }
            
            store = QdrantVectorStore(
                url="localhost:6333",
                collection_name="test_collection",
                vector_size=768,
                distance=Distance.EUCLID,
                on_disk=True,
                hnsw_config=HnswConfigDiff(m=32),
                quantization_config=quantization_config
            )
            mock_wrapper.assert_called_once_with("localhost:6333")
            mock_wrapper.return_value.create_collection.assert_called_once_with(
                name="test_collection",
                vector_size=768,
                distance=Distance.EUCLID,
                on_disk=True,
                hnsw_config=HnswConfigDiff(m=32),
                quantization_config=quantization_config
            )

    def test_add_text(self):
        """Test adding text and embedding."""
        text = "Hello, world!"
        embedding = [1.0, 2.0, 3.0]
        self.vector_store.add(text, embedding)
        
        # Verify upsert was called with correct parameters
        self.mock_wrapper.upsert.assert_called_once()
        call_args = self.mock_wrapper.upsert.call_args
        self.assertEqual(call_args[0][0], "default")  # collection name
        points = call_args[0][1]
        self.assertEqual(len(points), 1)
        self.assertEqual(points[0].payload["text"], text)
        self.assertEqual(points[0].vector, embedding)
        self.assertTrue(isinstance(points[0].id, str))

    def test_query_basic(self):
        """Test basic query functionality."""
        query_embedding = [1.0, 2.0, 3.0]
        results = self.vector_store.query(query_embedding)
        
        self.mock_wrapper.search.assert_called_once_with(
            collection_name="default",
            query_vector=query_embedding,
            limit=10,
            score_threshold=None,
            query_filter=None
        )
        self.assertEqual(results, ["Hello, world!"])

    def test_query_with_parameters(self):
        """Test query with custom parameters."""
        query_embedding = [1.0, 2.0, 3.0]
        filter_dict = {"category": "test"}
        results = self.vector_store.query(
            query_embedding=query_embedding,
            k=5,
            score_threshold=0.8,
            filter=filter_dict
        )
        
        self.mock_wrapper.search.assert_called_once_with(
            collection_name="default",
            query_vector=query_embedding,
            limit=5,
            score_threshold=0.8,
            query_filter=filter_dict
        )

    def test_query_empty_results(self):
        """Test query with no results."""
        self.mock_wrapper.search.return_value = []
        results = self.vector_store.query([1.0, 2.0, 3.0])
        self.assertEqual(results, [])

    def test_query_multiple_results(self):
        """Test query with multiple results."""
        mock_hits = [
            MagicMock(payload={"text": "First result"}),
            MagicMock(payload={"text": "Second result"}),
            MagicMock(payload={"text": "Third result"})
        ]
        self.mock_wrapper.search.return_value = mock_hits
        
        results = self.vector_store.query([1.0, 2.0, 3.0], k=3)
        self.assertEqual(results, ["First result", "Second result", "Third result"])

    def test_error_handling_add(self):
        """Test error handling during add operation."""
        # Setup the mock to raise an exception
        error_msg = "Upsert failed"
        self.mock_wrapper.upsert.side_effect = RuntimeError(error_msg)
        
        # Test that the exception is properly caught and re-raised
        with self.assertRaises(RuntimeError) as context:
            self.vector_store.add("test", [1.0, 2.0, 3.0])
        self.assertEqual(str(context.exception), error_msg)

    def test_error_handling_query(self):
        """Test error handling during query operation."""
        # Setup the mock to raise an exception
        error_msg = "Search failed"
        self.mock_wrapper.search.side_effect = RuntimeError(error_msg)
        
        # Test that the exception is properly caught and re-raised
        with self.assertRaises(RuntimeError) as context:
            self.vector_store.query([1.0, 2.0, 3.0])
        self.assertEqual(str(context.exception), error_msg)

    def test_wrapper_initialization(self):
        """Test QdrantWrapper initialization."""
        with patch('empire_chain.vector_stores.qdrant.QdrantClient') as mock_client:
            # Test in-memory initialization
            wrapper = QdrantWrapper()
            mock_client.assert_called_with(":memory:", prefer_grpc=True, timeout=None)
            
            # Test URL initialization
            wrapper = QdrantWrapper(url="localhost:6333")
            mock_client.assert_called_with(url="localhost:6333", prefer_grpc=True, timeout=None)
            
            # Test with custom parameters
            wrapper = QdrantWrapper(url="localhost:6333", prefer_grpc=False, timeout=30)
            mock_client.assert_called_with(url="localhost:6333", prefer_grpc=False, timeout=30)

    def test_wrapper_create_collection(self):
        """Test QdrantWrapper create_collection method."""
        wrapper = QdrantWrapper()
        wrapper.client = Mock()
        
        # Test with default parameters
        wrapper.create_collection("test_collection")
        wrapper.client.create_collection.assert_called_once()
        
        # Test with custom parameters
        wrapper.client.reset_mock()
        wrapper.create_collection(
            name="test_collection",
            vector_size=768,
            distance=Distance.EUCLID,
            on_disk=True
        )
        wrapper.client.create_collection.assert_called_once()

    def test_wrapper_error_handling(self):
        """Test QdrantWrapper error handling."""
        wrapper = QdrantWrapper()
        wrapper.client = Mock()
        error_msg = "Creation failed"
        wrapper.client.create_collection.side_effect = RuntimeError(error_msg)
        
        with self.assertRaises(RuntimeError) as context:
            wrapper.create_collection("test_collection")
        self.assertEqual(str(context.exception), f"Error creating collection: {error_msg}")

if __name__ == "__main__":
    unittest.main()