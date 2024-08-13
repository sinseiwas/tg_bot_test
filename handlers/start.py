from aiogram import Router, types
from aiogram.filters import Command
from keyboards.menu import *


router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = get_menu_keyboard()
    await message.answer(
        'Приветственное сообщение',
        reply_markup=builder.as_markup(resize_keyboard=True)
        )

