from src.modelo.declarative_base import Base, engine, session
from src.logica.PersistenciaCar import PersistenciaCar
from src.logica.PersistenciaTire import PersistenciaTire
from src.modelo.Car import Car
from src.modelo.Tire import Tire

def almacenar():
    # Crea la BD
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    persistenciaCar = PersistenciaCar()
    persistenciaTire = PersistenciaTire()
    persistenciaCar.eliminarFilaSQL()
    persistenciaTire.eliminarFilaSQL()

    # crear Car
    car1 = Car(placa="AAA-123")
    car2 = Car(placa="DPZ-721")
    car3 = Car(placa="A1A-970")

    session.add(car1)
    session.add(car2)
    session.add(car3)
    session.commit()

    # crear Tires
    tire1 = Tire(serie="SN/000101", cars=car1)
    tire2 = Tire(serie="SN/000102", cars=car1)
    tire3 = Tire(serie="SN/000103", cars=car2)
    tire4 = Tire(serie="SN/000104", cars=car2)
    session.add(tire1)
    session.add(tire2)
    session.add(tire3)
    session.add(tire4)
    session.commit()

    persistenciaCar.VerFilas()
    persistenciaTire.VerFilas()

    session.close()

def almacenarPersistencia():
    # Crea la BD
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    persistenciaCar = PersistenciaCar()
    persistenciaTire = PersistenciaTire()

    #persistenciaCar.eliminarFilaSQL()
    #persistenciaTire.eliminarFilaSQL()

    # crear Car
    persistenciaCar.agregarCar(placa="AAA-123")
    persistenciaCar.agregarCar(placa="DPZ-721")
    persistenciaCar.agregarCar(placa="A1A-970")

    car1 = persistenciaCar.dar_id(1)
    car2 = persistenciaCar.dar_id(2)
    car3 = persistenciaCar.dar_id(3)

    # crear Tire
    persistenciaTire.agregarTire(serie="SN/000101", cars=car1)
    persistenciaTire.agregarTire(serie="SN/000102", cars=car1)
    persistenciaTire.agregarTire(serie="SN/000103", cars=car1)
    persistenciaTire.agregarTire(serie="SN/000104", cars=car1)
    persistenciaTire.agregarTire(serie="SN/000105", cars=car2)
    persistenciaTire.agregarTire(serie="SN/000106", cars=car2)
    persistenciaTire.agregarTire(serie="SN/000107", cars=car2)
    persistenciaTire.agregarTire(serie="SN/000108", cars=car2)
    persistenciaTire.agregarTire(serie="SN/000109", cars=car3)
    persistenciaTire.agregarTire(serie="SN/000110", cars=car3)
    persistenciaTire.agregarTire(serie="SN/000111", cars=car3)
    persistenciaTire.agregarTire(serie="SN/000112", cars=car3)

    persistenciaCar.VerFilas()
    persistenciaTire.VerFilas()

    session.close()

if __name__ == '__main__':
    almacenar()
    #almacenarPersistencia()

