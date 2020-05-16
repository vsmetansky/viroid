from aiohttp import web

routes = web.RouteTableDef()


@routes.get('/')
async def health_check(request):
    return web.Response(text="I am healthy!")


@routes.post('/search')
async def search(request):
    return web.Response()


@routes.post('/query')
async def search(request):
    return web.Response()


@routes.post('/annotations')
async def search(request):
    return web.Response()


@routes.post('/tag-keys')
async def search(request):
    return web.Response()


@routes.post('/tag-values')
async def search(request):
    return web.Response()
