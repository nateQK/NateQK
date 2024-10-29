from sqlalchemy import BigInteger, ForeignKey, Column, Integer

from sqlalchemy.orm import mapped_column, relationship, Mapped, declarative_base
from sqlalchemy.ext.asyncio import AsyncAttrs

import asyncio

Base = declarative_base()

# NOTE: The things I'm ignoring here are not compatible with mypy, this is why they fail
class ServerSettings(Base): # type: ignore
    __tablename__ = "guildSettings"

    guildID = Column(BigInteger, primary_key=True, unique=True)
    serverJoin = Column(Integer, autoincrement=True)
    ownerID = Column(Integer)

    views = relationship("Views", back_populates="server")

class Views(Base): # type: ignore
    __tablename__ = "arcViews"

    id = Column(Integer, primary_key=True, autoincrement=True)
    viewID = Column(BigInteger)
    guildID = ForeignKey(f"{ServerSettings.__tablename__}.guildID")

    server = relationship("ServerSettings", back_populates="views")



