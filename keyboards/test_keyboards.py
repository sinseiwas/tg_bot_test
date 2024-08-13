from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_if_start_test_keyboard():
    buttons = [
        [
            InlineKeyboardButton(text="Да", callback_data="yes"),
            InlineKeyboardButton(text="Нет", callback_data="no")
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


ans = [
    ['ans1', 'ans2', 'ans3', 'ans4', 'ans5', 'ans6', 'ans7', 'ans8', 'ans9', 'ans10'],
    ['ans1', 'ans2', 'ans3', 'ans4', 'ans5', 'ans6', 'ans7', 'ans8', 'ans9', 'ans10'],
    ['ans1', 'ans2', 'ans3', 'ans4', 'ans5', 'ans6', 'ans7', 'ans8', 'ans9', 'ans10'],
    ['ans1', 'ans2', 'ans3', 'ans4', 'ans5', 'ans6', 'ans7', 'ans8', 'ans9', 'ans10'],
    ['ans1', 'ans2', 'ans3', 'ans4', 'ans5', 'ans6', 'ans7', 'ans8', 'ans9', 'ans10'],
    ['ans1', 'ans2', 'ans3', 'ans4', 'ans5', 'ans6', 'ans7', 'ans8', 'ans9', 'ans10'],
    ['ans1', 'ans2', 'ans3', 'ans4', 'ans5', 'ans6', 'ans7', 'ans8', 'ans9', 'ans10'],
    ['ans1', 'ans2', 'ans3', 'ans4', 'ans5', 'ans6', 'ans7', 'ans8', 'ans9', 'ans10'],
    ['ans1', 'ans2', 'ans3', 'ans4', 'ans5', 'ans6', 'ans7', 'ans8', 'ans9', 'ans10'],
    ['ans1', 'ans2', 'ans3', 'ans4', 'ans5', 'ans6', 'ans7', 'ans8', 'ans9', 'ans10'],
]


def get_answers_for_question(i):
    buttons = [
        [
            InlineKeyboardButton(text=ans[i][0], callback_data="1"),
            InlineKeyboardButton(text=ans[i][1], callback_data="2")
        ],
        [
            InlineKeyboardButton(text=ans[i][2], callback_data="3"),
            InlineKeyboardButton(text=ans[i][3], callback_data="4")
        ],
        [
            InlineKeyboardButton(text=ans[i][4], callback_data="5"),
            InlineKeyboardButton(text=ans[i][5], callback_data="6")
        ],
        [
            InlineKeyboardButton(text=ans[i][6], callback_data="7"),
            InlineKeyboardButton(text=ans[i][7], callback_data="8")
        ],
        [
            InlineKeyboardButton(text=ans[i][8], callback_data="9"),
            InlineKeyboardButton(text=ans[i][9], callback_data="10")
        ]
    ]

    
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard