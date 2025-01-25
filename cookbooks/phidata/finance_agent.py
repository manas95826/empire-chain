"""
This is a simple example of how to use the PhiFinanceAgent class to generate financial data.
Please run the following command to install the necessary dependencies and store keys in .env:
!pip install empire-chain phidata yfinance
"""
from empire_chain.phidata.finance_agent import PhiFinanceAgent

finance_agent = PhiFinanceAgent()

finance_agent.generate("What is the price of Tesla?")