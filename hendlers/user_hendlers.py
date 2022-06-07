import asyncpg.exceptions
from aiogram import types
from aiogram.dispatcher.filters import Command
from keybords.reply_keybords import menu
from create_bot import dp, db


@dp.message_handler(Command("start"))
async def start(message: types.Message):
    await message.answer('HI AGENT', reply_markup=menu)


@dp.message_handler(text="ROUT")
async def rout(message: types.Message):
    await message.answer(f'{message.from_user.id}')
    await db.add_agent(
        full_name=message.from_user.full_name,
        telegram_id=message.from_user.id
    )

    await message.answer(f"HI Agent, {message.from_user.full_name}!")
