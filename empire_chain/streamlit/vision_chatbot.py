import streamlit as st
from groq import Groq
import base64
from io import BytesIO
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

class VisionChatbot:
    def __init__(self, title: str, chat_history: bool = True, custom_instructions: str = "", verbose: bool = True):
        self.title = title
        self.groq_client = Groq()
        self.chat_history = chat_history
        self.custom_instructions = custom_instructions
        self.verbose = verbose
        
        if 'messages' not in st.session_state:
            st.session_state.messages = []
        
        if 'sidebar_state' not in st.session_state:
            st.session_state.sidebar_state = 'expanded'

    def convert_image_to_base64(self, image):
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        return f"data:image/png;base64,{img_str}"

    def process_image_query(self, image, query):
        image_data_url = self.convert_image_to_base64(image)
        
        completion = self.groq_client.chat.completions.create(
            model="llama-3.2-11b-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"{self.custom_instructions}\n\n{query}"
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": image_data_url
                            }
                        }
                    ]
                }
            ],
            temperature=1,
            max_completion_tokens=1024,
            top_p=1,
            stream=False,
            stop=None,
        )
        
        return completion.choices[0].message.content

    def display_example_queries(self):
        with st.expander("Example Queries"):
            example_queries = {
                "example1": "Who is the person in the image?",
                "example2": "What is the name of the person written in the image?",
                "example3": "How many people are in the image?",
                "example4": "What is the color of the shirt the person is wearing?"
            }
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Who is the person in the image?", key="example1"):
                    st.session_state.example_query = example_queries["example1"]
                if st.button("What is the name of the person written in the image?", key="example2"):
                    st.session_state.example_query = example_queries["example2"]
            with col2:
                if st.button("How many people are in the image?", key="example3"):
                    st.session_state.example_query = example_queries["example3"]
                if st.button("What is the color of the shirt the person is wearing?", key="example4"):
                    st.session_state.example_query = example_queries["example4"]

    def display_sidebar(self):
        with st.sidebar:
            st.title("Empire Chain 🚀")
            st.markdown("### AI Orchestration Framework")
            
            st.markdown("#### Key Features")
            st.markdown("""
            - 🤖 Seamless LLM Integration
              - Groq
              - OpenAI
              - Anthropic
            
            - 📚 Embedding Support
              - Sentence Transformers
              - OpenAI Embeddings
            
            - 🗄️ Vector Stores
              - Qdrant
              - ChromaDB
            
            - 🤝 Custom Agents
              - Web Agent (DuckDuckGo)
              - Finance Agent (YFinance)
            """)
            
            st.markdown("#### Quick Links")
            st.markdown("[GitHub Repository](https://lnkd.in/gbiiCVtk)")
            st.markdown("[PyPI Package](https://lnkd.in/gfhc4YeE)")
            
            st.markdown("---")
            st.markdown("*Make your RAG solution in just 30 lines of code!*")

    def chat(self):
        if self.verbose:
            self.display_sidebar()
        
        with st.container():
            st.title(self.title)
            
            if self.verbose:
                st.markdown("""
                Welcome to the Empire Chain Vision Demo! This chatbot can analyze images and answer questions about them.
                Upload an image and ask questions about it!
                """)
            
            st.subheader("Example Queries")
            self.display_example_queries()
            
            uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
            if uploaded_file is not None:
                image = Image.open(uploaded_file)
                st.image(image, caption="Uploaded Image", width=150)
            
            message_container = st.container()
            with message_container:
                for message in st.session_state.messages:
                    role = message["role"]
                    content = message["content"]
                    with st.chat_message(role):
                        st.markdown(content)
        
        prompt = st.chat_input("Ask a question about the image...")
        
        if "example_query" in st.session_state:
            prompt = st.session_state.pop("example_query")
        
        if prompt and uploaded_file is not None:
            with st.chat_message("user"):
                st.markdown(prompt)
                st.session_state.messages.append({"role": "user", "content": prompt})

            response_container = st.chat_message("assistant")
            with response_container:
                placeholder = st.empty()
                with placeholder:
                    with st.spinner("Analyzing image..."):
                        response = self.process_image_query(image, prompt)
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
        elif prompt and uploaded_file is None:
            st.warning("Please upload an image first!") 