from typing import Union
import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool
from .var_for_db import DB_NAME, DB_PASSWORD, DB_USER, DB_HOST


class Database:

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            database=DB_NAME
        )

    """ The method by which we work with queries to the database(
        Метод с помощью которого мы работаем с запросами в базу данных)
    """

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False):
        """ According to the documentation, create a connection pool(
            согласно документации создаем пул соединений)
        """
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_agent(self):
        sql = """
        CREATE TABLE IF NOT EXISTS agent (
        full_name VARCHAR(255) NOT NULL,
        telegram_id  BIGINT UNIQUE
        );
            """
        await self.execute(sql, execute=True)

    async def create_table_route_sheet(self):
        sql = """
        CREATE TABLE IF NOT EXISTS route_sheet (
        id_agent BIGINT,
        date DATE DEFAULT NOW(),
        initial_readings BIGINT,
        final_readings BIGINT,
        difference_readings BIGINT
        );
        """
        await self.execute(sql, execute=True)
