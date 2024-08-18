from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.media_group import MediaGroupBuilder
from aiogram.types import Message
from aiogram.enums import ParseMode
from typing import Dict, List
from aiogram import Bot, Dispatcher
from aiogram.exceptions import TelegramRetryAfter


from dotenv import load_dotenv
import os
import asyncio

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

def generate_keyboard(
    btn_text: str = None,
    btn_url: str = None
) -> InlineKeyboardMarkup | None:
    btn_builder = InlineKeyboardBuilder()
    btn_builder.row(
        InlineKeyboardButton(
            text=btn_text,
            url=btn_url
        )
    )
    return btn_builder.as_markup()


async def send_preview_with_keyboard(
    message: Message,
    photo: str = None,
    text: str = '',
    btn_text: str = None,
    btn_url: str = None
) -> int:
    keyboard = generate_keyboard(btn_text, btn_url)
    logging.info(f"Отправка сообщения: текст={text}, фото={photo}, клавиатура={keyboard}, режим={ParseMode.MARKDOWN_V2}")
    sent_message = await message.answer_photo(caption=text, photo=photo, reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN_V2)
    return sent_message.message_id



async def send_preview(
    message: Message,
    data: Dict
) -> int:
    message_id = await send_preview_with_keyboard(
        message,
        data['msg_photo'],
        data['msg_text'],
        data['btn_text'],
        data['btn_url']
    )
    return message_id


async def send_mail(
        bot: Bot,
        user_id: int,
        from_chat_id: int,
        message_id: int,
        keyboard: InlineKeyboardMarkup = None) -> bool:
    try:
        await bot.copy_message(chat_id=user_id, from_chat_id=from_chat_id, message_id=message_id, reply_markup=keyboard)
    except TelegramRetryAfter as e:
        await asyncio.sleep(e.retry_after)
        return await send_mail(bot, user_id, from_chat_id, message_id, keyboard)
    else:
        return True


import logging

async def start_sender(
    bot: Bot,
    data: Dict,
    user_ids: List[str],
    from_chat_id: int,
    message_id: int
) -> int:
    logging.info("Функция start_sender начата")
    count = 0
    keyboard = generate_keyboard(data['btn_text'], data['btn_url'])
    logging.info(f"Генерация клавиатуры завершена: {keyboard}")
    
    for u_id in user_ids:
        logging.info(f"Отправка сообщения пользователю: {u_id}")
        if await send_mail(bot, u_id, from_chat_id, message_id, keyboard):
            count += 1
            logging.info(f"Сообщение успешно отправлено пользователю: {u_id}")
        await asyncio.sleep(0.005)
    
    logging.info(f"Всего отправлено сообщений: {count}")
    return count

