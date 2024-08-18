from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states.base import CreateMessage
from aiogram import types

async def create_sender_handler(message: types.Message, state: FSMContext) -> None:
    await message.answer('*Создание рассылки!*\n\nНиже отправьте текст рассылки', parse_mode=ParseMode.MARKDOWN)
    await state.set_state(CreateMessage.get_text)
    