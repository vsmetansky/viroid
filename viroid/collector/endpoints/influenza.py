import asyncio

import pandas as pd
from viroid.collector.endpoints.endpoint import Endpoint
from viroid.collector.models.disease import Disease


class InfluenzaEndpoint(Endpoint):
    _model = Disease
    _url = 'https://apps.who.int/flumart/Reserved.ReportViewerWebControl.axd?ReportSession=v45tez4513m0lc55tbvzhw45' \
           '&Culture=1033&CultureOverrides=True&UICulture=1033&UICultureOverrides=True&ReportStack=1&ControlID' \
           '=a4ebbe704a1444b7bbd1d6105bc9f079&OpType=Export&FileName=Rpt_LabSurveillanceDataLatestWeekByCtry' \
           '&ContentDisposition=OnlyHtmlInline&Format=CSV '

    @classmethod
    async def _save_data(cls, data):
        raw_entities = pd.read_csv(await response.text(), header=0)
        await asyncio.gather(*(cls._model.add(
            cls._model(
                cases_num=r_e.get('cases'),
                country_code=r_e.get('countryterritoryCode'),
                date_updated=r_e.get('dateRep')
            )
        ) for r_e in raw_entities))
