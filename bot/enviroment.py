from pydantic import BaseModel

class MongoConfig:
    HOST: str
    PORT: int
    USERNAME: str
    PASSWORD: str

#? Pydnatic class for Verifying data
class BaseConfig:
    TOKEN: str
    PREFIX: str
    database: MongoConfig

