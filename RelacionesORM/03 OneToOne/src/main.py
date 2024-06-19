from src.modelo.Person import Person
from src.modelo.MobilePhone import MobilePhone
from src.modelo.declarative_base import Base, engine, session
from src.logica.PersistenciaPerson import PersistenciaPerson
from src.logica.PersistenciaMobilePhone import PersistenciaMobilePhone

def almacenar():
    # Crea la BD
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    persistenciaPerson = PersistenciaPerson()
    persistenciaMobilePhone = PersistenciaMobilePhone()

    # crear Person
    persona1 = Person(nombre="Juan Rios Solis")
    persona2 = Person(nombre="Jorge Perez Ramos")
    session.add(persona1)
    session.add(persona2)
    session.commit()

    # crear MobilePhone
    mobilePhone1 = MobilePhone(numero="954636524", operador="Claro", person=persona1)
    mobilePhone2 = MobilePhone(numero="964381245", operador="Movistar", person=persona2)
    session.add(mobilePhone1)
    session.add(mobilePhone2)
    session.commit()

    persistenciaPerson.VerFilas()
    persistenciaMobilePhone.VerFilas()

    session.close()

def almacenarPersitencia():
    # Crea la BD
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    persistenciaPerson = PersistenciaPerson()
    persistenciaMobilePhone = PersistenciaMobilePhone()

    # crear Person
    persistenciaPerson.agregarPerson(nombre="Juan Rios Solis")
    persistenciaPerson.agregarPerson(nombre="Jorge Perez Ramos")
    persona1 = persistenciaPerson.dar_id(1)
    persona2 = persistenciaPerson.dar_id(2)

    # crear MobilePhone
    persistenciaMobilePhone.agregarMobilePhone(numero="954636524", operador="Claro", person=persona1)
    persistenciaMobilePhone.agregarMobilePhone(numero="964381245", operador="Movistar", person=persona2)

    persistenciaPerson.VerFilas()
    persistenciaMobilePhone.VerFilas()

    session.close()

if __name__ == '__main__':
    #almacenar()
    almacenarPersitencia()


