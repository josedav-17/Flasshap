from flask import Flask, redirect, render_template, request, session, url_for, flash, g
from flask_wtf import CSRFProtect
from OperacionesDB import *
import requests
import unittest
import logging

App = Flask(__name__)
App.secret_key = '125AS35%$#2564"#$365/'
csrf = CSRFProtect(App)

@App.route('/')
def Login():  
    return render_template('Login.html')

#Conexion con base de datos
@App.route('/Home/', methods=['POST','GET'])
def home():    

    Usuario = request.form.get('User')
    Contra = request.form.get('Password')

    Dato = ValidaIngreso(Usuario)

    if request.method == 'POST':
        if Dato != None:
            if Usuario == Dato[0] and Contra == Dato[1]:
                session['username'] = request.form.get('User')

                datos = obtener_todas_las_tablas()
                registrar_dispositivo(request)

                return render_template('Home.html', Name=session['username'], datos=datos)
            
            else:
                flash(f'Usuario:{Usuario}, Contraseña Incorrecta')                
        else:
            flash(f'El Usuario {Usuario}, no esta en la base de datos')
    return redirect('/')



@App.route('/Logout/',  methods=['POST','GET'])
def Logout():
    if 'username' in session:
        session.pop('username')            
    return redirect('/') 



@App.after_request
def log_the_status_code(response):   
    print(str(response.status_code))  
    return response
    
@App.route('/Prueba',  methods=['POST','GET'])
def Prueba():
    
    return 'OK'

@App.route('/info',methods=["GET","POST"])
def inicio():
    cad=""
    cad+="URL:"+request.url+"<br/>"
    cad+="Método:"+request.method+"<br/>"
    cad+="header:<br/>"    

    for item,value in request.headers.items():
        cad+="{}:{}<br/>".format(item,value)    
    cad+="información en formularios (POST):<br/>"
    for item,value in request.form.items():
        cad+="{}:{}<br/>".format(item,value)
    cad+="información en URL (GET):<br/>"
    for item,value in request.args.items():
        cad+="{}:{}<br/>".format(item,value)    
    cad+="Ficheros:<br/>"
    for item,value in request.files.items():
        cad+="{}:{}<br/>".format(item,value)
    return cad , 200, {"Status":200}
    

if __name__ == '__main__':
    App.run(debug=True, port=8080)


