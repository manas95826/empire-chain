from empire_chain.llms.llms import OpenAILLM, AnthropicLLM, GroqLLM, GeminiLLM
import streamlit as st
from empire_chain.prompt_templates import templates
import time
from dataclasses import dataclass

class LLMPlayground:
    def __init__(self):
        self.llms = {
            "OpenAI": OpenAILLM(),
            "Anthropic": AnthropicLLM(),
            "Groq": GroqLLM(),
            "Gemini": GeminiLLM()
        }

    def launch(self):
        st.set_page_config(layout="wide")
        st.title("🤖 LLM Battle Arena")
        
        # Add CSS for the battle animation modal and overlay
        st.markdown("""
            <style>
            .battle-overlay {
                position: fixed;
                top: 0;
                left: 0;
                width: 100vw;
                height: 100vh;
                background: rgba(0, 0, 0, 0.7);
                backdrop-filter: blur(5px);
                z-index: 1000;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            .battle-animation {
                text-align: center;
                font-size: 3em;
                padding: 3rem;
                background: white;
                border-radius: 1rem;
                box-shadow: 0 0 20px rgba(0,0,0,0.3);
                animation: scale-in 0.3s ease-out;
            }
            @keyframes scale-in {
                from {
                    transform: scale(0.8);
                    opacity: 0;
                }
                to {
                    transform: scale(1);
                    opacity: 1;
                }
            }
            </style>
        """, unsafe_allow_html=True)
        
        # Create a placeholder for the battle animation with custom CSS
        st.markdown("""
            <style>
            .battle-animation {
                text-align: center;
                font-size: 2.5em;
                padding: 2rem;
                background: rgba(0,0,0,0.05);
                border-radius: 1rem;
                margin: 2rem 0;
            }
            </style>
        """, unsafe_allow_html=True)
        battle_animation_placeholder = st.empty()
        
        # Step 1: LLM Selection and API Keys
        st.header("1. Select Two LLMs to Compare")
        
        # Create two columns for LLM selection
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("First LLM")
            llm1 = st.selectbox(
                "Select LLM",
                options=list(self.llms.keys()),
                key="llm1"
            )
            api_key1 = st.text_input(
                "API Key",
                type="password",
                help=f"Enter your {llm1} API key",
                key="api_key1"
            )
        
        with col2:
            st.subheader("Second LLM")
            remaining_llms = [llm for llm in self.llms.keys() if llm != llm1]
            llm2 = st.selectbox(
                "Select LLM",
                options=remaining_llms,
                key="llm2"
            )
            api_key2 = st.text_input(
                "API Key",
                type="password",
                help=f"Enter your {llm2} API key",
                key="api_key2"
            )
        
        selected_llms = [(llm1, api_key1), (llm2, api_key2)]
            
        # Step 2: Template Selection
        st.header("2. Select Task")
        template_names = [template.__name__ for template in templates.available_templates]
        selected_template = st.selectbox(
            "Choose the task template",
            options=template_names
        )
        
        # Step 3: Input Parameters
        if selected_template:
            st.header("3. Fill Task Parameters")
            template_class = getattr(templates, selected_template)
            
            # Get the required parameters from class annotations
            template_params = {}
            
            if hasattr(template_class, '__annotations__'):
                for param_name, param_type in template_class.__annotations__.items():
                    template_params[param_name] = st.text_area(
                        f"{param_name} ({param_type.__name__})",
                        "",
                        help=f"Enter {param_name}"
                    )
            
            if st.button("⚔️ Battle!", type="primary"):
                try:
                    # Validate API keys
                    for llm_name, api_key in selected_llms:
                        if not api_key:
                            st.error(f"❌ Please provide an API key for {llm_name}")
                            return

                    # Create template instance
                    template = template_class()
                    for param_name, value in template_params.items():
                        setattr(template, param_name, value)
                    
                    prompt = str(template)
                    
                    # Display the generated prompt in an expander
                    with st.expander("🔍 Show generated prompt"):
                        st.code(prompt, language="text")
                    
                    # Create battle animation container at the bottom
                    battle_container = st.container()
                    
                    # Show battle animation
                    self.show_battle_animation(battle_container, selected_llms[0][0], selected_llms[1][0])
                    
                    # Create two columns for results
                    col1, col2 = st.columns(2)
                    
                    for col, (llm_name, api_key) in zip([col1, col2], selected_llms):
                        with col:
                            st.subheader(f"🤖 {llm_name}")
                            try:
                                # Initialize LLM with API key
                                llm_instance = self.llms[llm_name].__class__(api_key=api_key)
                                
                                start_time = time.time()
                                response = llm_instance.generate(prompt)
                                end_time = time.time()
                                
                                execution_time = end_time - start_time
                                st.success(f"⏱️ Time taken: {execution_time:.2f} seconds")
                                
                                st.code(response, language="text")
                            except Exception as e:
                                st.error(f"❌ Error with {llm_name}: {str(e)}")
                                
                except Exception as e:
                    st.error(f"❌ Error creating template: {str(e)}")
                    st.error(f"Template parameters: {template_params}")

    def show_battle_animation(self, container, llm1_name, llm2_name):
        placeholder = container.empty()
        
        frames = [
            f"""
            <div class="battle-overlay">
                <div class="battle-animation">
                    <div style="font-size: 0.6em; color: #ff4b4b;">🔥 {llm1_name} vs {llm2_name} 🔥</div>
                    <div style="margin: 1.5rem; color: #333;">
                        🤖  &nbsp;&nbsp; FIGHT! &nbsp;&nbsp;  🤖
                    </div>
                    <div style="font-size: 0.8em">⚔️  &nbsp;&nbsp;&nbsp;&nbsp;  ⚔️</div>
                </div>
            </div>
            """,
            f"""
            <div class="battle-overlay">
                <div class="battle-animation">
                    <div style="font-size: 0.6em; color: #ff4b4b;">🔥 {llm1_name} vs {llm2_name} 🔥</div>
                    <div style="margin: 1.5rem; color: #333;">
                        🤖  &nbsp; ⚡CLASH!⚡ &nbsp;  🤖
                    </div>
                    <div style="font-size: 0.8em">⚔️ &nbsp; ⚡ &nbsp; ⚔️</div>
                </div>
            </div>
            """,
            f"""
            <div class="battle-overlay">
                <div class="battle-animation">
                    <div style="font-size: 0.6em; color: #ff4b4b;">🔥 {llm1_name} vs {llm2_name} 🔥</div>
                    <div style="margin: 1.5rem; color: #333;">
                        🤖  &nbsp;&nbsp; BANG! &nbsp;&nbsp;  🤖
                    </div>
                    <div style="font-size: 0.8em">💥 &nbsp;&nbsp;&nbsp;&nbsp; 💥</div>
                </div>
            </div>
            """,
            f"""
            <div class="battle-overlay">
                <div class="battle-animation">
                    <div style="font-size: 0.6em; color: #ff4b4b;">🔥 {llm1_name} vs {llm2_name} 🔥</div>
                    <div style="margin: 1.5rem; color: #333;">
                        🤖  &nbsp; POW! POW! &nbsp;  🤖
                    </div>
                    <div style="font-size: 0.8em">💫 &nbsp;&nbsp; ⚡ &nbsp;&nbsp; 💫</div>
                </div>
            </div>
            """
        ]
        
        # Display each frame for a short duration
        for frame in frames:
            placeholder.markdown(frame, unsafe_allow_html=True)
            time.sleep(0.5)  # Slightly longer duration for better effect
        
        # Clear the animation placeholder
        placeholder.empty()

def launch_playground():
    playground = LLMPlayground()
    playground.launch()

if __name__ == "__main__":
    launch_playground()





