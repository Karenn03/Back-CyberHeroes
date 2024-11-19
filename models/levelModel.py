from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Level(Base):
    __tablename__ = "level"
    idlevel = Column(Integer, primary_key=True, autoincrement=True)
    difficulty = Column(String(20), nullable=False)

    monsters = relationship("Monsters", back_populates="level")
    game_has_levels = relationship("GameHasLevel", back_populates="level")