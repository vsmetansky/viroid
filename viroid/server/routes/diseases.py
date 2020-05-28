import json

from aiohttp import web

from viroid.server.routes.queries.covid_19 import Covid19TableQuery
from viroid.server.routes.queries.influenza import InfluenzaTableQuery

SERIES_DATA = {
    'COVID-19': (Covid19TableQuery(),),
    'Influenza': (InfluenzaTableQuery(),)
}

routes = web.RouteTableDef()


@routes.get('/')
async def health_check(request):
    return web.Response(text="I am healthy!")


@routes.post('/search')
async def search(request):
    return web.json_response(tuple(SERIES_DATA.keys()))


@routes.post('/query')
async def query(request):
    request_json = json.loads(await request.text())
    target = request_json['targets'][0]
    if target['type'] == 'table':
        series = target['target']
        filters = request_json['adhocFilters']
        return web.json_response(await SERIES_DATA.get(series)[0].body())


@routes.post('/annotations')
async def annotations(request):
    return web.Response()


@routes.post('/tag-keys')
async def filter_keys(request):
    return web.json_response([{"type": "string", "text": "country"}])


@routes.post('/tag-values')
async def filter_values(request):
    request_json = json.loads(await request.text())
    responses = {
        'country': [{'text': 'US'}],
    }
    return web.json_response(responses.get(request_json['key']))
