from aiohttp import web

from viroid.server.routes import routes


def create_app():
    app = web.Application()
    app.add_routes(routes)
    return app