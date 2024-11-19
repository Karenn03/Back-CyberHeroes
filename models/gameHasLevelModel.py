from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class GameHasLevel(Base):
    __tablename__ = "game_has_level"
    idGameHasLevel = Column(Integer, primary_key=True, autoincrement=True)
    idGame = Column(Integer, ForeignKey("game.idGame"), nullable=False)
    idUser = Column(Integer, ForeignKey("users.idUser"), nullable=False)
    idLevel = Column(Integer, ForeignKey("level.idLevel"), nullable=False)

    game = relationship("Game", back_populates="game_has_levels")
    user = relationship("User", back_populates="game_has_levels")
    level = relationship("Level", back_populates="game_has_levels")