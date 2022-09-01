from aiogram import types
from aiogram.dispatcher.filters import Text

from load_bot import dp
from db.db_commands import show_data_agent


@dp.callback_query_handler(Text(startswith="data_agent"))
async def show_dat_agent(call: types.CallbackQuery):
    id_agent = call.from_user.id
    show_data = await show_data_agent(agent_id=id_agent)
    await call.message.answer(f"Ім'я {show_data}"
                              f"ID {id_agent}")
    await call.answer()
