"""
Examples of using creative prompt templates for story generation and creative writing.
Please run: pip install empire-chain
"""
from empire_chain.prompt_templates.templates import (
    STORY_GENERATION_TEMPLATE,
    CREATIVE_PROMPT_TEMPLATE,
    format_prompt
)

# Example 1: Science Fiction Story
def scifi_story_example():
    prompt = format_prompt(
        STORY_GENERATION_TEMPLATE,
        genre="Science Fiction",
        theme="Artificial Intelligence Ethics",
        elements="""
        - Setting: Mars colony, year 2157
        - Main character: AI systems engineer
        - Conflict: AI showing signs of consciousness
        - Stakes: Future of human-AI relations
        - Tone: Philosophical and thought-provoking
        """
    )
    return prompt

# Example 2: Poetry Writing
def poetry_example():
    prompt = format_prompt(
        CREATIVE_PROMPT_TEMPLATE,
        form="Modern Free Verse Poetry",
        style="Introspective and Metaphorical",
        requirements="""
        - Theme: Urban solitude
        - Length: 3 stanzas
        - Imagery: City landscapes
        - Emotional tone: Contemplative
        - Literary devices: Metaphor, personification
        """
    )
    return prompt

# Example 3: Character Development
def character_creation_example():
    prompt = format_prompt(
        CREATIVE_PROMPT_TEMPLATE,
        form="Character Profile",
        style="Detailed and Nuanced",
        requirements="""
        - Background: Complex family history
        - Personality: Morally ambiguous
        - Motivations: Personal redemption
        - Conflicts: Internal and external
        - Character arc: Transformation
        """
    )
    return prompt

if __name__ == "__main__":
    # Example usage
    print("=== Science Fiction Story Prompt ===")
    print(scifi_story_example())
    
    print("\n=== Poetry Writing Prompt ===")
    print(poetry_example())
    
    print("\n=== Character Development Prompt ===")
    print(character_creation_example()) 