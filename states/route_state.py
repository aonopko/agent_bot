from aiogram.dispatcher.filters.state import StatesGroup, State


class Agent(StatesGroup):
    id_agent = State()
    agent_name = State()
