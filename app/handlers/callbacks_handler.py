from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton,CallbackQuery
from aiogram import Bot
from ..services.database_sevice import AsyncDatabase
from ..services.channel_service import ChannelService
from aiogram.dispatcher import Dispatcher
from ..utils.config import CHANNEL_ID,CHANNEL_URL,TELEGRAM_TOKEN
from ..utils.keyboards import *

bot = Bot(token=TELEGRAM_TOKEN)
channel_service = ChannelService(bot)

class CallbackService:

    async def __init__(self, callback_query: CallbackQuery, bot: Bot):

        self.callback_query= callback_query
        self.db = AsyncDatabase()
        self.bot = bot
        self.status = channel_service.is_user_subscribed(CHANNEL_ID,callback_query.from_user.id)

    async def solve(self) -> None:

        data = self.callback_query.data
        user_id = self.callback_query.from_user.id

        #chech sub on the channel
        if not self.status:
            await self.bot.send_message(user_id,f"Подпишитесь на канал.{CHANNEL_URL}",reply_markup=channel_subscribe_keyboard)
            return
        

        #create bd connection
        await self.db.connect() 

        try:
            
            #model swtich button
            if "switch" in data:

                model = data.replace("switch-","")
                await self.db.update_current_mod(user_id,model)
                await self.db.close()
                await self.bot.send_message(user_id,"Успешная смена модели!))Поробуйте пообщаться |>-<|")
                return
            
        except Exception as e:

            await self.bot.send_message(user_id,"У нас ошибка!! -  {e} - смена модели - 20 - CH")
            return
        
        try:
            
            #check sub button
            if data == "check_sub":

                if self.status:

                    await self.bot.send_message(user_id,"Успешная проверка.Выберите модель",reply_markup=choise_model_keyboard)
                    return
                
                else: 

                    await self.bot.send_message(user_id,f"Подпишитесь на канал.{CHANNEL_URL}",reply_markup=channel_subscribe_keyboard)
                    return

        except Exception as e:

            await self.bot.send_message(user_id,"У нас ошибка!! -  {e} - смена модели - 25 - CH")
            return

async def handle_callback_query(callback_query: CallbackQuery):
    callback_service = CallbackService(callback_query,bot)
    await callback_service.solve()
    
def setup_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(handle_callback_query)




    
    
    


