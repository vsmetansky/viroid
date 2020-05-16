from aiohttp import web

from viroid.server.factories import create_app

if __name__ == '__main__':
    web.run_app(create_app())
