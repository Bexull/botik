import random
import aiogram

from aiogram import Bot, Dispatcher, executor, types,exceptions
from aiogram.dispatcher.filters import Text
from config import TOKEN_API
from Keyboard import keyboard, ikb, kb, ikb2 , kb_medeu

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

HELP_COMMAND = """
/help - list of commands
/start - for starting Bot
/Medeu - some information about Medeu(With lifeHacks)
/Random - get some random photos
"""
arr_photos = [
	"https://i.pinimg.com/564x/0c/6b/7b/0c6b7bfe44ec0d273ac086322feda6e5.jpg",
	"https://i.pinimg.com/564x/81/43/10/81431081318e973eb31c7e6c24276b17.jpg",
	"https://i.pinimg.com/564x/34/f3/07/34f307995dd40ce5370d37b9cd4ecc4f.jpg",
	"https://i.pinimg.com/564x/c4/51/af/c451af8fc8de69d2b5ce48eeff602522.jpg"
]

photos = dict(zip(arr_photos, ['1','2','3','4']))

arr_photos_lifehacks = [
	"https://i.pinimg.com/564x/23/75/43/2375438815779b591831965cb05e2676.jpg",
	"https://i.pinimg.com/564x/5f/02/8c/5f028c8da50ffa5f4e5d5ebf5ba9c63c.jpg",
	"https://i.pinimg.com/564x/72/ed/85/72ed857d648c0d4ced2e581bbc41c19f.jpg"
]
lifehack_photos = dict(zip(arr_photos_lifehacks,["Приходи в хорошем настроении!✨",
												 "Завяжи коньки покрепче, чтобы он фиксировал голеностоп, верхние(последние 3-4) люверсы затяни туже чем предыдушие, но не переборщи😅",
												 f"Можно купить шнурки с пропиткой, они лучше держат шнуровку, но тяжело расшнуровать"]))

async def on_startup(_):
	print('Bot was successfully started!')

async def send_random(message: types.Message):
	randomPhoto = random.choice(list(photos.keys()))
	await bot.send_photo(message.chat.id,
						 photo=randomPhoto,
						 caption=photos[randomPhoto],
						 reply_markup=ikb2)


@dp.message_handler(commands=['start'])
async def start_cm(message:types.Message):
	await message.answer('<em>Wellcome to our Telegram Bot!</em>',
						 parse_mode="HTML",
						 reply_markup=keyboard)

@dp.message_handler(commands=['help'])
async def help(message:types.Message):
	await message.answer(HELP_COMMAND)

@dp.message_handler(commands=['Medeu'])
async def Medeu(message:types.Message):
	await message.answer(text="Medeu",reply_markup=kb_medeu)

@dp.message_handler(Text(equals="Info"))
async def infoMedeu(message: types.Message):
	await message.answer(text="Высокогорный каток медеу\n"
							  "2Gis ссылка: https://go.2gis.com/hx27s"
							  )
	await message.delete()
@dp.message_handler(Text(equals="LifeHacks"))
async def lifehack(message: types.Message):
	random_lifehack = random.choice(list(lifehack_photos.keys()))
	await bot.send_photo(message.chat.id,
						 photo=random_lifehack,
						 caption=lifehack_photos[random_lifehack])
	await message.delete()
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
	executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


