import asyncio
from .environment import Config
from os import path
Config.loadConfig()

configBOT: Config.Bot = Config.Bot()
configDB: Config.Database = Config.Database()
configGIT: Config.Git = Config.Git()
configMESSAGE: Config.Message = Config.Message()
configVERSION: Config.Version = Config.Version()

from .database.database import Database

asyncio.run(Database.connect())


async def hourlyTasks():
    """A list of Tasks that need to run every hour"""
    from .github import download_directory, update_directory
    if not path.exists(configGIT.getLocalDir()):
        download_directory(configGIT.getRepo())

    else:
        update_directory()

