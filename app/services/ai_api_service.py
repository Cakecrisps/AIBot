# app/services/ai_api_service.py

from openai import OpenAI
import math

class AIAPIService:
    def __init__(self, base_url: str = 'http://localhost:11434/v1/', api_key: str = 'ollama'):
        self.client = OpenAI(base_url=base_url, api_key=api_key)

    def send_chat_message(self, content: str, model: str) -> str:
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    'role': 'user',
                    'content': content,
                }
            ],
            model=model,
        )
        return chat_completion.choices[0].message.content