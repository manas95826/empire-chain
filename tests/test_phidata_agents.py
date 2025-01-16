from empire_chain.phidata_agents import PhiWebAgent, PhiFinanceAgent
import unittest
from dotenv import load_dotenv

load_dotenv()

class TestPhiAgents(unittest.TestCase):
    def test_phi_web_agent(self):
        agent = PhiWebAgent()
        agent.generate("What is the recent news about Tesla with sources?")

    def test_phi_finance_agent(self):
        agent = PhiFinanceAgent()
        agent.generate("What is the price of Tesla?")

if __name__ == "__main__":
    unittest.main()