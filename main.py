import asyncio
import os
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
from dotenv import load_dotenv


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Send me any message or forward message...")


id_message = """message's id = {message_id}
your user_id = {user_id}
message's author id = {author_id}
forwarded from chat id = {chat_id}
"""


@dp.message()
async def get_id(message: Message):
    await message.answer(text=id_message.format(
        message_id=message.message_id, user_id=message.from_user.id, 
        author_id=message.forward_from.id if message.forward_from else "",
        chat_id=message.forward_from_chat.id if message.forward_from_chat else "",
    ))


async def main():
    await dp.start_polling(bot, allowed_updates=['*'], skip_updates=True, verify=False)


asyncio.run(main())
