from empire_chain.vector_stores import QdrantVectorStore
from empire_chain.embeddings import OpenAIEmbeddings
from empire_chain.llms.llms import GroqLLM
from empire_chain.tools.file_reader import DocumentReader
import os
from dotenv import load_dotenv
from empire_chain.stt.stt import GroqSTT

def main(if_audio_input: bool = False):
    load_dotenv()
    
    vector_store = QdrantVectorStore(":memory:")
    embeddings = OpenAIEmbeddings("text-embedding-3-small")
    llm = GroqLLM("llama3-8b-8192")
    reader = DocumentReader()
    
    file_path = "input.pdf"
    text = reader.read(file_path)
    
    text_embedding = embeddings.embed(text)
    vector_store.add(text, text_embedding)
    
    text_query = "What is the main topic of this document?"
    if if_audio_input:
        stt = GroqSTT()
        audio_query = stt.transcribe("audio.mp3")
        query_embedding = embeddings.embed(audio_query)
    else:
        query_embedding = embeddings.embed(text_query)
    relevant_texts = vector_store.query(query_embedding, k=3)
    
    context = "\n".join(relevant_texts)
    prompt = f"Based on the following context, {text_query}\n\nContext: {context}"
    response = llm.generate(prompt)
    print(f"Query: {text_query}")
    print(f"Response: {response}")

if __name__ == "__main__":
    main(if_audio_input=False)