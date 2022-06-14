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
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        telegram_id BIGINT NOT NULL UNIQUE
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_route_sheet(self):
        sql = """
        CREATE TABLE IF NOT EXISTS route_sheet (
        date DATE DEFAULT NOW(),
        initial_readings INT,
        final_readings INT
        );
        """
        await self.execute(sql, execute=True)

    async def add_route(self, initial_readings, final_readings):
        sql = "INSERT INTO route_sheet(initial_readings, final_readings) VALUES($1, $2)"
        return await self.execute(sql, initial_readings, final_readings, execute=True)


    async def add_agent(self, full_name, telegram_id):
        sql = "INSERT INTO agent(full_name, telegram_id) VALUES($1, $2)"
        return await self.execute(sql, full_name, telegram_id, execute=True)

    async def select_all_agents(self):
        sql = "SELECT * FROM agent"
        return await self.execute(sql, fetch=True)
