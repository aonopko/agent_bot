from aiogram.dispatcher.filters.state import StatesGroup, State


class AgentState(StatesGroup):
    id_agent = State()
    agent_name = State()

