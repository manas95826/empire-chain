class VectorStore:
    def __init__(self, client):
        self.client = client

    def add(self, text: str, embedding: list[float]):
        pass

    def query(self, query_embedding: list[float], k: int = 10):
        pass 

def ChromaVectorStore(*args, **kwargs):
    from empire_chain.vector_stores.chroma import ChromaVectorStore as _ChromaVectorStore
    try:
        import chromadb
        return _ChromaVectorStore(*args, **kwargs)
    except ImportError:
        raise ImportError(
            "Could not import chroma. Please install the necessary dependencies with: "
            "pip install chromadb"
        )

def QdrantVectorStore(*args, **kwargs):
    from empire_chain.vector_stores.qdrant import QdrantVectorStore as _QdrantVectorStore
    try:
        import qdrant_client
        return _QdrantVectorStore(*args, **kwargs)
    except ImportError:
        raise ImportError(
            "Could not import qdrant. Please install the necessary dependencies with: "
            "pip install qdrant-client"
        )