from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery

from keybords.reply_keybords import menu
from load_bot import dp


@dp.message_handler(text="/start")
async def start(message: types.Message):
    text = message.text
    await message.answer(text, reply_markup=menu)


def get_agent_kb():
    buttons = [
        types.InlineKeyboardButton(text="Додати агента", callback_data="add_agent")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


@dp.message_handler(text="Агент")
async def start(message: types.Message):
    text = message.text
    await message.answer(text, reply_markup=get_agent_kb())


@dp.callback_query_handler(Text(startswith="add_agent"))
async def add_agent(call: types.CallbackQuery):
    id_agent = call.from_user.id
    name_agent = call.from_user.full_name
    await call.message.answer(f"{id_agent}, {name_agent}")

@dp.message_handler()