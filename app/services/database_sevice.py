import os
import asyncpg
from ..utils.config import DATABASE_URL

class AsyncDatabase:
    def __init__(self):
        self.pool = None

    async def connect(self) -> None:
        try:
            # Создаем пул соединений
            self.pool = await asyncpg.create_pool(DATABASE_URL)
            print("Connection to database successful")
        except Exception as e:
            print(f"Error connecting to database: {e}")
            raise

    async def close(self) -> None:
        if self.pool:
            await self.pool.close()
            print("Database connection closed")

    async def add_user(self, username: str, user_id: int, sub_status: str, current_mod: str) -> None:
        try:
            # Проверяем наличие пользователя
            existing_user = await self.get_user(user_id)
            if existing_user:
                raise ValueError(f"User with ID {user_id} already exists")

            async with self.pool.acquire() as connection:
                query = "INSERT INTO users (username, user_id, sub_status, current_mod) VALUES ($1, $2, $3, $4)"
                await connection.execute(query, username, user_id, sub_status, current_mod)
                print(f"User {user_id} added successfully")
        except Exception as e:
            print(f"Error adding user: {e}")
            raise

    async def delete_user(self, user_id: int) -> None:
        try:
            async with self.pool.acquire() as connection:
                query = "DELETE FROM users WHERE user_id = $1"
                await connection.execute(query, user_id)
                print(f"User {user_id} deleted successfully")
        except Exception as e:
            print(f"Error deleting user: {e}")
            raise

    async def update_sub_status(self, user_id: int, new_sub_status: bool) -> None:
        try:
            async with self.pool.acquire() as connection:
                query = "UPDATE users SET sub_status = $1 WHERE user_id = $2"
                await connection.execute(query, new_sub_status, user_id)
                print(f"Sub status of user {user_id} updated to {new_sub_status}")
        except Exception as e:
            print(f"Error updating sub status: {e}")
            raise

    async def update_current_mod(self, user_id: int, new_current_mod: str) -> None:
        try:
            async with self.pool.acquire() as connection:
                query = "UPDATE users SET current_mod = $1 WHERE user_id = $2"
                await connection.execute(query, new_current_mod, user_id)
                print(f"Current mod of user {user_id} updated to {new_current_mod}")
        except Exception as e:
            print(f"Error updating current mod: {e}")
            raise

    async def get_user(self, user_id: int):
        try:
            async with self.pool.acquire() as connection:
                query = "SELECT * FROM users WHERE user_id = $1"
                return await connection.fetchrow(query, user_id)
        except Exception as e:
            print(f"Error getting user: {e}")
            raise