"""
Examples of using prompt templates for various scenarios.
Please run: pip install empire-chain
"""
from empire_chain.prompt_templates.templates import (
    CODE_GENERATION_TEMPLATE,
    SENTIMENT_ANALYSIS_MAIN_TEMPLATE,
    SENTIMENT_ANALYSIS_EXAMPLE_TEMPLATE,
    PromptTemplate,
    FewShotPromptTemplate
)

# Example 1: Code Generation using PromptTemplate
def code_generation_example():
    template = PromptTemplate(CODE_GENERATION_TEMPLATE)
    prompt = template.format(
        language="Python",
        task="validates email addresses using regex",
        function_name="validate_email",
        parameters="email: str"
    )
    return prompt

# Example 2: Sentiment Analysis using FewShotPromptTemplate
def sentiment_analysis_example():
    examples = [
        {"text": "I love this product!", "sentiment": "Positive"},
        {"text": "Terrible service, very disappointed.", "sentiment": "Negative"},
        {"text": "It's okay, nothing special.", "sentiment": "Neutral"}
    ]
    
    few_shot = FewShotPromptTemplate(
        SENTIMENT_ANALYSIS_MAIN_TEMPLATE,
        SENTIMENT_ANALYSIS_EXAMPLE_TEMPLATE,
        examples
    )
    
    prompt = few_shot.format(query="The interface is confusing but the features are useful.")
    return prompt

if __name__ == "__main__":
    # Example usage
    print("=== Code Generation Template ===")
    print(code_generation_example())
    
    print("\n=== Sentiment Analysis Few-Shot ===")
    print(sentiment_analysis_example())