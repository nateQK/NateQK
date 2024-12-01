''' 
bot/utils/database/postgresql.py
The database handler module.

Contains:
Database interactions
Connection Info

'''

from loguru import logger
from typing import TypedDict
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncSession, async_sessionmaker


from .. import configDB

test=False

class DBInfo(TypedDict):
    database: str
    driver: str


class DBTypes():
    postgresql: DBInfo = {"database": "postgresql", "driver": "asyncpg"}
    mysql: DBInfo = {"database": "mysql", "driver": "aiomysql"}
    mariadb: DBInfo = {"database": "mysql", "driver": "aiomysql"}
    #sqlite: DBInfo = {"database": "sqlite", "driver": "aiosqlite"} # NOTE: I'm not implementing this logic rn. not enough time



class Database:
    uri: str
    engine: AsyncEngine
    engineType: DBInfo
    failedConnectionEvents: int
    
    @classmethod
    async def connect(cls) -> AsyncEngine:
        try:
            cls.engineType = getattr(DBTypes, configDB.getEngine())
           # logger.debug(f"""
           #             Username: {configDB.getUsername()}
           #             Password: {configDB.getPassword()}
           #             Host: {configDB.getHost()}
           #             Database: {configDB.getDatabase()}
           #             Engine Info: {cls.engineType}
           #     """)
            cls.engine = create_async_engine(
                f"{cls.engineType['database']}+{cls.engineType['driver']}://{configDB.getUsername()}:{configDB.getPassword()}@{configDB.getHost()}/{configDB.getDatabase()}",
                pool_size=20,
                max_overflow=40,
                pool_timeout=30,
                pool_recycle=1800
            )
            cls.session = async_sessionmaker(cls.engine, class_=AsyncSession, expire_on_commit=False)

        except Exception as e:
            logger.error("Failed to connect to the database!")
            logger.error(e)

        return cls.engine




    @classmethod
    async def disconnect(cls) -> int:
        try:
            await cls.engine.dispose()
            return 1
        except Exception as _e:
            logger.error(f"Failed to dispose of database connection: {_e}")
            return 0


    @classmethod
    async def testCon(cls) -> int:
        try:
            async with cls.engine.connect() as _connection:
                return 0
        except Exception as e:
            print("Connection failed:", str(e))
            return 1

    @classmethod
    async def reconnect(cls) -> int:
        try:
            await cls.disconnect()
            await cls.connect()
            return 1
        except Exception as e:
            logger.error(e)
            return 0

