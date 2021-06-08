"""Speedtest runner async."""
import asyncio
import os
import time

import aiohttp
import uvloop

PATH = os.path.dirname(os.path.realpath(__file__))


async def fetch(client, url):
    """Make request to our geolocatio service."""
    async with client.get(url) as resp:
        assert resp.status == 200
        return await resp.text()


async def main():
    """Make request to our geolocatio service."""
    async with aiohttp.ClientSession() as client:
        start = time.perf_counter()
        ips = open(PATH + "/10K_ips.txt", "r").readlines()
        for ip_address in ips:
            url = "http://0.0.0.0:8080/" + ip_address.replace("\n", "")
            res = await fetch(client, url)
            print(res)
        elapsed = time.perf_counter() - start
        print(f"10K executed in {elapsed:0.2f} seconds.")


loop = uvloop.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(main())
