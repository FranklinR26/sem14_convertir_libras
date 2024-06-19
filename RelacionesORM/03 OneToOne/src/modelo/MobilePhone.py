from src.modelo.declarative_base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class MobilePhone(Base):
    __tablename__ = 'mobile_phones'
    id = Column(Integer, primary_key=True)
    numero = Column(String, nullable=False)
    operador = Column(String, nullable=False)
    person_id = Column(Integer, ForeignKey('people.id'))
    person = relationship("Person", back_populates="mobile_phone")

    def __init__(self, numero, operador, person):
        self.numero = numero
        self.operador = operador
        self.person = person