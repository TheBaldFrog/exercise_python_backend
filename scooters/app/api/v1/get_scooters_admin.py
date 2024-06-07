from aiohttp import web

from app.context import AppContext
from app import storage
from app import models


async def handle(request: web.Request, context: AppContext) -> web.Response:
    scooters = await storage.get_scooters(context)
    return web.json_response({"items": [to_response(scooter) for scooter in scooters]})


def to_response(scooter: models.Scooter) -> dict:
    return {
        "id": scooter.id,
        "location": {"lon": scooter.location.lon, "lat": scooter.location.lat},
        "user": scooter.user.id if scooter.user else None,
    }
