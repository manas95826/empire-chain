"""
This is a simple example of how to use the WebAgent class to generate web data.
Please run the following command to install the necessary dependencies and store keys in .env:
!pip install empire-chain phidata duckduckgo-search
"""
from empire_chain.phidata.web_agent import WebAgent

web_agent = WebAgent()

web_agent.generate("What is the price of Tesla?")