from telegram import (
    ReplyKeyboardMarkup, KeyboardButton,
)


def get_gender_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [[
        KeyboardButton(text="Erkak"),
        KeyboardButton(text="Ayol")
    ]]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
