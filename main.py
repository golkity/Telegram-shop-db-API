import logging
import os
import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from app.handlers import router
from app.database.models import async_main
load_dotenv("app/.env")


async def main():
    await async_main()
    bot = Bot(token=os.getenv("TOKEN"))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        # logging.basicConfig(level=logging.DEBUG if True else logging.INFO)
        asyncio.run(main())
        print('Bot ofline')
    except KeyboardInterrupt:
        print("Bot ofline")
