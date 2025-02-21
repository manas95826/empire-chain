from openai import OpenAI
from anthropic import Anthropic
from groq import Groq
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from mistralai import Mistral
from together import Together
load_dotenv()

class LLM:
    def __init__(self, model: str, custom_instructions: str = ""):
        self.model = model
        self.custom_instructions = custom_instructions
    def generate(self, prompt: str) -> str:
        pass

class OpenAILLM(LLM):
    def __init__(self, model: str = "gpt-4o-mini", custom_instructions: str = ""):
        super().__init__(model, custom_instructions)
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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
    def __init__(self, model: str = "claude-3-5-sonnet-20240620", custom_instructions: str = ""):
        super().__init__(model, custom_instructions)
        self.client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    def generate(self, prompt: str) -> str:
        response = self.client.messages.create(
            model=self.model,
            max_tokens=1000,
            messages=[{"role": "system", "content": self.custom_instructions}, {"role": "user", "content": prompt}]
        )
        return response.content[0].text
    
class GroqLLM(LLM):
    def __init__(self, model: str = "llama3-8b-8192", custom_instructions: str = ""):
        super().__init__(model, custom_instructions)
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

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
    def __init__(self, model: str = "gemini-1.5-flash", custom_instructions: str = ""):
        super().__init__(model, custom_instructions)
        self.client = OpenAI(
            api_key=os.getenv("GEMINI_API_KEY"),
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
    

class HuggingFaceLLM(LLM):
    def __init__(self,model:str="HuggingFaceh4/zephyr-7b-beta", custom_instructions:str = ""):
        if os.getenv("HUGGINGFACE_API_KEY") is None:
            raise ValueError("HUGGINGFACE_API_KEY is not set")
        super().__init__(model, custom_instructions)
        self.client = InferenceClient(api_key=os.getenv("HUGGINGFACE_API_KEY"))

    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model, 
            messages=[
                {"role": "system", "content": self.custom_instructions}, 
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    


class MistralLLM(LLM):
    def __init__(self, model: str = "codestral-large", custom_instructions: str = ""):
        super().__init__(model, custom_instructions)
        api_key = os.getenv("MISTRAL_API_KEY")
        if api_key is None:
            raise ValueError("MISTRAL_API_KEY environment variable is not set.")
        self.client = Mistral(api_key=api_key)

    def generate(self, prompt: str) -> str:
        response = self.client.chat.complete(
            model=self.model,
            messages=[
                {"role": "system", "content": self.custom_instructions},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    
class TogetherAI(LLM):
    def __init__(self, model: str = "meta-llama/Llama-3.3-70B-Instruct-Turbo", custom_instructions: str = ""):
        super().__init__(model, custom_instructions)
        api_key = os.getenv("TOGETHERAI_API_KEY")
        if api_key is None:
            raise ValueError("TOGETHERAI_API_KEY environment variable is not set.")
        self.client = Together(api_key=api_key)

    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.custom_instructions},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content