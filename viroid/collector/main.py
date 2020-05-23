import asyncio
import logging

import aiohttp
import aioredis

from viroid.collector.aggregates import Diseases, DiseasesEndpoints
from viroid.collector.endpoints.covid_19 import Covid19Endpoint
from viroid.collector.models.covid_19 import Covid19
from viroid.collector.models.disease import Disease

UPDATE_PERIOD = 0  # seconds


async def cleanup(redis, session):
    redis.close()
    await redis.wait_closed()
    await session.close()
    logging.info('Bye!')


async def main():
    try:
        logging.basicConfig(level=logging.INFO)
        session = aiohttp.ClientSession()
        redis = await aioredis.create_redis_pool(('localhost', 6379))
        diseases = Diseases(redis, Covid19, Disease)
        endpoints = DiseasesEndpoints(session, Covid19Endpoint)
        while True:
            await endpoints.pick_many()
            logging.info('Data updated...')
            await asyncio.sleep(UPDATE_PERIOD)
    finally:
        await cleanup(redis, session)


if __name__ == '__main__':
    asyncio.run(main())
