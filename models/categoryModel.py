from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Category(Base):
    __tablename__ = "categories"
    idCategory = Column(Integer, primary_key=True, autoincrement=True)
    idMonsters = Column(Integer, ForeignKey("monsters.idMonsters"), nullable=False)
    category = Column(String(65), nullable=False)

    monster = relationship("Monsters", back_populates="categories")
    questions = relationship("Question", back_populates="category")