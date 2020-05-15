from aiohttp import web

from viroid.factories import create_app

if __name__ == '__main__':
    web.run_app(create_app())
