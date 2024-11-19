from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    idUser = Column(Integer, primary_key=True, autoincrement=True)
    idCard = Column(Integer, unique=True, nullable=False)
    names = Column(String(50), nullable=False)
    surnames = Column(String(50), nullable=False)
    email = Column(String(75), nullable=False)
    password = Column(String(255), nullable=False)
    score = Column(Integer, nullable=False)

    games = relationship("Game", back_populates="user")
    game_has_monsters = relationship("GameHasMonsters", back_populates="user")
    game_has_levels = relationship("GameHasLevel", back_populates="user")