from viroid.server.models.schema import Schema


class Disease(metaclass=Schema):
    def __init__(self, cases_num, country_code, date_updated):
        self.cases_num = cases_num
        self.country_code = country_code
        self.date_updated = date_updated
