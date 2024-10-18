import tomllib
from os import path
from loguru import logger
from json import dumps
from munch import munchify




class Config:
    
    @classmethod
    def loadConfig(cls):
        """Loads, Fetches, and Validates config from a pre-determined file"""

        configfile=path.join("bot", "app.toml")


        with open(configfile, 'rb') as f:
            config = tomllib.load(f)
            #config = dumps(config)
            cls.config = munchify(config)

    class Database:
        
        def __init__(self):
            pass

        @property
        def getHost(cls) -> str:
            """Fetches values of host from config"""
            return Config.config.DATABASE.host

        @property
        def getPort(cls):
            """Fetches values of port from config"""
            return Config.config.DATABASE.port

        @property
        def getUsername(cls):
            """Fetches values of username from config"""
            return Config.config.DATABASE.username

        @property
        def getPassword(cls):
            """Fetches values of username from config"""
            return Config.config.DATABASE.password


    class Bot:
        
        def __init__(self):
            pass

        @property
        def getToken(cls):
            """Gets bot token from config"""
            return Config.config.DEFAULT.token

        @property
        def getPrefix(cls):
            """Gets bot prefix from config"""
            return Config.config.DEFAULT.prefix


if __name__ == "__main__":
    #? This shit won't work unless you change the configfile path
    #? I'm just really lazy and won't write logic to fix it
    Config.loadConfig()
    botconf = Config.Bot()
    dbconf = Config.Database()
    logger.info(dbconf.getHost)
    logger.info(dbconf.getPort)
    logger.info(dbconf.getUsername)
    logger.info(dbconf.getPassword)
    logger.info(botconf.getToken)
    logger.info(botconf.getPrefix)

