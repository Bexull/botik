from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove,InlineKeyboardButton,InlineKeyboardMarkup

keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
							   one_time_keyboard=False) #скрывает клаву после нажатия
b_help = KeyboardButton('/help')
b_start = KeyboardButton('/Medeu')
b_location = KeyboardButton('/Random')
b_picture = KeyboardButton('/picture')
keyboard.add(b_help).insert(b_start).add(b_location).insert(b_picture)

ikb = InlineKeyboardMarkup(row_width=2)
ib = InlineKeyboardButton(text="Button1",
						  url="https://ru.pinterest.com/")
ib2 = InlineKeyboardButton(text="Button2",
						  url="https://ru.pinterest.com/")
ib3 = InlineKeyboardButton(text="Button3",
						  url="https://ru.pinterest.com/")

ikb2 = InlineKeyboardMarkup(row_width=2)
ib_1 = InlineKeyboardButton(text="Like",
                           callback_data="like")
ib_2 = InlineKeyboardButton(text="Dislike",
                           callback_data="Dislike")
ib_3 = InlineKeyboardButton(text="Next Photo",
                           callback_data="Next")
ikb2.add(ib_1, ib_2).add(ib_3)

ikb.add(ib).insert(ib2).add(ib3)

kb_medeu = ReplyKeyboardMarkup(resize_keyboard=True)
bm1 = KeyboardButton("Info")
bm2 = KeyboardButton("LifeHacks")
bm3 = KeyboardButton("Menu")
kb_medeu.add(bm1, bm2).add(bm3)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
bp1 = KeyboardButton("Random")
bp2 = KeyboardButton("Menu")
kb.add(bp1,bp2)