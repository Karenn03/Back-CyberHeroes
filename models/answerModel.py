from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Answer(Base):
    __tablename__ = "answers"
    idAnswer = Column(Integer, primary_key=True, autoincrement=True)
    idQuestion = Column(Integer, ForeignKey("questions.idQuestion"), nullable=False)
    answer = Column(String(170), nullable=False)
    isCorrect = Column(Boolean, nullable=False)

    question = relationship("Question", back_populates="answers")