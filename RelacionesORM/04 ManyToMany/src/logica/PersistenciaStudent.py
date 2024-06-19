from src.modelo.Student import Student
from sqlalchemy.exc import SQLAlchemyError
from src.modelo.declarative_base import session

class PersistenciaStudent():
    def agregarStudent(self, titulo):
        busqueda = session.query(Student).filter(Student.nombre == nombre).all()
        if len(busqueda) == 0:
            student = Student(nombre=nombre)
            session.add(student)
            session.commit()
            return True
        else:
            return False

    def VerFilas(self):
        students = session.query(Student).all()
        print('\n### Estudiantes:')
        for student in students:
            print(f'id: {student.id} Nombre: {student.nombre}')
        print('')

    def eliminarFilaAFila(self):
        students = session.query(Student).all()
        for student in students:
            session.delete(student)
        session.commit()

    def eliminarFilaSQL(self):
        sentencia = "DELETE  from students"
        try:
            data_source = session.execute(sentencia)
            session.commit()
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
        else:
            print("Tabla students")
            print("Nro de registros borrados : ", data_source.rowcount)


    def dar_id(self, id):
        return session.query(Student).get(id)