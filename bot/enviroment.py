from pydantic import BaseModel
import tomllib
from os import path


class MongoConfig(BaseModel):
    """Connection info for the mongodb server"""
    HOST: str
    PORT: int
    USERNAME: str
    PASSWORD: str

#? Pydnatic class for Verifying data
class BaseConfig(BaseModel):
    """
    Base Config for the app
    Any changes made to the config need to be reflected here
    """
    TOKEN: str
    PREFIX: str
    database: MongoConfig


class Config:
    @classmethod
    def loadConfig(cls):
        """Loads, Fetches, and Validates config from a pre-determined file"""
        configfile=path.join("../app.toml")
        print(configfile)
        with open(configfile, 'rb') as f:
            config = tomllib.load(f)
            print(config)


    
    @classmethod
    def verifyConfig(cls):
        """Uses pydantic to verify config validity"""
        pass
    
    class Database:

        @classmethod
        def getHost(cls):
            """Fetches values of host from config"""
            pass

        @classmethod
        def getPort(cls):
            """Fetches values of port from config"""
            pass

        @classmethod
        def getUsername(cls):
            """Fetches values of username from config"""
            pass

    class normal:
        @classmethod
        def getToken(cls):
            """Gets bot token from config"""
            pass

        @classmethod
        def getPrefix(cls):
            """Gets bot prefix from config"""
            pass

if __name__ == "__main__":
    Config.loadConfig()
