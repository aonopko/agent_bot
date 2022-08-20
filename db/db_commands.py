from aiogram import types
from asyncpg import UniqueViolationError
from .models import Agent


async def add_agent(agent_id, agent_name):
    try:
        agent = Agent(id_agent=agent_id, name_agent=agent_name)
        await agent.create()

    except UniqueViolationError:
        pass
