import asyncio
from .environment import Config

Config.loadConfig()

configBOT: Config.Bot = Config.Bot()
configDB: Config.Database = Config.Database()
configGIT: Config.Git = Config.Git()
configMESSAGE: Config.Message = Config.Message()
configVERSION: Config.Version = Config.Version()

from .database.database import Database

asyncio.run(Database.connect())
