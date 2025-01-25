def Chatbot():
    from empire_chain.streamlit.base_chatbot import Chatbot
    return Chatbot

def VisionChatbot():
    from empire_chain.streamlit.vision_chatbot import VisionChatbot
    return VisionChatbot

def PDFChatbot():
    from empire_chain.streamlit.pdf_chatbot import PDFChatbot
    return PDFChatbot

__all__ = ['Chatbot', 'VisionChatbot', 'PDFChatbot'] 