from empire_chain.embeddings.openai_embeddings import OpenAIEmbeddings

def HFEmbeddings(*args, **kwargs):
    try:
        from empire_chain.embeddings.sentence_transformers_embeddings import HFEmbeddings as _HFEmbeddings
        return _HFEmbeddings(*args, **kwargs)
    except ImportError:
        raise ImportError(
            "Could not import sentence-transformers. Please install it with: "
            "pip install sentence-transformers"
        )

__all__ = ["OpenAIEmbeddings", "HFEmbeddings"]