from sqlalchemy import Column, BigInteger, ForeignKey
from sqlalchemy.orm import DeclarativeBase, declarative_base
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import mapped_column, relationship, Mapped

import asyncio

Base = declarative_base()

#class Base(DeclarativeBase):
#    pass

class ServerSettings(Base):
    __tablename__ = "guildSettings"

    guildID: Mapped[int] = mapped_column(primary_key=True, unique=True)
    serverJoin: Mapped[int] = mapped_column(autoincrement=True)
    ownerID: Mapped[BigInteger]

class views(Base):
    __tablename__ = "arcViews"

    id: Mapped[int] = mapped_column(primary_key=True)
    viewID: Mapped[int]
    guildID: Mapped[int] = mapped_column(ForeignKey(f"{ServerSettings.__tablename__}.guildID"))

    server = relationship("ServerSettings", back_populates="views")



