from typing import Any, Callable, Dict, List, get_type_hints
import json
from datetime import datetime
import inspect
import requests
from empire_chain.llms.llms import GroqLLM

class FunctionRegistry:
    def __init__(self):
        self.functions: Dict[str, Callable] = {}
        self.descriptions: Dict[str, Dict[str, Any]] = {}
    
    def _extract_function_metadata(self, func: Callable) -> Dict[str, Any]:
        """Extract function metadata using introspection"""
        sig = inspect.signature(func)
        
        doc = inspect.getdoc(func) or "No description available"
        description = doc.split("\n")[0]
        
        type_hints = get_type_hints(func)
        parameters = []
        for param_name, param in sig.parameters.items():
            if param.default == inspect.Parameter.empty:
                param_type = type_hints.get(param_name, Any).__name__
                parameters.append({
                    "name": param_name,
                    "type": param_type,
                    "required": True
                })
            else:
                param_type = type_hints.get(param_name, Any).__name__
                parameters.append({
                    "name": param_name,
                    "type": param_type,
                    "required": False,
                    "default": param.default
                })
        
        return {
            "name": func.__name__,
            "description": description,
            "parameters": parameters,
            "full_docstring": doc
        }
    
    def register(self, func: Callable):
        """Register a function with automatically extracted metadata"""
        metadata = self._extract_function_metadata(func)
        self.functions[metadata["name"]] = func
        self.descriptions[metadata["name"]] = metadata
    
    def list_functions(self) -> List[str]:
        """List all registered function names"""
        return list(self.functions.keys())

class Agent:
    def __init__(self, model: str = "mixtral-8x7b-32768"):
        self.llm = GroqLLM(model=model)
        self.registry = FunctionRegistry()
        
    def register_function(self, func: Callable):
        """Register a function that the agent can call"""
        self.registry.register(func)
    
    def _create_function_prompt(self, query: str) -> str:
        functions_json = json.dumps(self.registry.descriptions, indent=2)
        return f"""You are a function router that maps user queries to the most appropriate function. Your response must be a valid JSON object.

User Query: {query}

Available Functions (with metadata):
{functions_json}

Instructions:
1. Analyze the user query and available functions
2. Select the most appropriate function based on its description and parameters
3. Extract parameter values from the query, respecting parameter types
4. Return a JSON object in EXACTLY this format, with NO ADDITIONAL WHITESPACE or FORMATTING:
{{"function":"<function_name>","parameters":{{"<param_name>":"<param_value>"}},"reasoning":"<one_line_explanation>"}}

Critical Rules:
- Response must be a SINGLE LINE of valid JSON
- NO line breaks, NO extra spaces
- NO markdown formatting or code blocks
- ALL strings must use double quotes
- Function name must be from available functions
- ALL required parameters must be included
- Parameter values must match the expected type
- Reasoning must be brief and single-line

Example Valid Response:
{{"function":"get_weather","parameters":{{"location":"New York"}},"reasoning":"Query asks about weather in a specific location"}}

Response (SINGLE LINE JSON):"""

    def _clean_json_response(self, response: str) -> str:
        """Clean and validate JSON response"""
        response = response.strip()
        if "```" in response:
            response = response.split("```")[1]
            if response.startswith("json"):
                response = response[4:]
        response = response.strip()
        
        response = " ".join(response.split())
        
        try:
            parsed = json.loads(response)
            return json.dumps(parsed, separators=(',', ':'))
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON response: {response[:100]}...")
    
    def process_query(self, query: str) -> Any:
        """Process a natural language query and route it to appropriate function"""
        if not self.registry.functions:
            raise ValueError("No functions registered with the agent")
            
        prompt = self._create_function_prompt(query)
        response = self.llm.generate(prompt)
        
        try:
            cleaned_response = self._clean_json_response(response)
            result = json.loads(cleaned_response)
            
            func_name = result["function"]
            parameters = result["parameters"]
            reasoning = result.get("reasoning", "No reasoning provided")
            
            if func_name not in self.registry.functions:
                raise ValueError(f"Function {func_name} not found. Available functions: {', '.join(self.registry.list_functions())}")
            
            func_metadata = self.registry.descriptions[func_name]
            for param in func_metadata["parameters"]:
                if param["required"] and param["name"] not in parameters:
                    raise ValueError(f"Missing required parameter: {param['name']}")
            
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