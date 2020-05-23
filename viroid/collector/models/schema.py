import asyncio
from pprint import pprint


class Schema(type):
    def __init__(cls, name, bases, dict):
        super().__init__(name, bases, dict)
        cls._schema_name = cls.__name__.lower()
        cls._keys_name = f'{cls._schema_name}_keys'
        cls._r = None

    async def get(cls, id_):
        raw_entity = await cls._r.hgetall(cls._key_from_id(id_))
        return cls._entity_from_raw(raw_entity)

    async def add(cls, entity):
        key = cls._key_from_id(f'{entity.country_code}|{entity.date_updated}')
        return await asyncio.gather(
            cls._r.sadd(cls._keys_name, key),
            cls._r.hmset_dict(key, vars(entity))
        )

    def _entity_from_raw(cls, raw_entity):
        if raw_entity:
            return cls(**cls._process_types(raw_entity))
        return None

    def _process_types(cls, raw_entity):
        """Deals with type conversion, usually during 'get' method call.

        If one stores boolean values in the entity, for instance,
        redis converts them to strings when storing, and, to receive
        booleans when getting, one should override this method.

        Returns:
            raw_entity (a dict) with correct types of the values
        """
        return {k.decode():v.decode() for k, v in raw_entity.items()}

    def _key_from_id(cls, id_):
        return f'{cls._schema_name}:{id_}'

    def _id_from_key(cls, key):
        return key.split(':').pop()
