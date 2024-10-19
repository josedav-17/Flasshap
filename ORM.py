from Conexion import * 
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
import pandas as pd

engine = create_engine(CadeConexionSQL())
conn = engine.connect()

#Para que funcione sin class objecto
meta = MetaData()

#Funciona para class objeto
Base = declarative_base()


"""Con obejcto class"""
#Crear tabla apartir de una objecto
class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    sex = Column(String(2))
    clas = Column(String(20))
    grade = Column(Float(32))
#Instruccion para crear la o eliminar tabla en el motor
#Student.__table__.create(engine) 
#Student.__table__.drop(engine)


#Esto funciona como el cursos es para realizar operaciones en la base
Session = sessionmaker(engine)
session = Session()

#Leer datos de sql
Student = session.query(Student).all()
for Student in Student:
   print(Student.name)

pd = pd.read_sql_query('Select * from Student', conn)
print(pd)

session.close()



#Insertar datos al objecto creado
new_student = Student(name='lily',sex='F',clas=2, grade=97)
session.add(new_student)
session.commit()
session.close()



"""Sin obejcto class"""
#Crear tablas sin comportarse como objectos
students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('lastname', String), 
)

#Borra los elementos del motor de base
Student = Table(
   'students', meta
)
Student.create(engine)
Student.drop(engine)

#Crea o borra todo lo del motor
meta.create_all(engine)
meta.drop_all(engine)

if __name__ == "__main__":
    print('Solo esto')