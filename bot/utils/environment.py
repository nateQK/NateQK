'''Config and Other globablly usable variables module.'''
import tomllib
from os import path
from loguru import logger
from pydantic import BaseModel
from typing import TypedDict


class DefaultConfig(BaseModel):
    token: str

class DatabaseConfig(BaseModel):
    host: str
    port: int
    username: str
    password: str

class VersionConfig(BaseModel):
    version: str

class Configuration(BaseModel):
    DEFAULT: DefaultConfig
    DATABASE: DatabaseConfig
    VERSION: VersionConfig



class Config:
    config: Configuration

    @classmethod
    def loadConfig(cls) -> None:
        """Loads, Fetches, and Validates config from a pre-determined file"""

        configfile: str = path.join("bot", "app.toml")

        #? Dev configfile
        #configfile: str = path.join("..", "app.toml")


        with open(configfile, 'rb') as file:
            config = tomllib.load(file)
        cls.config = Configuration(**config)


    class Database:

        @classmethod
        def getHost(cls):
            """Fetches values of Datbase.host from config"""
            return Config.config.DATABASE.host

        @classmethod
        def getPort(cls) -> int:
            """Fetches values of Datbase.port from config"""
            return Config.config.DATABASE.port

        @classmethod
        def getUsername(cls) -> str:
            """Fetches values of Database.username from config"""
            return Config.config.DATABASE.username

        @classmethod
        def getPassword(cls) -> str:
            """Fetches values of Database.username from config"""
            return Config.config.DATABASE.password


    class Bot:

        @classmethod
        def getToken(cls) -> str:
            """Gets bot token from config"""
            return Config.config.DEFAULT.token


    class Version:

        @classmethod
        def getVersion(cls) -> str:
            """Gets NateQK's Current version and compares to latest release"""


            CurrentVersion=Config.config.VERSION.version
            LatestVersion="0.0.1" # Ping github and look for latest version
            return CurrentVersion



if __name__ == "__main__":
    Config.loadConfig()
    
    logger.info(Config.Database.getHost())
    logger.info(Config.Database.getPort())
    logger.info(Config.Database.getUsername())
    logger.info(Config.Database.getPassword())
    logger.info(Config.Bot.getToken())
    logger.info(Config.Version.getVersion())
