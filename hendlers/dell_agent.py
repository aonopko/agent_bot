from aiogram import types
from aiogram.dispatcher.filters import Text

from load_bot import dp
from db.db_commands import del_agent


@dp.callback_query_handler(Text(startswith="del_agent"))
async def delete_agent(call: types.CallbackQuery):
    id_agent = call.from_user.id
    try:
        await del_agent(agent_id=id_agent)
        await call.answer(f"Удаляем{id_agent}")
    except AttributeError:
        await call.answer(f"id{id_agent} вже був видалений")
