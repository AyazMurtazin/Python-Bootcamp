import asyncio
import aiohttp

GET_URL = 'http://127.0.0.1:8000/api/v1/tasks/redis/'


async def get_request(session: aiohttp.ClientSession):
    async with session.get(GET_URL) as response:
        print(await response.json())


async def main():
    async with aiohttp.ClientSession() as session:
        await get_request(session)

if __name__ == "__main__":
    asyncio.run(main())
