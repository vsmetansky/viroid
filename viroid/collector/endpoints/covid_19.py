import asyncio

from viroid.collector.endpoints.endpoint import Endpoint
from viroid.collector.models.covid_19 import Covid19


class Covid19Endpoint(Endpoint):
    _model = Covid19
    _url = 'https://opendata.ecdc.europa.eu/covid19/casedistribution/json/'

    @classmethod
    async def _save_response_data(cls, response):
        raw_entities = (await response.json()).get('records')
        await asyncio.gather(*(Covid19.add(
            Covid19(
                cases_num=r_e.get('cases'),
                deaths_num=r_e.get('deaths'),
                country_code=r_e.get('countryterritoryCode'),
                date_updated=r_e.get('dateRep')
            )
        ) for r_e in raw_entities))
