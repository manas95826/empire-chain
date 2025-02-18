from openai import OpenAI
from anthropic import Anthropic
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

class LLM:
    def __init__(self, model: str, api_key: str = None, custom_instructions: str = ""):
        self.model = model
        self.api_key = api_key
        self.custom_instructions = custom_instructions
    def generate(self, prompt: str) -> str:
        pass

class OpenAILLM(LLM):
    def __init__(self, model: str = "gpt-4o-mini", api_key: str = None, custom_instructions: str = ""):
        super().__init__(model, api_key, custom_instructions)
        self.client = OpenAI(api_key=self.api_key or os.getenv("OPENAI_API_KEY"))

    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model, 
            messages=[
                {"role": "system", "content": self.custom_instructions}, 
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content

class AnthropicLLM(LLM):
    def __init__(self, model: str = "claude-3-5-sonnet-20240620", api_key: str = None, custom_instructions: str = ""):
        super().__init__(model, api_key, custom_instructions)
        self.client = Anthropic(api_key=self.api_key or os.getenv("ANTHROPIC_API_KEY"))

    def generate(self, prompt: str) -> str:
        response = self.client.messages.create(
            model=self.model,
            max_tokens=1000,
            messages=[{"role": "system", "content": self.custom_instructions}, {"role": "user", "content": prompt}]
        )
        return response.content[0].text
    
class GroqLLM(LLM):
    def __init__(self, model: str = "llama3-8b-8192", api_key: str = None, custom_instructions: str = ""):
        super().__init__(model, api_key, custom_instructions)
        self.client = Groq(api_key=self.api_key or os.getenv("GROQ_API_KEY"))

    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model, 
            messages=[
                {"role": "system", "content": self.custom_instructions}, 
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content


class GeminiLLM(LLM):
    def __init__(self, model: str = "gemini-1.5-flash", api_key: str = None, custom_instructions: str = ""):
        super().__init__(model, api_key, custom_instructions)
        self.client = OpenAI(
            api_key=self.api_key or os.getenv("GEMINI_API_KEY"),
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )

    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            n=1,
            messages=[
                {"role": "system", "content": self.custom_instructions},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    