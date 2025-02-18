from typing import List, Optional

# Medical Templates
MEDICAL_ANALYSIS_TEMPLATE = """
Patient Information:
{patient_info}

Symptoms: {symptoms}
Medical History: {medical_history}

Please provide:
1. Potential diagnoses to consider
2. Recommended tests or examinations
3. Treatment considerations
4. Important precautions or warnings

Note: This is for educational purposes only and should not replace professional medical advice."""

MEDICAL_RESEARCH_TEMPLATE = """
Research Topic: {topic}
Current Knowledge: {background}

Please analyze the latest research and evidence regarding this medical topic, including:
1. Key findings from recent studies
2. Clinical implications
3. Areas of consensus and controversy
4. Future research directions"""

# Reasoning Templates
LOGICAL_ANALYSIS_TEMPLATE = """
Problem Statement: {problem}
Given Information: {context}

Please provide:
1. Step-by-step logical analysis
2. Key assumptions identified
3. Potential alternative perspectives
4. Conclusion based on available evidence"""

CRITICAL_THINKING_TEMPLATE = """
Scenario: {scenario}
Question: {question}

Please analyze using:
1. Fact vs opinion differentiation
2. Evidence evaluation
3. Logical fallacy identification
4. Structured argumentation"""

# Financial Templates
FINANCIAL_ANALYSIS_TEMPLATE = """
Financial Data:
{financial_data}

Analysis Request: {analysis_type}

Please provide:
1. Key financial metrics and ratios
2. Trend analysis
3. Risk assessment
4. Recommendations
5. Important disclaimers"""

INVESTMENT_TEMPLATE = """
Investment Vehicle: {investment_type}
Market Context: {market_conditions}
Risk Profile: {risk_tolerance}

Please analyze:
1. Potential returns and risks
2. Market factors to consider
3. Strategic considerations
4. Important warnings and disclaimers"""

# Educational Templates
LESSON_PLAN_TEMPLATE = """
Subject: {subject}
Grade Level: {grade_level}
Duration: {duration}

Please create a lesson plan including:
1. Learning objectives
2. Required materials
3. Introduction/hook
4. Main activities
5. Assessment methods
6. Extensions/modifications"""

CONCEPT_EXPLANATION_TEMPLATE = """
Topic: {topic}
Student Level: {level}
Prior Knowledge: {prerequisites}

Please provide:
1. Clear explanation using appropriate language
2. Relevant examples and analogies
3. Common misconceptions
4. Practice problems or applications"""

# Creative Writing Templates
STORY_GENERATION_TEMPLATE = """
Genre: {genre}
Theme: {theme}
Key Elements: {elements}

Please create:
1. Engaging plot outline
2. Character descriptions
3. Setting details
4. Key story beats
5. Thematic elements"""

CREATIVE_PROMPT_TEMPLATE = """
Creative Form: {form}
Style: {style}
Requirements: {requirements}

Please generate creative content that:
1. Matches the specified form and style
2. Incorporates required elements
3. Maintains originality and engagement"""

# Blog Writing Templates
BLOG_POST_TEMPLATE = """
Topic: {topic}
Target Audience: {audience}
Purpose: {purpose}

Please create a blog post structure with:
1. Attention-grabbing headline
2. Engaging introduction
3. Main content points
4. Call to action
5. SEO considerations"""

CONTENT_STRATEGY_TEMPLATE = """
Blog Focus: {focus}
Target Demographics: {demographics}
Goals: {goals}

Please provide:
1. Content pillars
2. Topic clusters
3. Content calendar suggestions
4. Engagement strategies"""

# Coding Templates
CODE_REVIEW_TEMPLATE = """
Language: {language}
Code Context: {context}
Code Block:
{code}

Please review for:
1. Code quality and best practices
2. Potential bugs or issues
3. Performance considerations
4. Security concerns
5. Suggested improvements"""

ARCHITECTURE_DESIGN_TEMPLATE = """
Project Type: {project_type}
Requirements: {requirements}
Constraints: {constraints}

Please provide:
1. System architecture overview
2. Component relationships
3. Technical considerations
4. Implementation guidelines
5. Potential challenges"""

class MedicalAnalysis:
    patient_info: str
    symptoms: str
    medical_history: str
    
    def __str__(self):
        return format_prompt(MEDICAL_ANALYSIS_TEMPLATE, 
                           patient_info=self.patient_info,
                           symptoms=self.symptoms,
                           medical_history=self.medical_history)

class MedicalResearch:
    topic: str
    background: str
    
    def __str__(self):
        return format_prompt(MEDICAL_RESEARCH_TEMPLATE,
                           topic=self.topic,
                           background=self.background)

class LogicalAnalysis:
    problem: str
    context: str
    
    def __str__(self):
        return format_prompt(LOGICAL_ANALYSIS_TEMPLATE,
                           problem=self.problem,
                           context=self.context)

class CriticalThinking:
    scenario: str
    question: str
    
    def __str__(self):
        return format_prompt(CRITICAL_THINKING_TEMPLATE,
                           scenario=self.scenario,
                           question=self.question)

class FinancialAnalysis:
    financial_data: str
    analysis_type: str
    
    def __str__(self):
        return format_prompt(FINANCIAL_ANALYSIS_TEMPLATE,
                           financial_data=self.financial_data,
                           analysis_type=self.analysis_type)

class CodeReview:
    language: str
    context: str
    code: str
    
    def __str__(self):
        return format_prompt(CODE_REVIEW_TEMPLATE,
                           language=self.language,
                           context=self.context,
                           code=self.code)

# Add list of available templates
available_templates = [
    MedicalAnalysis,
    MedicalResearch,
    LogicalAnalysis,
    CriticalThinking,
    FinancialAnalysis,
    CodeReview
]

def format_prompt(template: str, **kwargs) -> str:
    """
    Format a prompt template with the provided arguments.
    
    Args:
        template: The prompt template to format
        **kwargs: Keyword arguments to fill in the template
        
    Returns:
        str: The formatted prompt
    """
    try:
        return template.format(**kwargs)
    except KeyError as e:
        raise ValueError(f"Missing required argument: {e}")

def combine_prompts(prompts: List[str], separator: str = "\n\n") -> str:
    """
    Combine multiple prompts into a single prompt string.
    
    Args:
        prompts: List of prompts to combine
        separator: String to use between prompts (default: double newline)
        
    Returns:
        str: Combined prompt string
    """
    return separator.join(prompt.strip() for prompt in prompts if prompt.strip())
