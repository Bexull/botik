import logging
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode

API_TOKEN = '5594737774:AAElQb--m5R8lgJZ6tIvAY9eLlmN8CzeIbI'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Echo message handler
@dp.message_handler()
async def echo_message(message: types.Message):
    await message.answer(f"Вы написали: {md.quote(message.text)}", parse_mode=ParseMode.MARKDOWN)

# Start the bot
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
