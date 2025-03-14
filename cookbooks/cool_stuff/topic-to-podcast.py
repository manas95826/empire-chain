"""
This is a simple example of how to use the GeneratePodcast class to generate a podcast.
Please run the following command to install the necessary dependencies and store keys in .env:
!pip install empire-chain kokoro_onnx (It might take a while to download the model files)
"""
from empire_chain.cool_stuff.podcast import GeneratePodcast

podcast=GeneratePodcast()
podcast.generate(topic="""
Manas Chopra is a dynamic tech community leader, AI enthusiast, and the co-founder of Geek Room, a thriving community with over 50,000 members that has hosted multiple hackathons, including high-profile collaborations with Microsoft and MasterCard. Passionate about AI and product development, Manas has worked on diverse projects, from LLM-powered chatbots and vector database integrations to document data extraction and fantasy sports AI. With a keen interest in digital forensics and cybersecurity, he actively explores emerging technologies while mentoring students and professionals. Currently, he’s part of the AI team at myracle.io, driving innovation in AI-driven solutions. His expertise in prompt engineering, LangChain, and retrieval-augmented generation (RAG) makes him a valuable voice in the tech space.
""")
