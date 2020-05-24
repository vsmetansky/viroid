import asyncio

import uvloop
from aiohttp import web

from viroid.server.factories import create_app

if __name__ == '__main__':
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    web.run_app(create_app())
