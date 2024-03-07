import aiohttp
import argparse
import asyncio
from model import URL, URLs, Task

from uuid import UUID

POST_URL = 'http://127.0.0.1:8000/api/v1/tasks/'


def parse() -> URLs:
    parser = argparse.ArgumentParser(
        description="Receives one or several queryable URLs as an argument")
    parser.add_argument("urls", nargs="+", type=str)

    return URLs(urls=[URL(url=i) for i in parser.parse_args().urls])


async def post_request(post_url: str, urls: URLs, session: aiohttp.ClientSession) -> Task:
    async with session.post(post_url, json=urls.model_dump()) as response:
        return await response.json()


async def get_request(get_url: str, task_id: UUID, session: aiohttp.ClientSession):
    while True:
        async with session.get(get_url+str(task_id)) as response:
            task = await response.json()
            if task['status'] == "ready":
                return task
            await asyncio.sleep(1)


async def main():
    urls = parse()
    async with aiohttp.ClientSession() as session:
        task = await post_request(POST_URL, urls, session)
        result_task = await get_request(POST_URL, task['id'],  session)
        [print(f'{i} {j}', end=" ")for i, j in result_task['result']]
        print()
if __name__ == "__main__":
    asyncio.run(main())
