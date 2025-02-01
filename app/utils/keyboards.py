
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

choise_model_keyboard = InlineKeyboardMarkup()
    
coder_button = InlineKeyboardButton(text='Код', callback_data='switch-coder')
math_button = InlineKeyboardButton(text='Математика', callback_data='switch-math')
llm_button = InlineKeyboardButton(text='Общая языковая модель', callback_data='switch-llm')

choise_model_keyboard.row(coder_button, math_button).row(llm_button)
channel_subscribe_keyboard = InlineKeyboardMarkup()
check_butt = InlineKeyboardButton(text='Проверить подписку', callback_data='check_sub')
channel_subscribe_keyboard.add(check_butt)