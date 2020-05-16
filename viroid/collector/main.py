import asyncio

from viroid.collector.endpoints import covid, influenza


async def main():
    async with aiohttp.ClientSession(timeout=60) as client:
        data_pickers = (
            covid, influenza
        )
        await asyncio.gather(x.pick(client) for x in data_pickers)


if __name__ == '__main__':
    asyncio.run(main())
