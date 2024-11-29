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
    economy = Column(Integer)  # NOTE: How much money is in the economy currently
    economyLeft = Column(Integer)  # NOTE: How much money is left in the public bank
    defacedCurrenty = Column(Integer)  # NOTE: How much money has been burned or "Defaced"

    views = relationship("Views", back_populates="server")


class Views(Base):
    __tablename__ = "arcViews"

    id = Column(Integer, primary_key=True, autoincrement=True)
    viewID = Column(BigInteger)
    guildID = Column(BigInteger, ForeignKey(f"{ServerSettings.__tablename__}.guildID"))

    server = relationship("ServerSettings", back_populates="views")


class Users(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(Integer, unique=True)
    worth = Column(Integer)
    messagesSent = Column(Integer)  # NOTE: Ballpark Estimation of How many messages have been sent by this user (Not 100% accurate)
    
    economy = relationship("Economy", back_populates="user")
    levels = relationship("Levels", back_populates="user")


class Economy(Base):
    __tablename__ = "Economy"

    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(Integer, ForeignKey("Users.uid"))
    coins = Column(Integer)  # NOTE: How much money the user currently has

    user = relationship("Users", back_populates="economy")


class Levels(Base):  # NOTE: This wasn't asked for, I just like level systems, and it's a game engine. so it makes sense
    __tablename__ = "Levels"

    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(Integer, ForeignKey("Users.uid"), unique=True)  # NOTE: This is the id of the discord user
    exp = Column(Integer)

    user = relationship("Users", back_populates="levels")

