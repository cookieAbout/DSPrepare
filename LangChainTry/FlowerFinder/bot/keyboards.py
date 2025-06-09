from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_main_keyboard():
    """ Клавиатура для основных команд """
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(
        # KeyboardButton("🔍 Ввести описание цветка"),
        KeyboardButton("ℹ️ Помощь"),
        KeyboardButton("Да, то что нужно!"),
        KeyboardButton("Не то"),
        KeyboardButton("Так и не нашел. Выйти."),
    )
    return keyboard
