from empire_chain.stt.stt import GroqSTT
from empire_chain.stt.stt import HuggingFaceSTT
from dotenv import load_dotenv
import os
load_dotenv()

stt = GroqSTT()
text = stt.transcribe("audio.mp3")
print(text)
