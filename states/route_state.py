from aiogram.dispatcher.filters.state import StatesGroup, State


class Route(StatesGroup):
    initial_readings = State()
    final_readings = State()
