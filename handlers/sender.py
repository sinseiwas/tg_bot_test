from aiogram.filters import Command
from aiogram import Bot, Dispatcher, Router, types, F


from database.requests import get_tg_id


from dotenv import load_dotenv
import os
import asyncio
ADMIN = 890684152

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")


router = Router()
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@router.message(Command("send"))
async def send_all(message: types.Message):
    if message.from_user.id == ADMIN:
        users_tg_id = await get_tg_id()
        print(users_tg_id)
        for i in users_tg_id:
            await bot.send_message(i, ' '.join(message.text.split()[1:]))