"""
Examples of using medical prompt templates for various healthcare scenarios.
Please run: pip install empire-chain
"""
from empire_chain.prompt_templates.templates import (
    MEDICAL_ANALYSIS_TEMPLATE, 
    MEDICAL_RESEARCH_TEMPLATE, 
    format_prompt
)

# Example 1: Patient Case Analysis
def patient_case_example():
    prompt = format_prompt(
        MEDICAL_ANALYSIS_TEMPLATE,
        patient_info="42-year-old female, non-smoker, active lifestyle",
        symptoms="""
        - Persistent cough for 3 weeks
        - Low-grade fever (99.5°F)
        - Fatigue and reduced exercise tolerance
        """,
        medical_history="""
        - Controlled asthma
        - No other chronic conditions
        - Up-to-date vaccinations
        """
    )
    return prompt

# Example 2: Medical Research Review
def research_review_example():
    prompt = format_prompt(
        MEDICAL_RESEARCH_TEMPLATE,
        topic="Emerging Treatments in Type 2 Diabetes",
        background="""
        Current standard treatments include:
        - Metformin as first-line therapy
        - GLP-1 receptor agonists
        - SGLT2 inhibitors
        Need to evaluate new therapeutic approaches and their efficacy.
        """
    )
    return prompt

# Example 3: Clinical Guidelines Analysis
def clinical_guidelines_example():
    prompt = format_prompt(
        MEDICAL_ANALYSIS_TEMPLATE,
        patient_info="Clinical Protocol Development",
        symptoms="Acute Coronary Syndrome Management",
        medical_history="""
        Review current protocols for:
        - Initial assessment
        - Risk stratification
        - Treatment pathways
        - Follow-up care
        """
    )
    return prompt

if __name__ == "__main__":
    # Example usage
    print("=== Patient Case Analysis ===")
    print(patient_case_example())
    
    print("\n=== Medical Research Review ===")
    print(research_review_example())
    
    print("\n=== Clinical Guidelines Analysis ===")
    print(clinical_guidelines_example()) 