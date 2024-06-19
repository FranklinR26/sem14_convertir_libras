from sqlalchemy import Column, Integer,String
from src.modelo.declarative_base import Base

class Class(Base):
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True)
    asignatura = Column(String, nullable=False)

    def __init__(self, asignatura):
        self.asignatura = asignatura