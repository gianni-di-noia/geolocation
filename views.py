"""
Geolocation service.
"""
from aiohttp import web

import controller

ROUTES = web.RouteTableDef()


@ROUTES.get("/")
async def hello(request):
    """Hello wolrd handler."""
    return web.json_response(request.match_info)


@ROUTES.get("/{ip_address}")
async def get_country(request):
    """Hello wolrd handler."""
    country = controller.search_country(request.match_info["ip_address"])
    return web.json_response({"success": True, "country": country})


APP = web.Application()
APP.add_routes(ROUTES)
