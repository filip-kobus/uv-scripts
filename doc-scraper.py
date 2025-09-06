# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "asyncio",
#     "crawl4ai",
# ]
# ///

import sys
import asyncio
from crawl4ai import *


async def main():
    if len(sys.argv) < 2:
        script_name = sys.argv[0].split("/")[-1].split("\\")[-1].replace(".py", "")
        print(f"Usage: run {script_name} <url>")
        sys.exit(1)
    url = sys.argv[1]
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=url)
        print(result.markdown)

if __name__ == "__main__":
    asyncio.run(main())