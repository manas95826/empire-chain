from dotenv import load_dotenv
import os
from groq import Groq
import requests
load_dotenv()

client = Groq()

class GroqSTT:
    def __init__(self, model: str = "whisper-large-v3"):
        self.client = Groq()
        self.model = model

    def transcribe(self, filename: str) -> str:
        with open(filename, "rb") as file:
            transcription = self.client.audio.transcriptions.create(
                file=(filename, file.read()),
                model=self.model,
                response_format="verbose_json",
                language="en",
            )
        return transcription.text
    

class HuggingFaceSTT:
    def __init__(self, model_name: str = "openai/whisper-large-v3-turbo"):
        self.model_name = model_name
        self.API_URL = f"https://api-inference.huggingface.co/models/{model_name}"
        self.headers = {"Authorization": f"Bearer {os.getenv('HF_API_KEY')}"}

    def transcribe(self, filename: str) -> str:
        with open(filename, "rb") as f:
            data = f.read()
        response = requests.post(self.API_URL, headers=self.headers, data=data)
        return response.json()["text"]      