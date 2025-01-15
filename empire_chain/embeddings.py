from openai import OpenAI
from sentence_transformers import SentenceTransformer
import os

class Embeddings:
    def __init__(self, model: str):
        self.model = model

    def embed(self, text: str) -> list[float]:
        pass

class OpenAIEmbeddings(Embeddings):
    def __init__(self, model: str):
        super().__init__(model)
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def embed(self, text: str) -> list[float]:
        response = self.client.embeddings.create(input=text, model=self.model)
        return response.data[0].embedding
    
class SentenceTransformerEmbeddings(Embeddings):
    def __init__(self, model: str):
        super().__init__(model)
        self.model = SentenceTransformer(model)

    def embed(self, text: str) -> list[float]:
        return self.model.encode(text)