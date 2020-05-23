import json
from pprint import pprint

from aiohttp import web

from viroid.server.models.covid_19 import Covid19

routes = web.RouteTableDef()


@routes.get('/')
async def health_check(request):
    return web.Response(text="I am healthy!")


@routes.post('/search')
async def search(request):
    return web.json_response((
        'COVID-19', 'Influenza'
    ))


@routes.post('/query')
async def search(request):
    request_json = json.loads(await request.text())
    if request_json['targets'][0]['type'] == 'table':
        series = request_json['targets'][0]['target']
        bodies = {'COVID-19': [{
            "columns": [
                {"text": "Country", "type": "string"},
                {"text": "Cases", "type": "number"},
            ],
            "rows": [[x.country_code, int(x.cases_num)] for x in (await Covid19.get_all())],
            "type": "table"
        }], 'Influenza': [{
            "columns": [
                {"text": "Country", "type": "string"},
                {"text": "Cases", "type": "number"}
            ],
            "rows": [],
            "type": "table"
        }]}
        return web.json_response(bodies[series])


@routes.post('/annotations')
async def search(request):
    return web.Response()
