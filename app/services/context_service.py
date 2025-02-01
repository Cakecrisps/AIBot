import os
import json
from ..utils.config import USER_FOLDER

class ContextManager:
    def __init__(self,user_id: int):
        self.file_path = USER_FOLDER.replace("?",str(user_id))

    def load_context(self) -> list[dict]:
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, 'r') as file:
            data = json.load(file)
            return data.get('context', [])

    def save_context(self, context: list[dict]) -> None:
        data = {'context': context}
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def add_to_context(self, item: dict) -> bool:
        context = self.load_context()
        if len(context) < 3:
            context.append(item)
        else:
            context.pop(0)  # Удаляем первый элемент
            context.append(item)
        self.save_context(context)
        return True
