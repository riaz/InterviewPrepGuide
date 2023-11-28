# Note: This code has error
import aiohttp
import asyncio

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()
        
async def main():
    urls = ["www.appliedllms.com", "www.pixls.ai"]
    tasks = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)

    for url, result in zip(urls, results):
        print(f"Contents of {url}")
        print(result[:100])

if __name__ == '__main__':
    asyncio.run(main())