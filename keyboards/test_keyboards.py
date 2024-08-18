from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


from database.data import answers 


def get_if_start_test_keyboard():
    buttons = [
        [
            InlineKeyboardButton(text="Да", callback_data="yes"),
            InlineKeyboardButton(text="Нет", callback_data="no")
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_answers_for_question(i):
    buttons = []

    for x in range(0, len(answers[i]), 2):
        buttons.append(
            [
            InlineKeyboardButton(text=answers[i][x], callback_data=str(x)),
            InlineKeyboardButton(text=answers[i][x + 1], callback_data=str(x + 1))
            ],
        )

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard