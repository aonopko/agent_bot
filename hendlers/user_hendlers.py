from asyncpg.exceptions import UniqueViolationError
from aiogram import types
from aiogram.dispatcher.filters import Command
from keybords.reply_keybords import menu
from create_bot import dp, db, bot


@dp.message_handler(Command("start"))
async def start(message: types.Message):
    await message.answer('HI AGENT', reply_markup=menu)


@dp.message_handler(text="add agent")
async def new_agent(message: types.Message):
    try:
        await db.add_agent(
            full_name=message.from_user.full_name,
            telegram_id=message.from_user.id)
    except UniqueViolationError:
        await bot.send_message(message.from_user.id,
                               f"Agent {message.from_user.id} exists ")
    else:
        await message.reply('Agent is add')




@dp.message_handler(text="add route")
async def new_rout(message: types.Message):
    initial_readings = message.text
    final_readings = message.text
    try:
        await db.add_route(
            initial_readings=initial_readings,
            final_readings=final_readings)
    except UniqueViolationError:
        await bot.send_message(message.from_user.id,
                               f"Agent {message.from_user.id} exists ")
    else:
        await message.reply('route is add')

