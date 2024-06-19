from src.modelo.Class import Class
from sqlalchemy.exc import SQLAlchemyError
from src.modelo.declarative_base import session

class PersistenciaClass():
    def agregarClass(self, asignatura):
        busqueda = session.query(Class).filter(Class.asignatura == asignatura).all()
        if len(busqueda) == 0:
            clase = Class(asignatura=asignatura)
            session.add(clase)
            session.commit()
            return True
        else:
            return False

    def VerFilas(self):
        clases = session.query(Class).all()
        print('\n### Clases:')
        for clase in clases:
            print(f'id: {clase.id} Asignatura: {clase.asignatura}')
        print('')

    def eliminarFilaAFila(self):
        clases = session.query(Class).all()
        for clase in clases:
            session.delete(clase)
        session.commit()

    def eliminarFilaSQL(self):
        sentencia = "DELETE  from classes"
        try:
            data_source = session.execute(sentencia)
            session.commit()
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
        else:
            print("Tabla classes")
            print("Nro de registros borrados : ", data_source.rowcount)


    def dar_id(self, id):
        return session.query(Class).get(id)