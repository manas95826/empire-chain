from empire_chain.embeddings import OpenAIEmbeddings, HFEmbeddings, HFAPIEmbeddings
import unittest
from dotenv import load_dotenv

class TestEmbeddings(unittest.TestCase):
    def setUp(self):
        load_dotenv()

    def test_openai_embeddings(self):
        embeddings = OpenAIEmbeddings("text-embedding-3-small")
        embedding = embeddings.embed("He is a good boy.")
        print(embedding)

    def test_sentence_transformer_embeddings(self):
        embeddings = HFEmbeddings("all-MiniLM-L6-v2")
        embedding = embeddings.embed("He is a good boy.")
        print(embedding)
    
    def test_hf_api_embeddings(self):
        embeddings = HFAPIEmbeddings("sentence-transformers/all-MiniLM-L6-v2")
        embedding = embeddings.embed("He is a good boy.")
        print(embedding)

if __name__ == "__main__":
    unittest.main()

