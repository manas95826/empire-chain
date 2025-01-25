import asyncio
from crawl4ai import AsyncWebCrawler

class Crawler:
    def __init__(self):
        self.crawler = AsyncWebCrawler()

    def crawl(self, url: str, format: str = "markdown"):
        async def _crawl():
            async with self.crawler as crawler:
                result = await crawler.arun(url=url)
                
            if format == "markdown":
                return result.markdown
            elif format == "html":
                return result.html
            elif format == "cleaned_html":
                return result.cleaned_html
            elif format == "fit_markdown":
                return result.fit_markdown
            elif format == "success":
                return result.success
            elif format == "status_code":
                return result.status_code
            elif format == "media":
                return result.media
            elif format == "links":
                return result.links
            else:
                raise ValueError(f"Invalid format: {format}")

        return asyncio.run(_crawl())