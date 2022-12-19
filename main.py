import random
import aiogram
from aiogram import Bot, Dispatcher, executor, types,exceptions
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove,InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.dispatcher.filters import Text


TOKEN_API = "5452261343:AAGg0oo9vRZVpyPz6LUMBkyRHlNZ2grJw40"
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
bp1 = KeyboardButton("Random")
bp2 = KeyboardButton("Menu")
kb.add(bp1,bp2)

IKB = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text="Like",
                           callback_data="like")
ib2 = InlineKeyboardButton(text="Dislike",
                           callback_data="Dislike")
ib3 = InlineKeyboardButton(text="Next Photo",
                           callback_data="Next")
IKB.add(ib1,ib2).add(ib3)

HELP_COMMAND = """
/help - list of commands
/start - for starting Bot
/give - get some sticker
/picture - get some picture
"""
arr_photos = [
	"https://i.pinimg.com/564x/0c/6b/7b/0c6b7bfe44ec0d273ac086322feda6e5.jpg",
	"https://i.pinimg.com/564x/81/43/10/81431081318e973eb31c7e6c24276b17.jpg",
	"https://i.pinimg.com/564x/34/f3/07/34f307995dd40ce5370d37b9cd4ecc4f.jpg",
	"https://i.pinimg.com/564x/c4/51/af/c451af8fc8de69d2b5ce48eeff602522.jpg"
]

photos = dict(zip(arr_photos, ['1','2','3','4']))


keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
							   one_time_keyboard=False) #скрывает клаву после нажатия
b_help = KeyboardButton('/help')
b_start = KeyboardButton('/give')
b_location = KeyboardButton('/loc')
b_picture = KeyboardButton('/picture')
keyboard.add(b_help).insert(b_start).add(b_location).insert(b_picture)

ikb = InlineKeyboardMarkup(row_width=2)
ib = InlineKeyboardButton(text="Button1",
						  url="https://ru.pinterest.com/")
ib2 = InlineKeyboardButton(text="Button2",
						  url="https://ru.pinterest.com/")
ib3 = InlineKeyboardButton(text="Button3",
						  url="https://ru.pinterest.com/")

ikb.add(ib).insert(ib2).add(ib3)

async def on_startup(_):
	print('Bot was successfully started!')

async def send_random(message: types.Message):
	randomPhoto = random.choice(list(photos.keys()))
	await bot.send_photo(message.chat.id,
						 photo=randomPhoto,
						 caption=photos[randomPhoto],
						 reply_markup=IKB)


@dp.message_handler(commands=['start'])
async def start_cm(message:types.Message):
	await message.answer('<em>Wellcome to our Telegram Bot!</em>', parse_mode="HTML",
						 reply_markup=keyboard
						 )

@dp.message_handler(commands=['help'])
async def help(message:types.Message):
	await message.answer(HELP_COMMAND)

count = 0
rand = random.randint(-10,20)

@dp.message_handler(commands=['dick'])
async def help(message:types.Message):
	await message.answer(str(count + rand))

@dp.message_handler(commands=['give'])
async def start_cm(message:types.Message):
	await bot.send_sticker(message.chat.id,sticker= "CAACAgIAAxkBAAEG4Xdjn0CkTaL-WadR0Nean4tMbmulIAACbQ8AAvX64EopOdJWyR2ApywE")
	await bot.send_message(message.chat.id,text="LOL",reply_markup=ikb)
	await message.delete()

@dp.message_handler(commands=['loc'])
async def location(message: types.Message):
	await bot.send_location(chat_id=message.from_user.id,longitude=33,latitude=23)

@dp.message_handler(commands=['picture'])
async def pic(message: types.Message):
	ink = InlineKeyboardMarkup(row_width=2)
	ib = InlineKeyboardButton(text="❤️", callback_data="like")
	ib2 = InlineKeyboardButton(text="🤮", callback_data="dislike")
	ink.add(ib).insert(ib2)
	await bot.send_photo(message.chat.id,photo="https://i.pinimg.com/564x/e3/11/c5/e311c52b0f472ebe9883e6bad20ec504.jpg")
	await bot.send_message(message.chat.id,text="Do you like it?",reply_markup=ink)

@dp.message_handler(Text(equals="random_photo"))
async def random_photo(message: types.Message):

	await message.answer(text="Please choose button 'Random' ",
						 reply_markup=kb)

@dp.message_handler(Text(equals="Random"))
async def SendRandomPhoto(message: types.Message):
	await send_random(message)


@dp.message_handler(Text(equals="Menu"))
async def menu(message: types.Message):
	await message.answer(text="Wellcome to main Menu",
						 reply_markup=keyboard)
	await message.delete()

@dp.callback_query_handler()
async def callbackall(callback: types.CallbackQuery):
	if callback.data == "like":
		await callback.answer(text="You like it✨")
	if callback.data == "Like":
		await callback.answer(text="You like it✨")
	if callback.data == "Dislike":
		await callback.answer(text="You Dislike it ")
	if callback.data == "Next":
		await send_random(message=callback.message)


@dp.message_handler()
async def send_emoji(message: types.Message):
	if message.text == "thx":
		await message.reply("💗")




if __name__ == "__main__" :
	executor.start_polling(dp, skip_updates = True, on_startup=on_startup)


