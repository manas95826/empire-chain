from empire_chain.phidata.phidata_agents import PhiWebAgent, PhiFinanceAgent
from dotenv import load_dotenv

load_dotenv()

web_agent = PhiWebAgent()
web_agent.generate("What is the recent news about Tesla with sources?")

finance_agent = PhiFinanceAgent()
finance_agent.generate("What is the price of Tesla?")