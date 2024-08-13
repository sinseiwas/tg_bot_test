from aiogram import Bot, Dispatcher, Router, types, F
from keyboards.test_keyboards import *
from bot import BOT_TOKEN
import asyncio

router = Router()
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


questions = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10']


@router.message(F.text=="Пройти тест по самоопределению")
async def if_start_test(message: types.Message):
    await message.answer(
        'Начать прохождение теста по самоопределению?',
        reply_markup=get_if_start_test_keyboard()
    )


@router.callback_query(F.data == 'yes')
async def process_callback_button(callback_query: types.CallbackQuery):
    for i in range(10):
        await bot.edit_message_text(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            text=questions[i],
            reply_markup=get_answers_for_question(i)
        )
    await callback.answer()