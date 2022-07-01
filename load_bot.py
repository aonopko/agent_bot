from loguru import logger
from aiogram import executor
from create_bot import db
from hendlers import dp


async def on_startup(dispatcher):
    logger.info('Створюємо підключення')
    await db.create()

    logger.info('Створюємо таблицю агентів')
    await db.create_table_agent()
    logger.info('Готово')

    logger.info('Створюємо таблицю маршруту')
    await db.create_table_route_sheet()
    logger.info('Готово')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
