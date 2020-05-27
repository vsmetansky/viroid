import asyncio
from datetime import date

import pandas as pd

from viroid.collector.constants import COUNTRY_CODES
from viroid.collector.endpoints.endpoint import Endpoint
from viroid.collector.models.influenza import Influenza


class InfluenzaEndpoint(Endpoint):
    _model = Influenza
    _url = 'https://atlas.ecdc.europa.eu/Public/AtlasService/rest/GetMeasureResultsForTimePeriodAndGeoLevel' \
           '?measureIds=409230,409231,4092329&timeCodes=&startTimeCode={0}-W{1}&endTimeCodeExcl={2}-W{3}&geoLevel=1'
    _period = 2

    @classmethod
    def _fetch(cls):
        year, week = date.today().isocalendar()[:2]
        return cls._s.get(cls._url.format(year - cls._period, week, year, week))

    @classmethod
    async def _get_raw_entities(cls, response):
        return (await response.json()).get('MeasureResults')

    @classmethod
    def _filter_raw_entities(cls, raw_entities):
        # do something with removing invalid country codes
        return pd.DataFrame(raw_entities).filter(['dGeoMnemonic', 'TimeCode', 'N'])

    @classmethod
    def _preprocess_entities(cls, entities):
        return entities.groupby(['dGeoMnemonic', 'TimeCode']).agg('sum')

    @classmethod
    async def _save_entities(cls, entities):
        for e in entities.itertuples():
            await cls._model.add(
                cls._model(
                    cases_num=e.N,
                    country_code=e.Index[0],
                    date_updated=e.Index[1]
                )
            )
