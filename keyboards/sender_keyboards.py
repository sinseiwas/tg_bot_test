from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_keyboard_confirm():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Отправить сейчас", callback_data="start_send"),
        InlineKeyboardButton(text="Отменить", callback_data="cancel")
    )

    return builder