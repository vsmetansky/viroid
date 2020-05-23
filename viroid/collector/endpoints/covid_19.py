import asyncio

from viroid.collector.endpoints.endpoint import Endpoint
from viroid.collector.models.covid_19 import Covid19


class Covid19Endpoint(Endpoint):
    _model = Covid19
    _url = 'https://opendata.ecdc.europa.eu/covid19/casedistribution/json/'

    @classmethod
    async def _filter_raw_entities(cls, response):
        raw_entities = (await response.json()).get('records')
        return (r_e for r_e in raw_entities if cls._is_valid_entity(r_e))

    @classmethod
    def _is_valid_entity(cls, entity):
        return entity.get('countryterritoryCode') and entity.get('dateRep')

    @classmethod
    async def _save_entities(cls, entities):
        await asyncio.gather(*(cls._model.add(
            cls._model(
                cases_num=e.get('cases'),
                deaths_num=e.get('deaths'),
                country_code=e.get('countryterritoryCode'),
                date_updated=e.get('dateRep')
            )
        ) for e in entities))
