'''Config and Other globablly usable variables module.'''
import tomllib
from os import path
from loguru import logger
from munch import munchify

class Config:
    @classmethod
    def loadConfig(cls):
        # """Loads, Fetches, and Validates config from a pre-determined file"""

        configfile = path.join("bot", "app.toml")


        with open(configfile, 'rb') as file:
            config = tomllib.load(file)
            #config = dumps(config)
            cls.config = munchify(config)

    class Database:
        def __init__(self):
            pass

        def getHost(self) -> str:
            """Fetches values of host from config"""
            return Config.config.DATABASE.host # type: ignore

        @property
        def getPort(self):
            """Fetches values of port from config"""
            return Config.config.DATABASE.port # type: ignore

        @property
        def getUsername(self):
            """Fetches values of username from config"""
            return Config.config.DATABASE.username # type: ignore

        @property
        def getPassword(self):
            """Fetches values of username from config"""
            return Config.config.DATABASE.password # type: ignore


    class Bot:
        def __init__(self):
            pass

        @property
        def getToken(cls):
            """Gets bot token from config"""

            return Config.config.DEFAULT.token # type: ignore

        @property
        def getPrefix(cls):
            """Gets bot prefix from config"""

            return Config.config.DEFAULT.prefix # type: ignore


if __name__ == "__main__":
    Config.loadConfig()

    configBOT = Config.Bot()
    configDB = Config.Database()

    logger.info(configDB.getHost)
    logger.info(configDB.getPort)
    logger.info(configDB.getUsername)
    logger.info(configDB.getPassword)
    logger.info(configBOT.getToken)
    logger.info(configBOT.getPrefix)
