from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_main_keyboard():
    """ Клавиатура для основных команд """
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("/start"))
    keyboard.add(KeyboardButton("/help"))
    keyboard.add(KeyboardButton("/enter_description"))
    keyboard.add(KeyboardButton("/history"))
    keyboard.add(KeyboardButton("/clear"))
    keyboard.add(KeyboardButton("/not_found"))
    return keyboard
