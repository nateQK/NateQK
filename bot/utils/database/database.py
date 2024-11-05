''' 
bot/utils/database/postgresql.py
The database handler module.

Contains:
Database interactions
Connection Info

'''

import asyncio
from loguru import logger
from typing import Any, TypedDict, Literal
from pydantic import BaseModel
import sqlalchemy
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine


from .. import configDB

test=False

class DBInfo(TypedDict):
    database: str
    driver: str


class DBTypes():
    postgresql: DBInfo = {"database": "postgresql", "driver": "asyncpg"}
    mysql: DBInfo = {"database": "mysql", "driver": "aiomysql"}
    mariadb: DBInfo = {"database": "mysql", "driver": "aiomysql"}
    sqlite: DBInfo = {"database": "sqlite", "driver": "aiosqlite"}



class Database:
    uri: str
    engine: AsyncEngine
    engineType: DBInfo
    failedConnectionEvents: int

    @classmethod
    async def connect(cls) -> None:
        try:
            cls.engineType = getattr(DBTypes, configDB.getEngine())
            logger.debug(f"""
                        Username: {configDB.getUsername()}
                        Password: {configDB.getPassword()}
                        Host: {configDB.getHost()}
                        Database: {configDB.getDatabase()}
                        Engine Info: {cls.engineType}
                """)
            cls.engine = create_async_engine(
                f"{cls.engineType['database']}+{cls.engineType['driver']}://{configDB.getUsername()}:{configDB.getPassword()}@{configDB.getHost()}/{configDB.getDatabase()}",
                pool_size=10,
                max_overflow=10,
                pool_timeout=30,
                pool_recycle=1800
            )

        except Exception as e:
            logger.error("Error Connecting to the Database")
            logger.error(e)

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
        await cls.connect()
        await cls.testCon()


if test:
    logger.info("Running Test Suite!")
    asyncio.run(Database.testSuite())
