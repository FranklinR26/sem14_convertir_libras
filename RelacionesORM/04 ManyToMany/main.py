from src.modelo.declarative_base import Base, engine, session
from src.modelo.Student import Student
from src.modelo.Class import Class
from src.modelo.declarative_base import session
from src.logica.PersistenciaStudent import PersistenciaStudent
from src.logica.PersistenciaClass import PersistenciaClass

def almacenar():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    persistenciaStudent = PersistenciaStudent()
    persistenciaClass = PersistenciaClass()

    # crear Student
    student1 = Student(nombre="Rafael Solis Matos")
    student2 = Student(nombre="Manuel Mantilla Ramos")
    session.add(student1)
    session.add(student2)
    session.commit()

    # crear Class
    class1 = Class(asignatura="Ingeniería de software")
    class2 = Class(asignatura="Inteligencia artificial")
    session.add(class1)
    session.add(class2)
    session.commit()

    # Relacionar articulos con commentarios
    student1.classes = [class1, class2]
    student2.classes = [class2]
    session.commit()

    persistenciaStudent.VerFilas()
    persistenciaClass.VerFilas()

    session.close()

if __name__ == '__main__':
   almacenar()
