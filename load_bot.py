from loguru import logger
from aiogram import executor

from create_bot import dp, db
import hendlers


async def on_startup(dispatcher):
    logger.info('Create connection')
    await db.create()
    await db.create_table_agent()
    await db.create_table_route_sheet()
    logger.info('Connection complete')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
