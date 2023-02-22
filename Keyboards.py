from aiogram import types

main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True).add('/top-100', '/movies')
url_kb = types.InlineKeyboardMarkup(row_width=2).add(*[types.InlineKeyboardButton(text=str(i),
                                    callback_data=f"page_{i}") for i in range(11)])
