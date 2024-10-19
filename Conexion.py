# import pyodbc 
# import urllib.parse

# Servidor = '(localdb)\MSSQLLocalDB' 
# BaseDatos = 'Consultas' 
# Driver = 'SQL Server Native Client 11.0'

# Uss = ['Operaciones','DatosRPA'] 
# Pass = ['Op3racion3s123%2A','DatosRPA']

# def ObtenerConexion():
#     return pyodbc.connect(
#         'Driver={'+Driver+'};'
#         'Server='+Servidor+';'
#         'Database='+BaseDatos+';'
#         'UID='+Uss[0]+';'
#         'PWD='+urllib.parse.unquote(Pass[0])+';'
#     )


# def ObtenerConexion2():
#     return pyodbc.connect(
#         'Driver={'+Driver+'};'
#         'Server='+Servidor+';'
#         'Database='+BaseDatos+';'
#         'UID='+Uss[1]+';'
#         'PWD='+urllib.parse.unquote(Pass[1])+';'
#     )

# def CadeConexionSQL():
#     return(
#         f'mssql://{Uss[0]}:{Pass[0]}@{Servidor}/{BaseDatos}?driver={Driver}'
#     )

import mysql.connector
from mysql.connector import Error
import urllib.parse

host = 'localhost'
database = 'basedatos'
user = 'root'
password = ''

def ObtenerConexion():
    password_decoded = urllib.parse.unquote(password)
    return mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password_decoded
        )

