''' 
bot/utils/database/postgresql.py
The database handler module.

Uses Asyncpg for postgresql
Database interactions
'''

import asyncio
from loguru import logger
from typing import Any

import sqlalchemy


from .. import configDB

test=False

class Database:
    uri: str
    
    @classmethod
    async def Connect(cls) -> None:
        pass
    
    @classmethod
    async def Disconnect(cls) -> None:
        pass

    @classmethod
    async def testCon(cls) -> None:
        pass


    @classmethod
    async def getClient(cls) -> None:
        #return cls.client
        pass

    @classmethod
    async def reInit(cls) -> None:
        pass


    @classmethod
    async def testSuite(cls) -> None:
        await cls.Connect()
        await cls.testCon()


if test:
    asyncio.run(Database.testSuite())
