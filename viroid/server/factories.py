import asyncio

import aredis
from aiohttp import web

from viroid.server.aggregates import Diseases
from viroid.server.models.covid_19 import Covid19
from viroid.server.models.influenza import Influenza
from viroid.server.routes import diseases

MAX_CONNECTION_NUM = 100


async def init_redis(app):
    app['redis'] = aredis.StrictRedisCluster(
        host='localhost', port=7000, decode_responses=True, max_connections=MAX_CONNECTION_NUM)
    diseases = Diseases(app['redis'], Covid19, Influenza)


async def start_background_tasks(app):
    app['init_redis'] = asyncio.create_task(init_redis(app))


async def cleanup_background_tasks(app):
    app['init_redis'].cancel()
    await app['init_redis']


def create_app():
    app = web.Application()
    app.add_routes(diseases.routes)
    app.on_startup.append(start_background_tasks)
    app.on_cleanup.append(cleanup_background_tasks)
    return app
