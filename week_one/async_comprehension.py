# Async Comprehensions:
# are a way to create a list, set, or dict asynchronously
# are similar to list comprehensions, but they use the async/await syntax
# are used with async generators

# example of async comprehensions:
import asyncio
import aiohttp


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    urls = ['https://python.org', 'https://google.com', 'https://yahoo.com']
    async with aiohttp.ClientSession() as session:
        htmls = [await fetch(session, url) for url in urls]
        print(htmls)

# Run the function
asyncio.run(main())
