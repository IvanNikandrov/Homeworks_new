import asyncio

import aiohttp

"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


