from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools

class FinanceAgent(Agent):
    def __init__(self):
        super().__init__(name="Finance Agent")
        self.tools = [YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)]
        self.instructions = ["Always include sources"]
        self.model = OpenAIChat(id="gpt-4o-mini")
        self.show_tool_calls = True
        self.markdown = True

    def generate(self, prompt: str) -> str:
        return self.print_response(prompt, stream=True)