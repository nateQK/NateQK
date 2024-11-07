from sqlalchemy import BigInteger, ForeignKey, Column, Integer

from sqlalchemy.orm import DeclarativeBase, relationship

class Base(DeclarativeBase):
    pass

class ServerSettings(Base):
    __tablename__ = "guildSettings"

    guildID = Column(BigInteger, primary_key=True, unique=True)
    serverJoin = Column(Integer, autoincrement=True)
    ownerID = Column(Integer)

    views = relationship("Views", back_populates="server")

class Views(Base):
    __tablename__ = "arcViews"

    id = Column(Integer, primary_key=True, autoincrement=True)
    viewID = Column(BigInteger)
    guildID = ForeignKey(f"{ServerSettings.__tablename__}.guildID")

    server = relationship("ServerSettings", back_populates="views")



