from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_menu_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="Пройти тест по самоопределению"))
    builder.adjust(1)

    return builder