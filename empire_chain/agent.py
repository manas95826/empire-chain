from typing import Any, Callable, Dict, List
import json
from datetime import datetime
import requests
from empire_chain.llms import GroqLLM

class FunctionRegistry:
    def __init__(self):
        self.functions: Dict[str, Callable] = {}
        self.descriptions: Dict[str, Dict[str, Any]] = {}
    
    def register(self, name: str, func: Callable, description: str, parameters: List[str]):
        """Register a function with its metadata"""
        self.functions[name] = func
        self.descriptions[name] = {
            "name": name,
            "description": description,
            "parameters": parameters
        }
    
    def list_functions(self) -> List[str]:
        """List all registered function names"""
        return list(self.functions.keys())

class Agent:
    def __init__(self, model: str = "mixtral-8x7b-32768"):  
        self.llm = GroqLLM(model=model)
        self.registry = FunctionRegistry()
        
    def register_function(self, name: str, func: Callable, description: str, parameters: List[str]):
        """Register a function that the agent can call"""
        self.registry.register(name, func, description, parameters)
    
    def _create_function_prompt(self, query: str) -> str:
        functions_json = json.dumps(self.registry.descriptions, indent=2)
        return f"""You are a function router that maps user queries to the most appropriate function. Your response must be a valid JSON object.

User Query: {query}

Available Functions:
{functions_json}

Instructions:
1. Analyze the user query
2. Select the most appropriate function from the available functions
3. Extract parameter values from the query
4. Return a JSON object in EXACTLY this format, with NO ADDITIONAL WHITESPACE or FORMATTING:
{{"function":"<function_name>","parameters":{{"<param_name>":"<param_value>"}},"reasoning":"<one_line_explanation>"}}

Critical Rules:
- Response must be a SINGLE LINE of valid JSON
- NO line breaks, NO extra spaces
- NO markdown formatting or code blocks
- ALL strings must use double quotes
- Function name must be from available functions
- ALL required parameters must be included
- Reasoning must be brief and single-line

Example Valid Response:
{{"function":"get_weather","parameters":{{"location":"New York"}},"reasoning":"Query asks about weather in a specific location"}}

Response (SINGLE LINE JSON):"""

    def _clean_json_response(self, response: str) -> str:
        """Clean and validate JSON response"""
        # Remove any markdown formatting
        response = response.strip()
        if "```" in response:
            response = response.split("```")[1]
            if response.startswith("json"):
                response = response[4:]
        response = response.strip()
        
        # Remove any line breaks and normalize whitespace
        response = " ".join(response.split())
        
        # Attempt to parse and re-serialize to ensure valid JSON
        try:
            parsed = json.loads(response)
            return json.dumps(parsed, separators=(',', ':'))
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON response: {response[:100]}...")
    
    def process_query(self, query: str) -> Any:
        """Process a natural language query and route it to appropriate function"""
        if not self.registry.functions:
            raise ValueError("No functions registered with the agent")
            
        # Get function and parameters from LLM
        prompt = self._create_function_prompt(query)
        response = self.llm.generate(prompt)
        
        try:
            # Clean and validate JSON response
            cleaned_response = self._clean_json_response(response)
            result = json.loads(cleaned_response)
            
            func_name = result["function"]
            parameters = result["parameters"]
            reasoning = result.get("reasoning", "No reasoning provided")
            
            if func_name not in self.registry.functions:
                raise ValueError(f"Function {func_name} not found. Available functions: {', '.join(self.registry.list_functions())}")
                
            # Call the function with extracted parameters
            func = self.registry.functions[func_name]
            return {
                "result": func(**parameters),
                "function_called": func_name,
                "parameters_used": parameters,
                "reasoning": reasoning
            }
            
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse LLM response as JSON. Response: {response[:100]}... Error: {str(e)}")
        except KeyError as e:
            raise ValueError(f"Missing required field in LLM response: {e}")
        except Exception as e:
            raise ValueError(f"Error processing query: {str(e)}") 