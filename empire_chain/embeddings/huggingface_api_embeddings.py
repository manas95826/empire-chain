import requests
import os
from dotenv import load_dotenv
from typing import List

load_dotenv()

class HFAPIEmbeddings:
    def __init__(self, model: str):
        self.model = model
        self.api_key = os.getenv("HUGGINGFACE_API_KEY")
        if not self.api_key:
            raise ValueError("HUGGINGFACE_API_KEY not found! Set it in your .env file.")

        self.api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{self.model}"
        self.headers = {"Authorization": f"Bearer {self.api_key}"}


    def embed(self, text: str) -> List[float]:
        response = requests.post(self.api_url, headers=self.headers, json={"inputs": text})
        if response.status_code == 200 and isinstance(response.json(), list):
            return response.json()
        raise Exception(f"Error: {response.status_code}, {response.text}")
