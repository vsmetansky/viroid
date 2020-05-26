import asyncio
import logging

import aiohttp
import aioredis
import uvloop

from viroid.collector.init import get_endpoints

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
        endpoints = get_endpoints(session, redis)
        while True:
            await endpoints.pick_many()
            logging.info('Data updated...')
            await asyncio.sleep(UPDATE_PERIOD)
    finally:
        await cleanup(redis, session)


if __name__ == '__main__':
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    asyncio.run(main())
