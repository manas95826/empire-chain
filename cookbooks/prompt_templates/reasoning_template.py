"""
Examples of using reasoning prompt templates for logical analysis and critical thinking.
Please run: pip install empire-chain
"""
from empire_chain.prompt_templates.templates import (
    LOGICAL_ANALYSIS_TEMPLATE,
    CRITICAL_THINKING_TEMPLATE,
    format_prompt
)

# Example 1: Complex Business Decision
def business_decision_example():
    prompt = format_prompt(
        LOGICAL_ANALYSIS_TEMPLATE,
        problem="Market Expansion Strategy Evaluation",
        context="""
        - Current market share: 25% domestic
        - Available expansion budget: $10M
        - Three potential markets: Asia, Europe, South America
        - Key constraints: regulatory compliance, supply chain capacity
        - Competition analysis available for each region
        """
    )
    return prompt

# Example 2: Policy Impact Analysis
def policy_impact_example():
    prompt = format_prompt(
        CRITICAL_THINKING_TEMPLATE,
        scenario="""
        A proposed urban development policy aims to:
        - Convert 30% of downtown parking to green spaces
        - Implement congestion pricing
        - Expand public transit infrastructure
        - Offer tax incentives for remote work
        """,
        question="What are the potential socioeconomic and environmental impacts over 5-10 years?"
    )
    return prompt

# Example 3: Scientific Hypothesis Evaluation
def scientific_reasoning_example():
    prompt = format_prompt(
        LOGICAL_ANALYSIS_TEMPLATE,
        problem="Evaluate the relationship between sleep patterns and cognitive performance",
        context="""
        - Recent sleep study data from 500 participants
        - Cognitive performance metrics: memory, attention, problem-solving
        - Variables: sleep duration, quality, consistency
        - Confounding factors: age, stress levels, screen time
        """
    )
    return prompt

if __name__ == "__main__":
    # Example usage
    print("=== Business Decision Analysis ===")
    print(business_decision_example())
    
    print("\n=== Policy Impact Analysis ===")
    print(policy_impact_example())
    
    print("\n=== Scientific Reasoning ===")
    print(scientific_reasoning_example()) 