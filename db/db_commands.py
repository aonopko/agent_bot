from models import Agent


async def add_user(user_id, user_name):
    new_user = await Agent(id=user_id, user_name=user_name).create()
    return new_user
