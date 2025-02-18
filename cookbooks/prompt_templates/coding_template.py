"""
Examples of using coding prompt templates for code review and architecture design.
Please run: pip install empire-chain
"""
from empire_chain.prompt_templates.templates import (
    CODE_REVIEW_TEMPLATE,
    ARCHITECTURE_DESIGN_TEMPLATE,
    format_prompt
)

# Example 1: Python Code Review
def python_review_example():
    prompt = format_prompt(
        CODE_REVIEW_TEMPLATE,
        language="Python",
        context="Data Processing Pipeline",
        code="""
        def process_data(data_frame):
            # Clean data
            df_cleaned = data_frame.dropna()
            
            # Transform columns
            df_cleaned['date'] = pd.to_datetime(df_cleaned['date'])
            df_cleaned['value'] = df_cleaned['value'].astype(float)
            
            # Aggregate results
            results = df_cleaned.groupby('category').agg({
                'value': ['mean', 'sum', 'count']
            })
            
            return results
        """
    )
    return prompt

# Example 2: System Architecture
def architecture_example():
    prompt = format_prompt(
        ARCHITECTURE_DESIGN_TEMPLATE,
        project_type="E-commerce Platform",
        requirements="""
        - High availability (99.9% uptime)
        - Scalable to 1M users
        - Real-time inventory management
        - Secure payment processing
        - Order tracking system
        """,
        constraints="""
        - Budget: $100k initial setup
        - Timeline: 6 months to MVP
        - Team: 5 developers
        - Technology: Cloud-native
        """
    )
    return prompt

# Example 3: API Design Review
def api_design_example():
    prompt = format_prompt(
        CODE_REVIEW_TEMPLATE,
        language="REST API",
        context="User Management Service",
        code="""
        Endpoints:
        POST /api/v1/users
        - Create new user
        - Required fields: username, email, password
        
        GET /api/v1/users/{id}
        - Retrieve user details
        - Returns: user profile data
        
        PUT /api/v1/users/{id}
        - Update user information
        - Supports partial updates
        
        DELETE /api/v1/users/{id}
        - Deactivate user account
        - Soft delete implementation
        """
    )
    return prompt

if __name__ == "__main__":
    # Example usage
    print("=== Python Code Review ===")
    print(python_review_example())
    
    print("\n=== System Architecture Design ===")
    print(architecture_example())
    
    print("\n=== API Design Review ===")
    print(api_design_example()) 