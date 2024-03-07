from fastapi import FastAPI, HTTPException
from uuid import uuid4, UUID

from model import *

from aiohttp import ClientSession, ClientError
import asyncio

import aioredis

from urllib.parse import urlparse

REDIS_URL = "redis://localhost"

CLEANING_TIME = 10.

REDIS_STATUS = False


app = FastAPI()

TASKS = dict()


async def redis_open() -> aioredis.Redis:
    try:
        redis = await aioredis.from_url(REDIS_URL, decode_responses=True)
        return redis
    except:
        return None


async def clear_redis():
    while True:
        await asyncio.sleep(CLEANING_TIME)
        redis = await redis_open()
        if not (redis is None):
            await redis.flushdb()
            await redis.close()
            # await redis.wait_closed()


async def set_cache_response(url: str, response_code: int):
    redis = await redis_open()
    if not (redis is None):
        await redis.set(url, response_code)
        await redis.close()
        # await redis.wait_closed()


async def increment_domain_counter(domain: str):
    redis = await redis_open()
    if not (redis is None):
        await redis.incr(domain)
        await redis.close()


async def get_request_status(url: str) -> int:
    async with ClientSession() as session:
        try:
            async with session.get(url) as response:
                return response.status
        except ClientError:
            return "Error: Connection failed"


async def get_url_status(url: str) -> int:
    redis = await redis_open()
    if not (redis is None):
        value = await redis.get(url)
        if not (value is None):
            return value
    value = await get_request_status(url)
    await set_cache_response(url, value)
    return value


async def count_url_domain(url: str):
    domain = urlparse(url).netloc
    await increment_domain_counter(domain)


async def process_urls(task_id, urls):
    results = []
    async with ClientSession() as session:
        for url in urls.urls:
            await count_url_domain(url.url)
            value = await get_url_status(url.url)
            results.append((url.url, value))
    TASKS[task_id].status = "ready"
    TASKS[task_id].result = results


@app.get("/api/v1/tasks/{task_id}")
async def get_task(task_id: UUID):
    if task_id not in TASKS:
        raise HTTPException(status_code=404, detail="Task not found")
    return TASKS[task_id]


@app.get("/api/v1/tasks/redis/")
async def get_task():
    redis = await redis_open()
    if not (redis is None):
        keys = await redis.keys()
        result = [(key, await redis.get(key)) for key in keys]
        await redis.close()
        return result
    else:
        return "No Redis"


@app.post("/api/v1/tasks", status_code=201)
async def post_task(urls: URLs):
    task_id = uuid4()
    task = Task(id=task_id, status="running", result=[])
    TASKS[task_id] = task
    asyncio.create_task(process_urls(task_id, urls))
    return task


@app.on_event("startup")
async def app_startup():
    asyncio.create_task(clear_redis())
