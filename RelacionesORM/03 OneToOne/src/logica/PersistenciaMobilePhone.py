from src.modelo.Person import Person
from src.modelo.MobilePhone import MobilePhone
from sqlalchemy.exc import SQLAlchemyError
from src.modelo.declarative_base import session

class PersistenciaMobilePhone:
    def agregarMobilePhone(self, numero, operador, person):
        busqueda = session.query(MobilePhone).filter(MobilePhone.numero == numero).all()
        if len(busqueda) == 0:
            mobilePhone = MobilePhone(numero=numero, operador=operador, person=person)
            session.add(mobilePhone)
            session.commit()
            return True
        else:
            return False

    def VerFilas(self):
        mobilePhones = session.query(MobilePhone).all()
        print('\n### MobilePhone:')
        for mobilePhone in mobilePhones:
            print(f'id: {mobilePhone.id} Número: {mobilePhone.numero} operador: {mobilePhone.operador} perteneciente al Id: {mobilePhone.person_id}')
        print('')

    def eliminarFilaAFila(self):
        mobilePhones = session.query(MobilePhone).all()
        for mobilePhone in mobilePhones:
            session.delete(mobilePhone)
        session.commit()

    def eliminarFilaSQL(self):
        sentencia = "DELETE  from mobile_phones"
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
        return session.query(MobilePhone).get(id)