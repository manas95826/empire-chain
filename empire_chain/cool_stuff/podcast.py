import soundfile as sf
from kokoro_onnx import Kokoro
import numpy as np
import random
from groq import Groq
from dotenv import load_dotenv
import json
import os
import requests
from pathlib import Path
import tempfile
from tqdm import tqdm


class GeneratePodcast:
    def __init__(self):
        load_dotenv()
        pass

    def download_required_files(self):
        """Download required model and voices files if they don't exist."""
        files = {
            "kokoro-v0_19.onnx": "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/kokoro-v0_19.onnx",
            "voices.json": "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/voices.json"
        }
        
        for filename, url in files.items():
            if not os.path.exists(filename):
                print(f"Downloading {filename} from {url}...")
                response = requests.get(url, stream=True)
                total_size = int(response.headers.get('content-length', 0))
                block_size = 1024  

                with open(filename, "wb") as f, tqdm(
                    desc=filename,
                    total=total_size,
                    unit='iB',
                    unit_scale=True,
                    unit_divisor=1024,
                ) as bar:
                    for data in response.iter_content(block_size):
                        f.write(data)
                        bar.update(len(data))
                print(f"Downloaded {filename} successfully.")
            else:
                print(f"{filename} already exists, skipping download.")

    def load_dotenv(self):
        load_dotenv()

    def client(self, topic: str):
        client = Groq()
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {
                    "role": "system",
                    "content": """You are a podcast scriptwriter. You'll be giving the sentences for a podcast related to a particular topic. Generate as many sentences as you can. User will provide the topic. 
                    Available voices are af, af_bella, af_sarah, af_sky, am_adam, am_michael, bf_emma, bf_isabella, bm_george, bm_lewis
                    You shouldn't return anything else, just the array of json objects.

                    Example output:
                    [
                        {
                            "voice": "sarah",
                            "text": "Hello and welcome to the podcast! We've got some exciting things lined up today."
                        },
                        {
                            "voice": "michael",
                            "text": "It's going to be an exciting episode. Stick with us!"
                        },
                        ...etc
                    ]
                    """
                },
                {
                    "role": "user",
                    "content": f"My topic is '{topic}'."
                }
            ],
            temperature=0.3,
            max_completion_tokens=8000,
        )
        return completion

    def random_pause(self, sample_rate, min_duration=0.5, max_duration=2.0):
        silence_duration = random.uniform(min_duration, max_duration)
        silence = np.zeros(int(silence_duration * sample_rate))
        return silence
    
    def generate(self, topic: str):
        kokoro = Kokoro("kokoro-v0_19.onnx", "voices.json")
        audio = []
        completion = self.client(topic)
        sentences = json.loads(completion.choices[0].message.content)

        with tqdm(total=len(sentences), desc="Generating Audio", unit="sentence") as pbar:
            for sentence in sentences:
                voice = sentence["voice"]
                text = sentence["text"]
                
                samples, sample_rate = kokoro.create(
                    text,
                    voice=voice,
                    speed=1.0,
                    lang="en-us",
                )
                audio.append(samples)
                audio.append(self.random_pause(sample_rate))
                
                pbar.update(1)

        audio = np.concatenate(audio)
        sf.write("podcast.wav", audio, sample_rate)
        return "The podcast has been created successfully"