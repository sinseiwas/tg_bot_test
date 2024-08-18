from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from database.models import async_main

import asyncio


from handlers import start, test, sender


from dotenv import load_dotenv
import os


load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Начало"),
        BotCommand(command="help", description="Помощь"),
        BotCommand(command="test", description="Пройти тест 🧩"),
    ]
    await bot.set_my_commands(commands)


async def main():
    await async_main()
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    await set_commands(bot)
    dp.include_routers(start.router, test.router, sender.router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())