from src.modelo.Person import Person
from src.modelo.MobilePhone import MobilePhone
from sqlalchemy.exc import SQLAlchemyError
from src.modelo.declarative_base import session

class PersistenciaPerson():
    def agregarPerson(self, nombre):
        busqueda = session.query(Person).filter(Person.nombre == nombre).all()
        if len(busqueda) == 0:
            person = Person(nombre=nombre)
            session.add(person)
            session.commit()
            return True
        else:
            return False

    def VerFilas(self):
        persons = session.query(Person).all()
        print('\n### Articulos:')
        for person in persons:
            print(f'id: {person.id} Nombre: {person.nombre}')
        print('')

    def eliminarFilaAFila(self):
        persons = session.query(Person).all()
        for person in persons:
            session.delete(person)
        session.commit()

    def eliminarFilaSQL(self):
        sentencia = "DELETE  from people"
        try:
            data_source = session.execute(sentencia)
            session.commit()
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
        else:
            print("Tabla people")
            print("Nro de registros borrados : ", data_source.rowcount)


    def dar_id(self, id):
        return session.query(Person).get(id)