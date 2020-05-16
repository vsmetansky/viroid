class Schema(type):
    def __init__(cls):
        cls._next_id = 0
        cls._schema_name = cls.__name__.lower()
        cls._keys_name = f'{cls._schema_name}_ids'
        cls._r = None

    def get_all(cls):
        keys = cls._r.smembers(cls._keys_name)
        return (cls._r.get(cls._id_from_key(k)) for k in keys)

    def get(cls, id_):
        raw_entity = cls._r.hgetall(id_)
        return cls._entity_from_raw(raw_entity, id_)

    def add(cls, entity):
        key = cls._key_from_id(cls._next_id)
        cls._next_id += 1
        cls._r.sadd(cls._keys_name, key)
        return cls._r.hmset(key, vars(entity))

    def remove(cls, id_):
        return cls._r.delete(id_)

    def exists(cls, id_):
        return cls._r.exists(id_)

    def _entity_from_raw(cls, raw_entity, id_):
        raw_entity.id_ = id_
        return cls(**cls._process_types(raw_entity))

    def _process_types(cls, raw_entity):
        """Deals with type conversion during 'get' method call.

        If one stores boolean values in the entity, for instance,
        redis converts them to strings when storing, and, to receive
        booleans when getting, one should override this method.

        Returns:
            raw_entity (a dict) with correct types of the values
        """
        return raw_entity

    def _key_from_id(cls, id_):
        return f'{cls._schema_name}:{id_}'

    def _id_from_key(cls, key):
        return key.split(':').pop()
