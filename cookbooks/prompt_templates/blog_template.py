"""
Examples of using blog writing prompt templates for content creation and strategy.
Please run: pip install empire-chain
"""
from empire_chain.prompt_templates.templates import (
    BLOG_POST_TEMPLATE,
    CONTENT_STRATEGY_TEMPLATE,
    format_prompt
)

# Example 1: Tech Blog Post
def tech_blog_example():
    prompt = format_prompt(
        BLOG_POST_TEMPLATE,
        topic="Introduction to Machine Learning",
        audience="Tech-curious professionals",
        purpose="""
        - Educate beginners about ML basics
        - Demystify technical concepts
        - Encourage further learning
        - Build authority in AI/ML space
        """
    )
    return prompt

# Example 2: Content Strategy
def content_strategy_example():
    prompt = format_prompt(
        CONTENT_STRATEGY_TEMPLATE,
        focus="Sustainable Living Blog",
        demographics="""
        - Primary: 25-40 year old urban professionals
        - Interest in eco-friendly lifestyle
        - Value practical solutions
        - Engaged in social media
        """,
        goals="""
        - Increase organic traffic by 50%
        - Build email list to 10k subscribers
        - Establish brand partnerships
        - Create community engagement
        """
    )
    return prompt

# Example 3: Lifestyle Blog Post
def lifestyle_blog_example():
    prompt = format_prompt(
        BLOG_POST_TEMPLATE,
        topic="Mindful Morning Routines",
        audience="Busy professionals seeking work-life balance",
        purpose="""
        - Share actionable morning routine tips
        - Address common time management challenges
        - Incorporate mindfulness practices
        - Promote sustainable lifestyle changes
        """
    )
    return prompt

if __name__ == "__main__":
    # Example usage
    print("=== Tech Blog Post ===")
    print(tech_blog_example())
    
    print("\n=== Content Strategy ===")
    print(content_strategy_example())
    
    print("\n=== Lifestyle Blog Post ===")
    print(lifestyle_blog_example()) 