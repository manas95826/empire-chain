"""
This is a cookbook for the LLMPlayground

To run this cookbook, you need to have the empire-chain library installed.

You can install it using the following command:

```bash
pip install empire-chain streamlit
```
"""
from empire_chain.playground.compare_llms import LLMPlayground

llm_playground = LLMPlayground()
llm_playground.launch()