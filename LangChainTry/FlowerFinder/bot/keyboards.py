from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_main_keyboard():
    """ Клавиатура для основных команд """
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(
        KeyboardButton("🔍 Ввести описание цветка"),
        KeyboardButton("ℹ️ Помощь")
    )
    return keyboard
