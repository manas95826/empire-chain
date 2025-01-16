import streamlit as st
from empire_chain.llms import OpenAILLM
from dotenv import load_dotenv

load_dotenv()

class Chatbot:
    def __init__(self, llm: OpenAILLM, title: str, chat_history: bool = True):
        self.llm = llm
        self.title = title
        
        if 'messages' not in st.session_state:
            st.session_state.messages = []
        
        # Initialize sidebar content
        if 'sidebar_state' not in st.session_state:
            st.session_state.sidebar_state = 'expanded'

    def display_example_queries(self):
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
        self.display_sidebar()
        
        # Main chat container
        with st.container():
            st.title(self.title)
            
            # Add description
            st.markdown("""
            Welcome to the Empire Chain Demo! This chatbot showcases the capabilities 
            of our AI orchestration framework. Feel free to ask questions about anything!
            """)
            
            st.divider()
            st.subheader("Example Queries")
            self.display_example_queries()
            
            # Chat messages
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
            # Format conversation history
            conversation_history = ""
            for message in st.session_state.messages:
                conversation_history += f"{message['role']}: {message['content']}\n"
            
            # Combine history with new prompt
            full_prompt = f"Previous conversation history:\n{conversation_history}\nNew query: {prompt}"

            with st.chat_message("user"):
                st.markdown(prompt)
                st.session_state.messages.append({"role": "user", "content": prompt})

            # Create a persistent container for the assistant's response
            response_container = st.chat_message("assistant")
            with response_container:
                placeholder = st.empty()
                with placeholder:
                    with st.spinner("Thinking..."):
                        response = self.llm.generate(full_prompt)
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})