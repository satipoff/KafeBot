from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Menuni ko'rish"),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)