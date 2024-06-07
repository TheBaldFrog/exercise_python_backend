import typing as tp

from app.context import AppContext
from app import models


async def get_scooters(context: AppContext) -> tp.List[models.Scooter]:
    sql = """
    select id, location, scooters.user from scooters
    """
    rows = await context.db.fetch(sql)
    print(rows)

    return [models.Scooter.from_db(row) for row in rows]
