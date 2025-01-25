"""
This is a simple example of how to use the GeneratePodcast class to generate a podcast.
Please run the following command to install the necessary dependencies and store keys in .env:
!pip install empire-chain kokoro_onnx (It might take a while to download the model files)
"""
from empire_chain.cool_stuff.podcast import GeneratePodcast

podcast=GeneratePodcast()
podcast.generate(topic="About boom of meal plan and recipe generation apps")