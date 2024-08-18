from aiogram import Bot, Dispatcher, F
from aiogram.types import BotCommand
from database.models import async_main


from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command 
from handlers import commands, callbacks
from states.base import CreateMessage


from handlers import start, test, create_mail
from states import sender
from handlers.commands import create_sender_handler

from dotenv import load_dotenv
import os
import asyncio 
import logging 
import sys

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


def set_handlers():
    # dp.message.register(commands.create_sender_handler, Command(commands=['sender'])) 
    dp.callback_query.register(callbacks.cancel_sending, F.data == "cancel")
    dp.callback_query.register(callbacks.start_sending, F.data.startswith("start_send"), CreateMessage.confirm_sender)

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Начало"),
        BotCommand(command="help", description="Помощь"),
        BotCommand(command="test", description="Пройти тест 🧩"),
    ]
    await bot.set_my_commands(commands)


async def main():
    await async_main()


    await set_commands(bot)
    dp.include_routers(start.router, test.router, sender.router, create_mail.router)
    set_handlers()
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())