from aiogram import executor

import logging

from hendlers import dp

from create_bot import db


async def on_startup(dispatcher):
    logging.info('Создаем подключение')
    await db.create()






if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
