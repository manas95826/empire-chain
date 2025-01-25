import streamlit as st
from empire_chain.llms.llms import OpenAILLM
from dotenv import load_dotenv

load_dotenv()

class Chatbot:
    def __init__(self, llm: OpenAILLM, title: str, chat_history: bool = True, custom_instructions: str = "", verbose: bool = True):
        self.llm = llm
        self.title = title
        self.chat_history = chat_history
        self.custom_instructions = custom_instructions
        self.verbose = verbose
        
        if 'messages' not in st.session_state:
            st.session_state.messages = []
        
        if 'sidebar_state' not in st.session_state:
            st.session_state.sidebar_state = 'expanded'

    def display_example_queries(self):
        with st.expander("Example Queries"):
            example_queries = {
                "example1": "Who is the CEO of Tesla?",
                "example2": "What are llms?",
                "example3": "How to write a research paper?",
                "example4": "How to set up a company in Delaware?"
            }
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Who is the CEO of Tesla?", key="example1"):
                    st.session_state.example_query = example_queries["example1"]
                if st.button("What are llms?", key="example2"):
                    st.session_state.example_query = example_queries["example2"]
            with col2:
                if st.button("How to write a research paper?", key="example3"):
                    st.session_state.example_query = example_queries["example3"]
                if st.button("How to set up a company in Delaware?", key="example4"):
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
                Welcome to the Empire Chain Demo! This chatbot showcases the capabilities 
                of our AI orchestration framework. Feel free to ask questions about anything!
                """)
            
            st.subheader("Example Queries")
            self.display_example_queries()
            
            message_container = st.container()
            with message_container:
                for message in st.session_state.messages:
                    role = message["role"]
                    content = message["content"]
                    with st.chat_message(role):
                        st.markdown(content)
        
        prompt = st.chat_input("What would you like to know?")
        
        if "example_query" in st.session_state:
            prompt = st.session_state.pop("example_query")
        
        if prompt:
            with st.chat_message("user"):
                st.markdown(prompt)
                if self.chat_history:
                    st.session_state.messages.append({"role": "user", "content": prompt})

            response_container = st.chat_message("assistant")
            with response_container:
                placeholder = st.empty()
                with placeholder:
                    with st.spinner("Thinking..."):
                        if self.chat_history:
                            conversation_history = f"{self.custom_instructions}\n"
                            for message in st.session_state.messages:
                                conversation_history += f"{message['role']}: {message['content']}\n"
                            full_prompt = f"Previous conversation history:\n{conversation_history}\nNew query: {prompt}"
                            response = self.llm.generate(full_prompt)
                        else:
                            response = self.llm.generate(prompt)
                    st.markdown(response)
                    if self.chat_history:
                        st.session_state.messages.append({"role": "assistant", "content": response}) 