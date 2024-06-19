from src.modelo.declarative_base import Base
from sqlalchemy import Column, Integer, String

class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    placa = Column(String)

    def __init__(self, placa):
        self.placa = placa
