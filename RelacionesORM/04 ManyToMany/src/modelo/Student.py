from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from src.modelo.declarative_base import Base

students_classes_association = Table('students_classes', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('class_id', Integer, ForeignKey('classes.id'))
)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    classes = relationship("Class", secondary=students_classes_association)

    def __init__(self, nombre):
        self.nombre = nombre