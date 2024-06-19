from src.modelo.Car import Car
from sqlalchemy.exc import SQLAlchemyError
from src.modelo.declarative_base import session


class PersistenciaCar():
    def agregarCar(self, placa):
        busqueda = session.query(Car).filter(Car.placa == placa).all()
        if len(busqueda) == 0:
            car = Car(placa=placa)
            session.add(car)
            session.commit()
            return True
        else:
            return False

    def VerFilas(self):
        cars = session.query(Car).all()
        print('\n### Cars:')
        for car in cars:
            print(f'id: {car.id} Placa: {car.placa}')
        print('')

    def eliminarFilaSQL(self):
        sentencia = "DELETE from cars"
        try:
            data_source = session.execute(sentencia)
            session.commit()
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
        else:
            print("Tabla cars")
            print("Nro de registros borrados : ", data_source.rowcount)

    def dar_id(self, id):
        return session.query(Car).get(id)
