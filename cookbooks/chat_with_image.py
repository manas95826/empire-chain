from empire_chain.streamlit import VisionChatbot

vision_chatbot = VisionChatbot(title="Empire Vision Chatbot", verbose=False, custom_instructions="Please answer in json only title , description and summary. Don't include any other information.")
vision_chatbot.chat()