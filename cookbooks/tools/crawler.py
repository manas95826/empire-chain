"""
This is a simple crawler that uses the Empire Chain library to crawl a website and save the content as markdown.
Please run the following command to install the necessary dependencies and store keys in .env:
!pip install empire-chain crawl4ai
!playwright install
"""
from empire_chain.tools.crawl4ai import Crawler

crawler = Crawler()
result = crawler.crawl(url="https://www.geekroom.in", format="markdown")
print(result)
