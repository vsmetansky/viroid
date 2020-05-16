import asyncio

import aiohttp
import aioredis

from viroid.collector.aggregates import Diseases, DiseasesEndpoints
from viroid.collector.endpoints.covid_19 import Covid19Endpoint
from viroid.collector.models.covid_19 import Covid19


async def cleanup(redis, session):
    redis.close()
    await redis.wait_closed()
    await session.close()


async def main():
    try:
        session = aiohttp.ClientSession(timeout=60)
        redis = await aioredis.create_redis_pool(('localhost', 6379))
        diseases = Diseases(redis, Covid19)
        endpoints = DiseasesEndpoints(session, Covid19Endpoint)
        while True:
            await endpoints.pick_many()
    finally:
        await cleanup(redis, session)


if __name__ == '__main__':
    asyncio.run(main())
