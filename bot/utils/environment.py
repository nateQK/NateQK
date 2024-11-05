'''Config and Other globablly usable variables module.'''
import tomllib
from os import path
from loguru import logger
from pydantic import BaseModel
from typing import TypedDict
from requests import request
import requests

class DefaultConfig(BaseModel):
    token: str

class DatabaseConfig(BaseModel):
    engine: str
    host: str
    port: int
    username: str
    password: str
    database: str

class MessageConfig(BaseModel):
    activity: str

class VersionConfig(BaseModel):
    version: str

class Configuration(BaseModel):
    DEFAULT: DefaultConfig
    DATABASE: DatabaseConfig
    MESSAGE: MessageConfig
    VERSION: VersionConfig



class Config:
    config: Configuration

    @classmethod
    def loadConfig(cls) -> None:
        """Loads, Fetches, and Validates config from a pre-determined file"""

        configfile: str = path.join("bot", "app.toml")

        with open(configfile, 'rb') as file:
            config = tomllib.load(file)
        cls.config = Configuration(**config)


    class Database:

        @classmethod
        def getEngine(cls) -> str:
            """Fetches values of Datbase.host from config"""
            return Config.config.DATABASE.engine


        @classmethod
        def getHost(cls) -> str:
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
        
        @classmethod
        def getDatabase(cls) -> str:
            """Fetches values of Database.database from config"""
            return Config.config.DATABASE.database

    class Message:
        @classmethod
        def getActivity(cls) -> str:
            return Config.config.MESSAGE.activity

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

        @classmethod
        def latestVersion(cls) -> str:
            """Gets NateQK's latest version"""
            req: requests.Response = requests.get("https://nateqk.github.io/latest")
            logger.error(req.json())
            return 'this'


