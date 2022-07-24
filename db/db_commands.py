from models import Agent


async def add_agent(**kwargs):
    new_agent = await Agent(**kwargs).create()
    return new_agent