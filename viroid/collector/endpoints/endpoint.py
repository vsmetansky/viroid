class Endpoint:
    _url = None
    _model = None
    _s = None

    @classmethod
    async def pick(cls):
        """Gets data from API and writes it to Redis."""
        async with cls._s.get(cls._url) as response:
            await cls._save_response_data(response)

    @classmethod
    async def _save_response_data(cls, response):
        """Writes data to Redis."""
        pass
