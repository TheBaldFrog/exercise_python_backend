import typing as tp
import asyncpg  # type: ignore
from app.utils import secrets
import config


class AppContext:
    def __init__(self, *, secrets_dir: str):
        self.secrets: secrets.SecretsReader = secrets.SecretsReader(secrets_dir)
        self.db: tp.Optional[asyncpg.Pool] = None

    async def on_startup(self, app=None):
        self.db = await asyncpg.create_pool(config.POSTGRES_URI)

    async def on_shutdown(self, app=None):
        if self.db is not None:
            await self.db.close()
