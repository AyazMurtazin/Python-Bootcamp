from typing import Union

from fastapi import FastAPI, HTTPException

from uuid import uuid4, UUID

from model import *

import logging

from aiohttp import ClientSession, ClientError
import asyncio

app = FastAPI()

TASKS = dict()


async def process_urls(task_id, urls):
    results = []
    async with ClientSession() as session:
        for url in urls.urls:
            try:
                async with session.get(url.url) as response:
                    results.append((url.url, response.status))
            except ClientError:
                results.append((url.url, "Error: Connection failed"))

    TASKS[task_id].status = "ready"
    TASKS[task_id].result = results


@app.get("/api/v1/tasks/{task_id}")
async def get_task(task_id: UUID):
    if task_id not in TASKS:
        raise HTTPException(status_code=404, detail="Task not found")
    return TASKS[task_id]


@app.post("/api/v1/tasks", status_code=201)
async def post_task(urls: URLs):
    task_id = uuid4()
    task = Task(id=task_id, status="running", result=[])
    TASKS[task_id] = task
    asyncio.create_task(process_urls(task_id, urls))
    return task
