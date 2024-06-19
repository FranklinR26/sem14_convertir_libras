from src.modelo.declarative_base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    nombre =Column(String)
    mobile_phone = relationship("MobilePhone", uselist=False, back_populates="person")

    def __init__(self, nombre):
        self.nombre = nombre