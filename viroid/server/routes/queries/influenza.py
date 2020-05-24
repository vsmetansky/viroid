from viroid.server.models.influenza import Influenza
from viroid.server.routes.queries.table_query import TableQuery


class InfluenzaTableQuery(TableQuery):
    def _columns(self):
        return (
            {'text': 'Date', 'type': 'String'},
            {'text': 'Country', 'type': 'String'},
            {'text': 'Cases', 'type': 'Number'}
        )

    async def _rows(self, filters):
        return [[x.date_updated, x.country_code, int(x.cases_num)] for x in (await Influenza.get_all())]
