from aiohttp import web

routes = web.RouteTableDef()


@routes.get('/')
async def index(req):
    return web.Response(text='fuck')
