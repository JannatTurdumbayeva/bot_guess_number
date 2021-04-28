from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_key = InlineKeyboardMarkup()
btn = InlineKeyboardButton('Yes', callback_data='yes')
btn1 = InlineKeyboardButton('No', callback_data='no')
inline_key.add(btn, btn1)