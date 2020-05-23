class Endpoint:
    _url = None
    _model = None
    _s = None

    @classmethod
    async def pick(cls):
        """Gets data from API and writes it to Redis."""
        async with cls._s.get(cls._url) as response:
            entities = await cls._filter_raw_entities(response)
            await cls._save_entities(entities)

    @classmethod
    async def _filter_raw_entities(cls, response):
        """Validates and filters raw data.

        Returns a generator of valid data.
        """
        pass

    @classmethod
    def _is_valid_entity(cls, entity):
        """Checks if given entity is valid.

        The method is used by _filter_raw_data
        and returns True or False.
        """
        pass

    @classmethod
    async def _save_entities(cls, entities):
        """Writes data to Redis."""
        pass
