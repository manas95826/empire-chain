from empire_chain.embeddings import OpenAIEmbeddings, SentenceTransformerEmbeddings
import unittest
from dotenv import load_dotenv

class TestEmbeddings(unittest.TestCase):
    def setUp(self):
        load_dotenv()

    def test_openai_embeddings(self):
        embeddings = OpenAIEmbeddings("text-embedding-3-small")
        embedding = embeddings.embed("What is the capital of France?")
        print(embedding)

    def test_sentence_transformer_embeddings(self):
        embeddings = SentenceTransformerEmbeddings("all-MiniLM-L6-v2")
        embedding = embeddings.embed("What is the capital of France?")
        print(embedding)

if __name__ == "__main__":
    unittest.main()