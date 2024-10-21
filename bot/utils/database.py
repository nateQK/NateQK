''' The database handler module. '''
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
from loguru import logger
from . import configDB

class Database:
    
    @classmethod
    async def Connect(cls):
        cls.uri = f"mongodb://{configDB.getUsername}:{configDB.getPassword}@{configDB.getHost}:{configDB.getPort}/?authSource=admin"
        cls.client = AsyncIOMotorClient(cls.uri, server_api=ServerApi("1"))

    @classmethod
    async def Disconnect(cls):
        pass

    @classmethod
    async def testCon(cls):
        try:
            await cls.client.admin.command('ping')
        except Exception as e:
            logger.error(e)
            exit(1)



    @classmethod
    async def getClient(cls):
        return cls.client

    @classmethod
    async def reInit(cls):
        pass
    
    @classmethod
    async def testSuite(cls):
        await cls.Connect()
        await cls.testCon()



if __name__ == "__main__":
    asyncio.run(Database.testSuite())
