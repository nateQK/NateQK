import asyncio
from .environment import Config

Config.loadConfig()

configBOT: Config.Bot = Config.Bot()
configDB: Config.Database = Config.Database()

from .database import Database

asyncio.run(Database.Connect())
