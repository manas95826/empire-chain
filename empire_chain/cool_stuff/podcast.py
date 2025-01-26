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
                    "content": """You are a podcast scriptwriter for an engaging multi-host podcast show. Create a natural, flowing conversation between 2-3 hosts discussing the given topic. Follow these guidelines:

1. Structure:
   - Start with a warm welcome and topic introduction
   - Have a structured discussion with clear segments
   - End with a conclusion and sign-off

2. Host Personalities (use these consistently):
   - af_sarah: The main host/moderator who guides the conversation
   - am_michael: The expert/analyst who provides deep insights
   - af_bella: The engaging co-host who asks good questions (optional)

3. Make the conversation natural by:
   - Including casual reactions ("That's fascinating!", "I agree", etc.)
   - Having hosts build on each other's points
   - Including brief personal anecdotes
   - Using conversational language, not formal speech

4. Keep each speaking turn relatively brief (1-3 sentences) to maintain flow.

Available voices: af, af_bella, af_sarah, af_sky, am_adam, am_michael, bf_emma, bf_isabella, bm_george, bm_lewis

Return only a JSON array of conversation turns, like:
[
    {
        "voice": "af_sarah",
        "text": "Welcome to The Deep Dive! Today we're exploring [topic], and I'm thrilled to discuss this with our experts."
    },
    {
        "voice": "am_michael",
        "text": "Thanks Sarah! This is such an interesting topic, and I've actually been researching it recently."
    },
    ...
]"""
                },
                {
                    "role": "user",
                    "content": f"My topic is '{topic}'."
                }
            ],
            temperature=0.5,
            max_completion_tokens=8000,
        )
        return completion

    def random_pause(self, sample_rate, min_duration=0.5, max_duration=2.0):
        silence_duration = random.uniform(min_duration, max_duration)
        silence = np.zeros(int(silence_duration * sample_rate))
        return silence
    
    def _clean_json_response(self, response: str) -> str:
        """Clean and validate JSON response"""
        response = response.strip()
        
        # Try to extract content between square brackets
        try:
            start_idx = response.index('[')
            end_idx = response.rindex(']') + 1
            response = response[start_idx:end_idx]
        except ValueError:
            raise ValueError(f"Could not find JSON array in response: {response[:100]}...")
        
        try:
            parsed = json.loads(response)
            return json.dumps(parsed, separators=(',', ':'))
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON response: {response[:100]}...")

    def generate(self, topic: str):
        self.download_required_files()  # Download required files first
        kokoro = Kokoro("kokoro-v0_19.onnx", "voices.json")
        audio = []
        completion = self.client(topic)
        response_content = completion.choices[0].message.content
        cleaned_json = self._clean_json_response(response_content)
        sentences = json.loads(cleaned_json)

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