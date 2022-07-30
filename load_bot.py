from loguru import logger
from aiogram import executor
from create_bot import dp
from db.models import create_db


async def on_startup(dispatcher):
    logger.info('Create connection')
    await create_db()
    logger.info('Connection complete')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
