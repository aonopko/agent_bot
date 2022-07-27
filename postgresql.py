from gino import Gino
from loguru import logger
import asyncio
from var_for_db import POSTGRES_URI

db = Gino()

async def create_db():
    await db.set_bind(POSTGRES_URI)
    logger.info("add table")
    await db.gino.create_all()

loop = asyncio.get_event_loop()
loop.run_until_complete(create_db())
