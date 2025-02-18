"""
Examples of using financial prompt templates for analysis and investment guidance.
Please run: pip install empire-chain
"""
from empire_chain.prompt_templates.templates import (
    FINANCIAL_ANALYSIS_TEMPLATE,
    INVESTMENT_TEMPLATE,
    format_prompt
)

# Example 1: Company Financial Health Analysis
def company_analysis_example():
    prompt = format_prompt(
        FINANCIAL_ANALYSIS_TEMPLATE,
        financial_data="""
        - Revenue: $50M (20% YoY growth)
        - Operating Margin: 25%
        - Debt-to-Equity: 0.8
        - Current Ratio: 2.1
        - Cash Flow from Operations: $12M
        - R&D Spending: 15% of revenue
        """,
        analysis_type="Comprehensive Financial Health Assessment"
    )
    return prompt

# Example 2: Investment Portfolio Strategy
def portfolio_strategy_example():
    prompt = format_prompt(
        INVESTMENT_TEMPLATE,
        investment_type="Diversified Portfolio Strategy",
        market_conditions="""
        - High inflation environment (6.5%)
        - Rising interest rates
        - Tech sector volatility
        - Emerging market opportunities
        """,
        risk_tolerance="Moderate - Balanced growth and safety"
    )
    return prompt

# Example 3: Startup Valuation Analysis
def startup_valuation_example():
    prompt = format_prompt(
        FINANCIAL_ANALYSIS_TEMPLATE,
        financial_data="""
        - Pre-money valuation: $15M
        - Monthly burn rate: $200K
        - User growth: 15% MoM
        - Revenue run rate: $2M ARR
        - Market size: $5B TAM
        - Competitor valuations: 10-12x ARR
        """,
        analysis_type="Series A Investment Evaluation"
    )
    return prompt

if __name__ == "__main__":
    # Example usage
    print("=== Company Financial Analysis ===")
    print(company_analysis_example())
    
    print("\n=== Investment Portfolio Strategy ===")
    print(portfolio_strategy_example())
    
    print("\n=== Startup Valuation Analysis ===")
    print(startup_valuation_example()) 