import asyncio
from aiogram import Bot, Dispatcher
from questions import router

async def main():
    bot = Bot(token=open("token").readline(), parse_mode="HTML")

    dp = Dispatcher()
    dp.include_routers(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    loop.create_task(main())

    loop.run_forever()