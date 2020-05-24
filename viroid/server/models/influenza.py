from viroid.server.models.disease import Disease


class Influenza(Disease):
    def __init__(self, cases_num, country_code, date_updated):
        super().__init__(
            cases_num=cases_num,
            country_code=country_code,
            date_updated=date_updated
        )
