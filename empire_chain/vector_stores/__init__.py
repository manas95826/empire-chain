class VectorStore:
    def __init__(self, client):
        self.client = client
    def add(self, text: str, embedding: list[float]):
        pass
    def query(self, query_embedding: list[float], k: int = 10):
        pass

def QdrantVectorStore(*args, **kwargs):
    from empire_chain.vector_stores.qdrant import QdrantVectorStore as _QdrantVectorStore
    return _QdrantVectorStore(*args, **kwargs)