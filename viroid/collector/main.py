import asyncio
import logging

import aiohttp
import aredis
import uvloop

from viroid.collector.init import get_endpoints

UPDATE_PERIOD = 0  # seconds
MAX_CONNECTION_NUM = 100  # goddamn aredis creates separate connection for each operation


async def cleanup(session):
    await session.close()
    logging.info('Bye!')


async def main():
    try:
        logging.basicConfig(level=logging.INFO)
        session = aiohttp.ClientSession()
        redis = aredis.StrictRedisCluster(
            host='localhost', port=7000, decode_responses=True, max_connections=MAX_CONNECTION_NUM)
        endpoints = get_endpoints(session, redis)

        while True:
            await endpoints.pick_many()
            logging.info('Data updated...')
            await asyncio.sleep(UPDATE_PERIOD)
    finally:
        await cleanup(session)


if __name__ == '__main__':
    uvloop.install()
    asyncio.run(main())
