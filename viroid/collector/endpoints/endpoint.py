class Endpoint:
    _url = None
    _model = None
    _s = None

    @classmethod
    async def pick(cls):
        """Gets data from API and writes it to Redis."""
        async with cls._fetch() as response:
            raw_entities = await cls._get_raw_entities(response)
            entities = cls._filter_raw_entities(raw_entities)
            preprocessed_entities = cls._preprocess_entities(entities)
            await cls._save_entities(preprocessed_entities)

    @classmethod
    def _fetch(cls):
        return cls._s.get(cls._url)

    @classmethod
    async def _get_raw_entities(cls, response):
        """Extracts needed data from response."""
        return await response.json()

    @classmethod
    def _filter_raw_entities(cls, raw_entities):
        """Validates and filters raw data.

        Returns a generator of valid data.
        """
        return raw_entities

    @classmethod
    def _is_valid_entity(cls, entity):
        """Checks if given entity is valid.

        The method is used by _filter_raw_data
        and returns True or False.
        """
        return True

    @classmethod
    def _preprocess_entities(cls, entities):
        """Usually suits for data regrouping, etc."""
        return entities

    @classmethod
    async def _save_entities(cls, entities):
        """Writes data to Redis."""
        pass
