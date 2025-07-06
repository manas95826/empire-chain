"""
Demonstration of the new PromptTemplate system
"""
import sys
from pathlib import Path

# Add project root to Python path
try:
    project_root = Path(__file__).resolve().parents[2]  # Adjust based on your structure
    sys.path.insert(0, str(project_root))
except Exception as e:
    print(f"Path adjustment failed: {e}")
   
    
from empire_chain.prompt_templates.templates import (
    PromptTemplate,
    FewShotPromptTemplate
)

# 1. Basic Template Example
def basic_template_demo():
    template = PromptTemplate("Translate from {{source_lang}} to {{target_lang}}: {{text}}")
    return template.format(
        source_lang="English",
        target_lang="Spanish",
        text="Hello World"
    )

# 2. Few-Shot Learning Example
def few_shot_demo():
    # Main template with {{examples}} placeholder
    main_template = """
    Examples of translations:
    {{examples}}
    
    Now translate this:
    {{query}}
    """
    
    # Example template for each demonstration
    example_template = "{{english}} => {{spanish}}"
    
    # Example data
    examples = [
        {"english": "Good morning", "spanish": "Buenos días"},
        {"english": "How are you?", "spanish": "¿Cómo estás?"}
    ]
    
    # Create few-shot template
    few_shot = FewShotPromptTemplate(
        main_template,
        example_template,
        examples
    )
    
    return few_shot.format(query="I love programming")

if __name__ == "__main__":
    print("=== BASIC TEMPLATE ===")
    print(basic_template_demo())
    
    print("\n=== FEW-SHOT TEMPLATE ===")
    print(few_shot_demo())