from empire_chain.llms import GroqLLM
import matplotlib.pyplot as plt
import json
from dotenv import load_dotenv
import os
from abc import ABC, abstractmethod
from typing import Optional, Dict, Any, Union, Tuple

load_dotenv()

class DataAnalyzer:
    def __init__(self):
        self.client = GroqLLM(custom_instructions="""You are a data analysis expert. Your task is to analyze input data and structure it for visualization.
Your response must ALWAYS be a valid JSON object with no additional text, comments, or explanations outside the JSON structure.

Rules:
1. Always return valid JSON with either:
   Success: {"title": string, "x-axis": string, "y-axis": string, "datapoints": object}
   Failure: {"result": null, "error": string}
2. For numerical data: Extract or calculate meaningful metrics
3. For categorical data: Generate frequency counts or proportions
4. For time-series: Preserve chronological order
5. Clean and standardize inconsistent data
6. Handle both structured and unstructured text input
7. If data format is unclear but usable, make reasonable assumptions and note them in the title
8. If no numerical values can be extracted, return null result
9. Ensure all datapoint values are numbers, not text""")

    def analyze(self, data: str) -> Dict[str, Any]:
        prompt = f"""IMPORTANT: Respond ONLY with a valid JSON object. No other text or explanation.

Analyze the following data and structure it for visualization.
If the data cannot be meaningfully converted to datapoints or lacks numerical values, return a null result with explanation.

Required JSON structure (use exactly this format):
{{
    "title": "Descriptive title of the analysis",
    "x-axis": "Label for x-axis",
    "y-axis": "Label for y-axis",
    "datapoints": {{
        "category1": value1,
        "category2": value2
    }} or [value1, value2, ...]
}}
OR if data cannot be processed:
{{
    "result": null,
    "error": "Explanation of why data cannot be processed"
}}

Input data to analyze:
{data}

Remember: Return ONLY the JSON object, no other text."""
        
        try:
            response = self.client.generate(prompt)
            response = response.strip()
            if response.startswith('```json'):
                response = response[7:]
            if response.startswith('```'):
                response = response[3:]
            if response.endswith('```'):
                response = response[:-3]
            response = response.strip()
            
            return json.loads(response)
        except json.JSONDecodeError as e:
            print(f"Failed to parse LLM response as JSON: {response}")
            return {
                "result": None,
                "error": f"Failed to generate valid JSON from analysis: {str(e)}"
            }
        except Exception as e:
            return {
                "result": None,
                "error": f"Error during data analysis: {str(e)}"
            }

class BaseChart(ABC):
    def __init__(self, data_json: Union[str, Dict], fig_ax: Optional[Tuple[plt.Figure, plt.Axes]] = None):
        self.data = json.loads(data_json) if isinstance(data_json, str) else data_json
        if fig_ax is None:
            self.fig, self.ax = plt.subplots(figsize=(10, 6))
        else:
            self.fig, self.ax = fig_ax

    @abstractmethod
    def plot(self) -> Optional[plt.Figure]:
        pass

    def show(self):
        """Display the chart."""
        if self.plot():
            plt.show()

    def _validate_data(self) -> bool:
        if "result" in self.data and self.data["result"] is None:
            print(f"Error in data: {self.data.get('error', 'Unknown error')}")
            return False
        try:
            if isinstance(self.data['datapoints'], dict):
                return all(isinstance(v, (int, float)) for v in self.data['datapoints'].values())
            elif isinstance(self.data['datapoints'], list):
                return all(isinstance(v, (int, float)) for v in self.data['datapoints'])
        except Exception:
            return False
        return True

class LineChart(BaseChart):
    def plot(self) -> Optional[plt.Figure]:
        if not self._validate_data():
            return None
        
        if isinstance(self.data['datapoints'], dict):
            categories = list(self.data['datapoints'].keys())
            values = list(self.data['datapoints'].values())
        else:
            categories = [f'Point {i+1}' for i in range(len(self.data['datapoints']))]
            values = self.data['datapoints']
        
        self.ax.plot(categories, values, marker='o', linewidth=2)
        self.ax.set_xlabel(self.data['x-axis'])
        self.ax.set_ylabel(self.data['y-axis'])
        self.ax.set_title(self.data['title'])
        plt.xticks(rotation=45)
        plt.tight_layout()
        return self.fig

class PieChart(BaseChart):
    def plot(self) -> Optional[plt.Figure]:
        if not self._validate_data():
            return None
        
        categories = list(self.data['datapoints'].keys())
        values = list(self.data['datapoints'].values())
        
        self.ax.pie(values, labels=categories, autopct='%1.1f%%')
        self.ax.set_title(self.data['title'])
        plt.tight_layout()
        return self.fig

class BarGraph(BaseChart):
    def plot(self) -> Optional[plt.Figure]:
        if not self._validate_data():
            return None
        
        categories = list(self.data['datapoints'].keys())
        values = list(self.data['datapoints'].values())
        
        self.ax.bar(categories, values)
        self.ax.set_xlabel(self.data['x-axis'])
        self.ax.set_ylabel(self.data['y-axis'])
        self.ax.set_title(self.data['title'])
        plt.xticks(rotation=45)
        plt.tight_layout()
        return self.fig

class ScatterChart(BaseChart):
    def plot(self) -> Optional[plt.Figure]:
        if not self._validate_data():
            return None
        
        categories = list(self.data['datapoints'].keys())
        values = list(self.data['datapoints'].values())
        
        self.ax.scatter(categories, values)
        self.ax.set_xlabel(self.data['x-axis'])
        self.ax.set_ylabel(self.data['y-axis'])
        self.ax.set_title(self.data['title'])
        plt.xticks(rotation=45)
        plt.tight_layout()
        return self.fig

class Histogram(BaseChart):
    def plot(self) -> Optional[plt.Figure]:
        if not self._validate_data():
            return None
        
        values = list(self.data['datapoints'].values())
        
        self.ax.hist(values, bins='auto')
        self.ax.set_xlabel(self.data['y-axis'])
        self.ax.set_ylabel('Frequency')
        self.ax.set_title(self.data['title'])
        plt.tight_layout()
        return self.fig

class BoxPlot(BaseChart):
    def plot(self) -> Optional[plt.Figure]:
        if not self._validate_data():
            return None
        
        values = list(self.data['datapoints'].values())
        
        self.ax.boxplot(values)
        self.ax.set_ylabel(self.data['y-axis'])
        self.ax.set_title(self.data['title'])
        plt.tight_layout()
        return self.fig

class ChartFactory:
    _chart_types = {
        'Line Chart': LineChart,
        'Pie Chart': PieChart,
        'Bar Graph': BarGraph,
        'Scatter Plot': ScatterChart,
        'Histogram': Histogram,
        'Box Plot': BoxPlot
    }

    @classmethod
    def create_chart(cls, chart_type: str, data_json: Union[str, Dict], fig_ax: Optional[Tuple[plt.Figure, plt.Axes]] = None) -> Optional[BaseChart]:
        chart_class = cls._chart_types.get(chart_type)
        if chart_class:
            return chart_class(data_json, fig_ax)
        return None
