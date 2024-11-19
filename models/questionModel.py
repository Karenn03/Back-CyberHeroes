from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Question(Base):
    __tablename__ = "questions"
    idQuestion = Column(Integer, primary_key=True, autoincrement=True)
    idCategory = Column(Integer, ForeignKey("categories.idCategory"), nullable=False)
    content = Column(String(200), nullable=False)

    category = relationship("Category", back_populates="questions")
    answers = relationship("Answer", back_populates="question")