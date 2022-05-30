from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from var_for_db import DB_NAME, DB_PASSWORD, DB_USER, DB_HOST


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
