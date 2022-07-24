from asyncpg.exceptions import UniqueViolationError
from aiogram import types
from aiogram.dispatcher.filters import Command
from keybords.reply_keybords import menu
from create_bot import dp, db, bot
from inline_keybords.inline_menu import route_kb


@dp.message_handler(Command("start"))
async def start(message: types.Message):
    await message.answer('Привіт агент', reply_markup=menu)


@dp.message_handler(text="Меню")
async def new_agent(message: types.Message):
    try:
        await db.add_agent(
            full_name=message.from_user.full_name,
            telegram_id=message.from_user.id)
    except UniqueViolationError:
        await bot.send_message(message.from_user.id,
                               f"Agent {message.from_user.id} існує")
    else:
        await message.reply('Агента додано')

@dp.message_handler(text="Маршрут")
async def show_route(message: types.Message):
    await message.reply(reply_markup=route_kb)



