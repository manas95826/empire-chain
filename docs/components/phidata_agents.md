# PhiData Agents

Empire Chain integrates with PhiData to provide specialized agents for various tasks.

## Web Agent

The Web Agent helps gather and analyze information from the internet:

```python
from empire_chain.phidata.web_agent import WebAgent

# Create web agent
web_agent = WebAgent()

# Generate response about a topic
response = web_agent.generate("What is the price of Tesla?")
print(response)
```

## Finance Agent

The Finance Agent specializes in financial analysis and stock market data:

```python
from empire_chain.phidata.finance_agent import PhiFinanceAgent

# Create finance agent
finance_agent = PhiFinanceAgent()

# Analyze stock performance
analysis = finance_agent.generate("Analyze TSLA stock performance")
print(analysis)
```

## Features

- **Web Agent**:
  - Real-time web search
  - Information synthesis
  - Data extraction
  - News analysis

- **Finance Agent**:
  - Stock analysis
  - Market trends
  - Financial metrics
  - Price predictions

## Installation

```bash
pip install empire-chain phidata
```

Additional dependencies:
- Web Agent: `pip install duckduckgo-search`
- Finance Agent: `pip install yfinance`

For more examples and advanced usage, check out the PhiData agent cookbooks in the repository. 