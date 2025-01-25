import openai
from dotenv import load_dotenv
import os

load_dotenv()

class OpenAIEmbeddings:
    def __init__(self, model: str):
        self.model = model
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def embed(self, text: str) -> list[float]:
        response = self.client.embeddings.create(input=text, model=self.model)
        return response.data[0].embedding