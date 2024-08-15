from aiogram import Bot, Dispatcher, Router, types, F
from keyboards.test_keyboards import *
from bot import BOT_TOKEN
import asyncio
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from handlers.test_processing import user_answer_processing
from aiogram.types import ReplyKeyboardRemove


router = Router()
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


questions = [
    'Вопрос 1: выберите самый подходящий вам род деятельности', 
    'Вопрос 2: Выберите самый подходящий вам род деятельности', 
    'Вопрос 3: Выберите самый подходящий вам род деятельности', 
    'Вопрос 4: Выберите самый подходящий вам род деятельности', 
    'Вопрос 5: Выберите самый подходящий вам род деятельности', 
    'Вопрос 6: Выберите самый подходящий вам род деятельности', 
    'Вопрос 7: Выберите самый подходящий вам род деятельности', 
    'Вопрос 8: Выберите самый подходящий вам род деятельности', 
    'Вопрос 9: Выберите самый подходящий вам род деятельности', 
    'Вопрос 10: Выберите самый подходящий вам род деятельности',
]


@router.message(F.text=="Пройти тест по самоопределению")
async def if_start_test(message: types.Message):
    await message.answer(
        'Начать прохождение теста по самоопределению?',
        reply_markup=get_if_start_test_keyboard()
    )


@router.callback_query(F.data == 'yes')
async def process_callback_button(callback_query: types.CallbackQuery):


    reply_markup = ReplyKeyboardRemove()

    
    if callback_query.from_user.id in user_answers:
        del user_answers[callback_query.from_user.id]
    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        text=questions[0],
        reply_markup=get_answers_for_question(0),
    )



class TestStates(StatesGroup):
    question = State()  # Состояние для текущего вопроса
# Словарь для хранения ответов пользователей
user_answers = {}

# Обработчик для callback'ов
@router.callback_query(F.data.in_({'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}))
async def process_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id  # Получаем id пользователя

    # Если для данного пользователя еще нет массива, создаем его
    if user_id not in user_answers:
        user_answers[user_id] = ''

    # Получаем текущий вопрос
    data = await state.get_data()
    current_question = data.get("current_question", 0)

    # Обновляем ответ пользователя
    user_answer = callback_query.data
    user_answers[user_id] += user_answer
    print(user_answers)  # Для отладки, чтобы видеть ответы пользователей

    # Переходим к следующему вопросу
    next_question = current_question + 1

    # Если вопросы закончились, выводим сообщение с результатом
    if next_question >= len(questions):
        a, b, c, d, e, f = user_answer_processing(user_answers[user_id])
        await bot.edit_message_text(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            text=f"Три самые популярные категории: {a}, {b}, {c}\nТри категории, к которым стоит присмотреться: {d}, {e}, {f}"
        )
        await state.clear()  # Завершаем состояние

        # Можно обработать результаты и очистить массив ответов для данного пользователя
        del user_answers[user_id]
    else:
        # Сохраняем новый текущий вопрос
        await state.update_data(current_question=next_question)

        # Отправляем следующий вопрос
        await send_question(callback_query.message.chat.id, next_question)


# Функция для отправки вопроса
async def send_question(chat_id, question_index):
    await bot.send_message(
        chat_id=chat_id,
        text=questions[question_index],
        reply_markup=get_answers_for_question(question_index)   
    )

