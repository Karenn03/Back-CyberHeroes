from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Game(Base):
    __tablename__ = "game"
    idGame = Column(Integer, primary_key=True, autoincrement=True)
    idUser = Column(Integer, ForeignKey("users.idUser"), nullable=False)
    startDate = Column(Date, nullable=False)
    endDate = Column(Date, nullable=False)
    finalScore = Column(Integer, nullable=False)

    user = relationship("User", back_populates="games")
    game_has_monsters = relationship("GameHasMonsters", back_populates="game")
    game_has_levels = relationship("GameHasLevel", back_populates="game")