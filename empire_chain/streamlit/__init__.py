def Chatbot(*args, **kwargs):
    from empire_chain.streamlit.base_chatbot import Chatbot as _Chatbot
    return _Chatbot(*args, **kwargs)

def VisionChatbot(*args, **kwargs):
    from empire_chain.streamlit.vision_chatbot import VisionChatbot as _VisionChatbot
    return _VisionChatbot(*args, **kwargs)

def PDFChatbot(*args, **kwargs):
    try:
        from empire_chain.streamlit.pdf_chatbot import PDFChatbot as _PDFChatbot
    except ImportError:
        raise ImportError(
            "Could not import pdf_chatbot. Please install necessary dependencies with: "
            "pip install chroma-db sentence-transformers"
        )
    return _PDFChatbot(*args, **kwargs)

__all__ = ["Chatbot", "VisionChatbot", "PDFChatbot"]