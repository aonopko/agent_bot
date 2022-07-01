from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Додати агента'),
            KeyboardButton(text='Додати маршрут')
        ]
    ],
    resize_keyboard=True
)