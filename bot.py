from aiogram import Bot, Dispatcher
import asyncio
from handlers import start, test
from dotenv import load_dotenv
import os


load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_routers(start.router, test.router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())