"""Main tests module."""
import os
from aiohttp import web
import views
import controller


PATH = os.path.dirname(os.path.realpath(__file__))


def test_search_country():
    """Test search country function."""
    ip_address = "1.1.1.1"
    country = controller.search_country(ip_address)
    assert country == "Australia"


countries = [
    "United States",
    "Japan",
    "United States",
    "China",
    "Japan",
    "Denmark",
    "United States",
    "Netherlands",
    "France",
    "Russia",
    "New Zealand",
    "Switzerland",
]


def test_search_countries():
    """Test search country function."""
    ips = open(PATH + "/1_ips.txt", "r").readlines()
    for ip_address in ips:
        country = controller.search_country(ip_address.replace("\n", ""))
        print(country)
        idx = ips.index(ip_address)
        real_contry = countries[idx]
        assert country == real_contry


async def test_hello(aiohttp_client, loop):
    app = web.Application()
    app.add_routes(views.ROUTES)
    client = await aiohttp_client(app)
    resp = await client.get("/")
    assert resp.status == 200

async def test_search(aiohttp_client, loop):
    app = web.Application()
    app.add_routes(views.ROUTES)
    client = await aiohttp_client(app)
    resp = await client.get("/1.1.1.1")
    assert resp.status == 200


if __name__ == "__main__":
    test_search_countries()
