from telegram import (
    ReplyKeyboardMarkup, KeyboardButton,
)


def get_contact_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [[
        KeyboardButton(text="📞 Raqamni yuborish", request_contact=True)
    ]]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)

