"""
Examples of using education prompt templates for lesson planning and concept explanation.
Please run: pip install empire-chain
"""
from empire_chain.prompt_templates.templates import (
    LESSON_PLAN_TEMPLATE,
    CONCEPT_EXPLANATION_TEMPLATE,
    format_prompt
)

# Example 1: High School Physics Lesson
def physics_lesson_example():
    prompt = format_prompt(
        LESSON_PLAN_TEMPLATE,
        subject="Physics - Newton's Laws of Motion",
        grade_level="10th Grade",
        duration="""
        - Total Time: 90 minutes
        - Introduction: 15 minutes
        - Main Activity: 45 minutes
        - Group Work: 20 minutes
        - Assessment: 10 minutes
        """
    )
    return prompt

# Example 2: Programming Concept Explanation
def programming_concept_example():
    prompt = format_prompt(
        CONCEPT_EXPLANATION_TEMPLATE,
        topic="Object-Oriented Programming: Inheritance",
        level="Intermediate Programming Students",
        prerequisites="""
        - Basic understanding of classes and objects
        - Experience with method creation
        - Familiarity with Python syntax
        - Understanding of variables and data types
        """
    )
    return prompt

# Example 3: Mathematics Problem-Solving
def math_lesson_example():
    prompt = format_prompt(
        LESSON_PLAN_TEMPLATE,
        subject="Algebra - Quadratic Equations",
        grade_level="9th Grade",
        duration="""
        - Class Duration: 60 minutes
        - Concept Review: 15 minutes
        - Guided Practice: 25 minutes
        - Independent Work: 15 minutes
        - Wrap-up/Homework: 5 minutes
        """
    )
    return prompt

if __name__ == "__main__":
    # Example usage
    print("=== Physics Lesson Plan ===")
    print(physics_lesson_example())
    
    print("\n=== Programming Concept Explanation ===")
    print(programming_concept_example())
    
    print("\n=== Mathematics Lesson Plan ===")
    print(math_lesson_example()) 