from datetime import datetime as dt

from viroid.collector.models.disease import Disease


class Covid19(Disease):
    def __init__(self, cases_num, deaths_num, country_code, date_updated):
        super().__init__(
            cases_num=cases_num,
            country_code=country_code,
            date_updated=date_updated
        )
        self.deaths_num = deaths_num

    @classmethod
    def _compare_entities(cls, prev_entity, entity):
        try:
            date_prev = dt.strptime(prev_entity.date_updated, '%d/%m/%Y')
            date = dt.strptime(entity.date_updated, '%d/%m/%Y')
            return date_prev < date
        except AttributeError:
            return True