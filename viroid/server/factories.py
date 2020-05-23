import asyncio

import aioredis
from aiohttp import web

from viroid.server.aggregates import Diseases
from viroid.server.models.covid_19 import Covid19
from viroid.server.routes import routes


async def close_redis(redis):
    redis.close()
    await redis.wait_closed()


async def init_redis(app):
    try:
        app['redis'] = await aioredis.create_redis_pool(('localhost', 6379))
        diseases = Diseases(app['redis'], Covid19)
    except asyncio.CancelledError:
        await close_redis(app['redis'])


async def start_background_tasks(app):
    app['init_redis'] = asyncio.create_task(init_redis(app))


async def cleanup_background_tasks(app):
    app['init_redis'].cancel()
    await app['init_redis']
    await close_redis(app['redis'])


def create_app():
    app = web.Application()
    app.add_routes(routes)
    app.on_startup.append(start_background_tasks)
    app.on_cleanup.append(cleanup_background_tasks)
    return app
