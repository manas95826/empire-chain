def Chatbot():
    try:
        from empire_chain.streamlit.base_chatbot import Chatbot as BaseChatbot
        return BaseChatbot
    except ImportError as e:
        raise ImportError("Could not import Chatbot. Please install required dependencies: pip install openai") from e

def VisionChatbot():
    try:
        from empire_chain.streamlit.vision_chatbot import VisionChatbot as VisionChatbotClass
        return VisionChatbotClass
    except ImportError as e:
        raise ImportError("Could not import VisionChatbot. Please install required dependencies: pip install groq pillow") from e

def PDFChatbot():
    try:
        from empire_chain.streamlit.pdf_chatbot import PDFChatbot as PDFChatbotClass
        return PDFChatbotClass
    except ImportError as e:
        raise ImportError("Could not import PDFChatbot. Please install required dependencies: pip install chromadb qdrant-client") from e 