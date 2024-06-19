from src.modelo.declarative_base import Base
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

class Tire(Base):
    __tablename__ = 'tires'

    id = Column(Integer, primary_key=True)
    serie = Column(String)

    car_id = Column(Integer, ForeignKey('cars.id'))
    cars = relationship('Car')

    def __init__(self, serie, cars):
        self.serie = serie
        self.cars = cars