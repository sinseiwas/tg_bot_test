from aiogram.filters import Command
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states.base import CreateMessage

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


@router.message(Command("sender"))
async def create_sender_handler(message: types.Message, state: FSMContext) -> None:
    if ADMIN == message.from_user.id:
        await message.answer('*Создание рассылки!*\n\nНиже отправьте текст рассылки', parse_mode=ParseMode.MARKDOWN)
        await state.set_state(CreateMessage.get_text)