import asyncio
from .environment import Config

Config.loadConfig()

configBOT: Config.Bot = Config.Bot()
configDB: Config.Database = Config.Database()
configVERSION: Config.Version = Config.Version()
configMESSAGE: Config.Message = Config.Message()

from .database.database import Database

asyncio.run(Database.connect())
