from src.modelo.Tire import Tire
from sqlalchemy.exc import SQLAlchemyError
from src.modelo.declarative_base import session

class PersistenciaTire():
    def agregarTire(self, serie,cars):
        busqueda = session.query(Tire).filter(Tire.serie == serie).all()
        if len(busqueda) == 0:
            tire = Tire(serie=serie,cars=cars)
            session.add(tire)
            session.commit()
            return True
        else:
            return False

    def VerFilas(self):
        tires = session.query(Tire).all()
        print('\n### Tires:')
        for tire in tires:
            print(f'id: {tire.id} serie: {tire.serie} car id: {tire.car_id}')
        print('')

    def eliminarFilaSQL(self):
        sentencia = "DELETE from tires"
        try:
            data_source = session.execute(sentencia)
            session.commit()
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
        else:
            print("Tabla tires")
            print("Nro de registros borrados : ", data_source.rowcount)

    def dar_id(self, id):
        return session.query(Tire).get(id)
