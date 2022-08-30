from aiogram import types
from aiogram.dispatcher.filters import Text

from load_bot import dp


@dp.callback_query_handler(Text(startswith="data_agent"))
async def delete_agent(call: types.CallbackQuery):
    name_agent = call.from_user.full_name
    id_agent = call.from_user.id
    await call.message.answer(f"Ім'я {name_agent}\n"
                              f"ID {id_agent}")
    await call.answer()
