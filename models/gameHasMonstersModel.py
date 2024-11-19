from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class GameHasMonsters(Base):
    __tablename__ = "game_has_monsters"
    idGameHasMonsters = Column(Integer, primary_key=True, autoincrement=True)
    idGame = Column(Integer, ForeignKey("game.idGame"), nullable=False)
    idUser = Column(Integer, ForeignKey("users.idUser"), nullable=False)
    idMonsters = Column(Integer, ForeignKey("monsters.idMonsters"), nullable=False)
    idLevel = Column(Integer, ForeignKey("level.idLevel"), nullable=False)

    game = relationship("Game", back_populates="game_has_monsters")
    user = relationship("User", back_populates="game_has_monsters")
    monster = relationship("Monsters", back_populates="game_has_monsters")