from datetime import datetime as dt

from viroid.collector.models.disease import Disease


class Influenza(Disease):
    def __init__(self, cases_num, country_code, date_updated):
        date_updated_raw = dt.strptime(date_updated + '-1', '%Y-W%W-%w')
        super().__init__(
            cases_num=cases_num,
            country_code=country_code,
            date_updated=date_updated_raw.strftime('%d/%m/%Y')
        )
