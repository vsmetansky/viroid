from viroid.server.models.covid_19 import Covid19
from viroid.server.routes.queries.table_query import TableQuery


class Covid19TableQuery(TableQuery):
    def _columns(self):
        return (
            {'text': 'Date', 'type': 'String'},
            {'text': 'Country', 'type': 'String'},
            {'text': 'Cases', 'type': 'Number'}
        )

    async def _rows(self, filters):
        return [[x.date_updated, x.country_code, int(x.cases_num)] for x in (await Covid19.get_all())]
