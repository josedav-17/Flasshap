from Conexion import *
import requests

def Datos():
    conn = ObtenerConexion()
    Datos = []
    with conn.cursor() as cursor:
        cursor.execute('Select * from [dbo].[basedatos]')
        Datos = cursor.fetchall()
    conn.close()
    print(Datos())
    return Datos


def ValidaIngreso(username):
    print(username)
    conn = ObtenerConexion()
    Datos = []
    with conn.cursor() as cursor:
        cursor.execute("SELECT User, Password FROM usuarios WHERE User = %s", (username,))
        Datos = cursor.fetchone()
    conn.close()
    return Datos


def obtener_todas_las_tablas():
    conn = ObtenerConexion()
    
    # Diccionario para almacenar los datos de cada tabla
    datos_totales = {
        'clientes': [],
        'sensores': [],
        'mediciones': [],
        'reportes': []
    }

    try:
        with conn.cursor() as cursor:
            # Obtener datos de la tabla clientes
            cursor.execute('SELECT * FROM clientes')
            datos_totales['clientes'] = cursor.fetchall()
            
            # Obtener datos de la tabla sensores
            cursor.execute('SELECT * FROM sensores')
            datos_totales['sensores'] = cursor.fetchall()
            
            # Obtener datos de la tabla mediciones
            cursor.execute('SELECT * FROM mediciones')
            datos_totales['mediciones'] = cursor.fetchall()
            
            # Obtener datos de la tabla reportes
            cursor.execute('SELECT * FROM reportes')
            datos_totales['reportes'] = cursor.fetchall()

    finally:
        conn.close()  # Asegúrate de cerrar la conexión

    return datos_totales


def registrar_dispositivo(request):
    direccion_ip = request.remote_addr
    ciudad, pais = obtener_geolocalizacion(direccion_ip)
    print(f"Inserción: {direccion_ip}, {request.user_agent.string}, {ciudad}, {pais}")
    
    conn = ObtenerConexion()
    try:
        with conn.cursor() as cursor:
            cursor.execute('''
                INSERT INTO dispositivos (direccion_ip, user_agent, ciudad, pais)
                VALUES (%s, %s, %s, %s)
            ''', (direccion_ip, request.user_agent.string, ciudad, pais))
            conn.commit()
    except Exception as e:
        print(f"Error al registrar dispositivo: {e}")  # Imprime el error específico
    finally:
        conn.close()


def obtener_geolocalizacion(ip):
    try:
        response = requests.get(f'https://ipinfo.io/[dirección IP]?token= 729c714cb230ad')
        data = response.json()
        ciudad = data.get('city', 'Desconocida')
        pais = data.get('country', 'Desconocido')
        return ciudad, pais
    except Exception as e:
        print(f"Error al obtener geolocalización: {e}")
        return 'Desconocida', 'Desconocido'
