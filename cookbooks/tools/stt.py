from empire_chain.stt.stt import GroqSTT

stt = GroqSTT()
text = stt.transcribe("audio.mp3")
print(text)
