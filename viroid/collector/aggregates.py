import asyncio


class Diseases:
    def __init__(self, db, *diseases):
        for d in diseases:
            d._r = db


class DiseasesEndpoints:
    def __init__(self, session, *endpoints):
        self.endpoints = endpoints
        for e in endpoints:
            e._s = session

    async def pick_many(self):
        await asyncio.gather(*(e.pick() for e in self.endpoints))
