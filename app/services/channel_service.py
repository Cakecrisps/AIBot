from aiogram import Bot
from aiogram.types import User

class ChannelService:
    def __init__(self, bot: Bot):
        self.bot = bot

    async def is_user_subscribed(self, channel_id: str, user_id: int) -> bool:
        try:
            member = await self.bot.get_chat_member(chat_id=channel_id, user_id=user_id)
            # Проверяем статус участника
            if member.status in ['member', 'creator', 'administrator']:
                return True
            else:
                return False
        except Exception as e:
            print(f"Error checking subscription: {e}")
            return False