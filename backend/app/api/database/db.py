import asyncpg
import os

DATABASE_URL = os.getenv("DATABASE_URL")

pool = None


async def connect_to_db():
    global pool
    pool = await asyncpg.create_pool(DATABASE_URL)


async def close_db():
    global pool
    await pool.close()


async def get_connection():
    async with pool.acquire() as connection:
        yield connection
