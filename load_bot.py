import os

from telegrambot.manage import main
import django
from loguru import logger
from aiogram import executor

from create_bot import dp, db
import hendlers


async def on_startup(dispatcher):
    logger.info('Create connection')
    logger.info('Connection complete')


def setup_django():
    logger.info("CREATE DJANGO CONNECTION")
    main()
    logger.info("DJANGO WAS CONNECT")


if __name__ == '__main__':
    setup_django()
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
