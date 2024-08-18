from aiogram import Router, types
from aiogram.filters import Command
# from keyboards.menu import *


import database.requests as rq


router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    # builder = get_menu_keyboard()
    await rq.set_user(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)
    await message.answer(
        'Приветственное сообщение',
        )


