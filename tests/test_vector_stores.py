from empire_chain.vector_stores import QdrantVectorStore, ChromaVectorStore, QdrantWrapper
from unittest.mock import Mock, MagicMock
import unittest

class TestVectorStores(unittest.TestCase):
    def test_qdrant_vector_store(self):
        mock_wrapper = Mock()
        mock_hit = MagicMock()
        mock_hit.payload = {"text": "Hello, world!"}
        mock_wrapper.search.return_value = [mock_hit]
        
        vector_store = QdrantVectorStore()
        vector_store.client = mock_wrapper
        
        vector_store.add("Hello, world!", [1, 2, 3])
        mock_wrapper.upsert.assert_called_once()
        
        results = vector_store.query([1, 2, 3], k=1)
        self.assertEqual(results, ["Hello, world!"])
        mock_wrapper.search.assert_called_once()

    def test_chroma_vector_store(self):
        mock_client = Mock()
        mock_collection = Mock()
        mock_client.create_collection.return_value = mock_collection
        
        mock_collection.query.return_value = {
            "documents": [["Hello, world!"]]
        }
        
        vector_store = ChromaVectorStore(mock_client)
        
        vector_store.add("Hello, world!", [1, 2, 3])
        mock_collection.add.assert_called_once()
        
        results = vector_store.query([1, 2, 3], k=1)
        self.assertEqual(results, ["Hello, world!"])
        mock_collection.query.assert_called_once()

if __name__ == "__main__":
    unittest.main()