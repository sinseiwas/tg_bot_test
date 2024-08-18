from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State


from keyboards.test_keyboards import *
from handlers.test_processing import user_answer_processing
from database.data import questions


from dotenv import load_dotenv
import os
import asyncio

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

router = Router()
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

#  Задаём вопрос, проходить ли тест, если он уже начат,
#  говорим закончить
@router.message(Command("test"))
async def if_start_test(message: types.Message):
    if message.from_user.id not in user_answers:
        await message.answer(
            'Начать прохождение теста по самоопределению?',
            reply_markup=get_if_start_test_keyboard()
        )
    else:
        await message.answer(
            'Завершите прохождение теста'
        )


#  Если ответ да, проверяем, есть ли полльзователь в прохождении,
#  да - удаляем и стартуем заново
@router.callback_query(F.data == 'yes')
async def process_callback_button(callback_query: types.CallbackQuery):
    if callback_query.from_user.id in user_answers:
        del user_answers[callback_query.from_user.id]

    # await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)

    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        text=questions[0],
        reply_markup=get_answers_for_question(0),
    )


@router.callback_query(F.data == 'no')
async def idk(callback_query: types.CallbackQuery):
    await callback_query.message.answer(
        'Не знаю, что тут должно быть'
    )

class TestStates(StatesGroup):
    question = State()  # Состояние для текущего вопроса
#  Словарь для хранения ответов пользователей
user_answers = {}

#  Обработчик для callback'ов
@router.callback_query(F.data.in_({'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}))
async def process_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id  # Получаем id пользователя

    #  Если для данного пользователя еще нет массива, создаем его
    if user_id not in user_answers:
        user_answers[user_id] = ''

    #  Обновляем ответ пользователя
    user_answer = callback_query.data
    user_answers[user_id] += user_answer
    print(user_answers)
    
    #  Переходим к следующему вопросу
    data = await state.get_data()
    current_question = data.get("current_question", 0)
    next_question = current_question + 1

    if next_question >= len(questions):
        #  Удаляем предыдущие кнопки
        await delete_buttons(callback_query.message.chat.id, callback_query.message.message_id)

        #  Получаем категории
        most_popular, least_popular = await user_answer_processing(user_answers[user_id])

        #  Формируем текст для вывода только если есть категории
        result_text = ""
        if most_popular:
            result_text += f"🚀 Самые популярные категории: {', '.join(most_popular)}\n"
        if least_popular:
            result_text += f"Категории, к которым стоит присмотреться: {', '.join(least_popular)}"

        #  Отправляем результат, если есть текст
        if result_text:
            await bot.send_message(
                chat_id=callback_query.message.chat.id,
                text=result_text
            )

        #  Завершаем состояние
        await state.clear()
        del user_answers[user_id]
    else:

        #  Удаляем предыдущие кнопки
        await delete_buttons(callback_query.message.chat.id, callback_query.message.message_id)

        await asyncio.sleep(0.3)
        
        #  Сохраняем новый текущий вопрос
        await state.update_data(current_question=next_question)

        #  Отправляем следующий вопрос
        await send_question(callback_query.message.chat.id, next_question)



#  Функция для отправки вопроса
async def send_question(chat_id, question_index):
    await bot.send_message(
        chat_id=chat_id,
        text=questions[question_index],
        reply_markup=get_answers_for_question(question_index)   
    )


async def delete_buttons(chat_id, message_id):
    await bot.edit_message_reply_markup(
            chat_id=chat_id,
            message_id=message_id,
            reply_markup=None
        )