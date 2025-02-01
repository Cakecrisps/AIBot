from aiogram import types
from aiogram.dispatcher import Dispatcher
from app.utils.keyboards import channel_subscribe_keyboard,choise_model_keyboard
from app.services.channel_service import ChannelService
from app.utils.config import API_TOKEN,CHANNEL_URL,CHANNEL_ID
from app.services.database_sevice import AsyncDatabase
from aiogram import Bot

bot = Bot(token=API_TOKEN)
channel_service = ChannelService(bot)
db = AsyncDatabase()

async def start_command(message: types.Message):
    await db.connect()
    user = message.from_user
    await db.add_user(user.first_name,user.id,"start","llm")
    
    is_subscribed = await channel_service.is_user_subscribed(CHANNEL_ID, user)
    
    if is_subscribed:
        await message.reply("Привет! Нажми на кнопку:", reply_markup=channel_subscribe_keyboard)
    else:
        await message.reply(f"Вы не подписаны на канал!{CHANNEL_URL}", reply_markup=None)

async def help_command(message: types.Message):
    await message.answer("Это помощь!\nИспользуйте /start для начала.")

def setup_command_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(help_command, commands=['help'])