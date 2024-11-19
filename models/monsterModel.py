from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Monsters(Base):
    __tablename__ = "monsters"
    idMonsters = Column(Integer, primary_key=True, autoincrement=True)
    idLevel = Column(Integer, ForeignKey("level.idLevel"), nullable=False)
    name = Column(String(50), nullable=False)
    description = Column(String(100), nullable=False)

    level = relationship("Level", back_populates="monsters")
    categories = relationship("Category", back_populates="monster")
    game_has_monsters = relationship("GameHasMonsters", back_populates="monster")