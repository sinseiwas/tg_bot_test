from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import F
from aiogram import types

from states.base import CreateMessage
from utils import sender
from keyboards.sender_keyboards import get_keyboard_confirm



router = Router()


@router.message(CreateMessage.get_text, F.text)
async def set_text_handler(message: types.Message, state: FSMContext):
    await state.update_data(msg_text=message.md_text)
    await message.answer(
        text='Отлично, теперь отправьте фото'
    )
    await state.set_state(CreateMessage.get_photo)


@router.message(CreateMessage.get_photo, F.photo)
async def set_photo_handler(message: types.Message, state: FSMContext):
    await state.update_data(msg_photo=message.photo[-1].file_id)
    data = await state.get_data()
    await state.set_state(CreateMessage.get_keyboard_text)
    await message.answer(
        text='Введите текст кнопки'
    )


@router.message(CreateMessage.get_keyboard_text, F.text)
async def set_text_handler(message: types.Message, state: FSMContext):
    await state.update_data(btn_text=message.text)
    await state.set_state(CreateMessage.get_keyboard_url)
    await message.answer(
        text='Супер! Отправьте ссылку для кнопки:'
    )


@router.message(CreateMessage.get_keyboard_url, F.text)
async def set_btn_url_handler(message: types.Message, state: FSMContext):
    await state.update_data(btn_url=message.text)
    data = await state.get_data()
    message_id = await sender.send_preview(
        message,
        data
    )
    await state.update_data(message_id=message_id)
    await message.answer(
        text='*Сообщение для рассылки сформировано!*\n\nЧтобы начать, нажмите кнопку ниже',
        reply_markup=get_keyboard_confirm().as_markup(),
        parse_mode=ParseMode.MARKDOWN
    )
    await state.set_state(CreateMessage.confirm_sender)


