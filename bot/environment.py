import tomllib
from os import path
from loguru import logger
from json import dumps
from munch import munchify




class Config:
    
    @classmethod
    def loadConfig(cls):
        """Loads, Fetches, and Validates config from a pre-determined file"""

        configfile=path.join("../app.toml")


        with open(configfile, 'rb') as f:
            config = tomllib.load(f)
            #config = dumps(config)
            cls.config = munchify(config)
            print(cls.config)

    class Database:

        @classmethod
        def getHost(cls) -> str:
            """Fetches values of host from config"""
            return Config.config.DATABASE.host

        @classmethod
        def getPort(cls):
            """Fetches values of port from config"""
            return Config.config.DATABASE.port

        @classmethod
        def getUsername(cls):
            """Fetches values of username from config"""
            return Config.config.DATABASE.username

        @classmethod
        def getPassword(cls):
            """Fetches values of username from config"""
            return Config.config.DATABASE.password


    class Bot:
        @classmethod
        def getToken(cls):
            """Gets bot token from config"""
            return Config.config.DEFAULT.token

        @classmethod
        def getPrefix(cls):
            """Gets bot prefix from config"""
            return Config.config.DEFAULT.prefix


if __name__ == "__main__":
    Config.loadConfig()
    logger.info(Config.Database.getHost())
    logger.info(Config.Database.getPort())
    logger.info(Config.Database.getUsername())
    logger.info(Config.Database.getPassword())
    logger.info(Config.Bot.getToken())
    logger.info(Config.Bot.getPrefix())

