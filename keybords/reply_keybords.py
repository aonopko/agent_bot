from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='add agent'),
            KeyboardButton(text='add route')
        ]
    ],
    resize_keyboard=True
)