from create_bot import dp, bot
from aiogram import types


@dp.message_handler(text="/start")
async def start(message: types.Message):
    chat_id = message.chat.id
    text = message.text
    await bot.send_message(chat_id=chat_id, text=text)
    await message.answer(text)
