import time
from aiogram.enums import ParseMode
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from database.requests import get_tg_id
from keyboards.sender_keyboards import get_keyboard_confirm
from states.base import CreateMessage
from utils import sender
from bot import bot
from aiogram import Bot


async def cancel_sending(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text('Рассылка отменена')
    await state.clear()
    await callback.answer()


async def start_sending(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await callback.message.answer('Рассылка началась')
    await state.clear()
    await callback.answer()

    users_id = await get_tg_id()
    t_start = time.time()
    message_id = data.get('message_id')
    count = await sender.start_sender(
        bot=bot,
        data=data,
        user_ids=users_id,
        from_chat_id=callback.message.chat.id,
        message_id=message_id)
    await callback.message.answer(f'Отправлено {count} за {round(time.time() - t_start)}с')