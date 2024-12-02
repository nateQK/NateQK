'''Config and Other globablly usable variables module.'''
import tomllib
from os import path
from loguru import logger
from pydantic import BaseModel
from typing import Any
import requests
import os
from dotenv import load_dotenv

class DefaultConfig(BaseModel):
    token: str
    botpfp: str

class DatabaseConfig(BaseModel):
    engine: str
    host: str
    port: int
    username: str
    password: str
    database: str

class GitConfig(BaseModel):
    repo: str
    localdir: str = "blazium"

class MessageConfig(BaseModel):
    activity: str

class VersionConfig(BaseModel):
    version: str
    major: int
    minor: int
    branch: str


class Configuration(BaseModel):
    DEFAULT: DefaultConfig
    DATABASE: DatabaseConfig
    GIT: GitConfig
    MESSAGE: MessageConfig
    VERSION: VersionConfig



class Config:
    config: Configuration
    @classmethod
    def loadConfig(cls) -> None:
        """Loads, Fetches, and Validates config from a pre-determined file"""
        load_dotenv()
        config: dict[str, Any] = {
            'DEFAULT': 
                {'token': os.getenv("TOKEN"),
                 'botpfp': os.getenv("BOTPFP")
                 },
            'DATABASE': 
                {'engine': os.getenv("ENGINE"),
                'host': os.getenv("HOST"),
                'port': os.getenv("PORT"),
                'username': os.getenv("DBUSERNAME"),
                'password': os.getenv("PASSWORD"),
                'database': os.getenv("DATABASE")
                 },
            'GIT':
                {'repo': os.getenv("REPO_URL"),
                 'localdir': "blazium"

                },
            'MESSAGE': 
                {'activity': os.getenv("ACTIVITY")}
        }


        configfile: str = path.join("bot", "app.toml")

        with open(configfile, 'rb') as file:
            fileconfig = tomllib.load(file)

        for x in fileconfig.values():
            config["VERSION"] = x

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

    class Git:
        @classmethod
        def getRepo(cls) -> str:
            """Fetches value of GIT.repo from config"""
            return Config.config.GIT.repo

        @classmethod
        def getLocalDir(cls) -> str:
            """Fetches value of GIT.localdir from config"""
            return Config.config.GIT.localdir

    class Message:
        @classmethod
        def getActivity(cls) -> str:
            return Config.config.MESSAGE.activity

    class Bot:

        @classmethod
        def getToken(cls) -> str:
            """Gets bot token from config"""
            return Config.config.DEFAULT.token

        @classmethod
        def getBotPFP(cls) -> str:
            """Gets bot token from config"""
            return Config.config.DEFAULT.botpfp

    class Version:

        @classmethod
        def getVersion(cls) -> str:
            """Gets NateQK's Current version and compares to latest release"""


            CurrentVersion=Config.config.VERSION.version+"-"+Config.config.VERSION.branch
            return CurrentVersion

        @classmethod
        def compareLatest(cls) -> str:
            """Gets NateQK's Current version and compares to latest release"""


            CurrentMajor = Config.config.VERSION.major
            CurrentMinor = Config.config.VERSION.minor
            CurrentBranch = Config.config.VERSION.branch

            CurrentVersion = f"{CurrentMajor}.{CurrentMinor}{CurrentBranch if CurrentBranch != 'dev' else ''}"

            # TODO:
            # Ping github Looking for latest version
            # I'm working on getting a webserver setup
            # using github pages so this is easy
            LatestVersion=cls.latestVersion() # Ping github and look for latest version
            if CurrentVersion != LatestVersion:
                Response: str = f"""
                Latest Version: {LatestVersion}
                Current Version: {CurrentVersion}
                """
                return Response
            else:
                return CurrentVersion

        @classmethod
        def latestVersion(cls) -> str:
            """Gets NateQK's latest version"""
            try:
                req: requests.Response = requests.get("https://nateqk.github.io/latest/latest.json")
                reqjson: Any = req.json()

            except requests.HTTPError as e:
                logger.error(f"Somethig went terribly wrong with your request to check latest bot version: {e}")
                return f"{e}"

            logger.debug(req.json())
            return f"{reqjson['version']['major']}.{reqjson['version']['minor']}"


