from empire_chain.llms.llms import OpenAILLM, AnthropicLLM, GroqLLM, GeminiLLM , HuggingFaceLLM , MistralLLM, TogetherAI
import unittest
import os
from unittest.mock import patch
from dotenv import load_dotenv

class TestLLMs(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        self.env_patcher = patch.dict('os.environ', {
            'OPENAI_API_KEY': os.getenv('OPENAI_API_KEY', 'test-openai-key'),
            'ANTHROPIC_API_KEY': os.getenv('ANTHROPIC_API_KEY', 'test-anthropic-key'),
            'GROQ_API_KEY': os.getenv('GROQ_API_KEY', 'test-groq-key'),
            "GEMINI_API_KEY": os.getenv('GEMINI_API_KEY', 'test-gemini-key'),
            "HUGGINGFACE_API_KEY": os.getenv('HUGGINGFACE_API_KEY', 'test-huggingface-key'),
            "MISTRAL_API_KEY": os.getenv('MISTRAL_API_KEY', 'test-mistral-key'),
            "TOGETHERAI_API_KEY": os.getenv('TOGETHERAI_API_KEY', 'test-together-key')
        })
        self.env_patcher.start()

    def tearDown(self):
        self.env_patcher.stop()

    def test_openai_llm(self):
        llm = OpenAILLM("gpt-4o-mini")
        response = llm.generate("What is the capital of France?")
        print(response)

    def test_anthropic_llm(self):
        llm = AnthropicLLM("claude-3-5-sonnet-20240620")
        response = llm.generate("What is the capital of France?")
        print(response)
    
    def test_groq_llm(self):
        llm = GroqLLM("llama3-8b-8192")
        response = llm.generate("What is the capital of France?")
        print(response)
    
    def test_gemini_llm(self):
        llm = GeminiLLM("gemini-1.5-pro")
        response = llm.generate("What is the capital of France?")
        print(response)

    def test_huggingface_llm(self):
        llm = HuggingFaceLLM("HuggingFaceh4/zephyr-7b-beta")
        response = llm.generate("What is the capital of France?")
        print(response)
    def test_mistral_llm(self):
        llm = MistralLLM("mistral-small-latest")
        response = llm.generate("What is the capital of France?")
        print(response)

    def test_together_llm(self):
        llm = TogetherAI("deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free")
        response = llm.generate("What is the capital of France?")
        print(response)
 


if __name__ == "__main__":
    unittest.main()