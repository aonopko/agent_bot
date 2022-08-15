from aiogram import types
from .models import Agent


async def add_user(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    return (user_id, user_name)
