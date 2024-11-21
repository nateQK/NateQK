from sqlalchemy import BigInteger, ForeignKey, Column, Integer

from sqlalchemy.orm import DeclarativeBase, relationship

class Base(DeclarativeBase):
    pass

class ServerSettings(Base):
    __tablename__ = "guildSettings"

    guildID = Column(BigInteger, primary_key=True, unique=True)
    serverJoin = Column(Integer, autoincrement=True)
    ownerID = Column(Integer)
    userAmount = Column(Integer)
    economy = Column(Integer) # NOTE: How much money is in the economy currently

    views = relationship("Views", back_populates="server")

class Views(Base):
    __tablename__ = "arcViews"

    id = Column(Integer, primary_key=True, autoincrement=True)
    viewID = Column(BigInteger)
    guildID = ForeignKey(f"{ServerSettings.__tablename__}.guildID")

    server = relationship("ServerSettings", back_populates="views")


class Users(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(Integer, unique=True)
    worth = Column(Integer)

