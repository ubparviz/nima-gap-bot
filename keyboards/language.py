from telegram import ReplyKeyboardMarkup, KeyboardButton


def get_language_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text='Uzbek'), KeyboardButton(text='English')]
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        one_time_keyboard=True,
    )
