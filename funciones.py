# funciones.py
from flask import Flask, session, request, render_template, redirect, Response, url_for, flash
from flask import Blueprint
from conexion.conexionBD import connectionBD
from plyer import notification
blueprint = Blueprint('blueprint',__name__)


#FUNCION LOGIN
def login(request):
    try:
        connection = connectionBD()
        if request.method == 'POST' and 'txtCorreo' in request.form and 'txtPassword' in request.form:
            _correo = request.form['txtCorreo']
            _password = request.form['txtPassword']

            cur = connection.cursor(dictionary=True)
            cur.execute('SELECT * FROM usuarios WHERE CorreoUsuario = %s AND ContrasenaUsuario = %s LIMIT 1', (_correo, _password,))
            account = cur.fetchone()
            cur.close()

            if account:
                session['logueado'] = True
                session['id'] = account['IdUsuario']
                return True  # Autenticación exitosa

    except Exception as e:
        print(f"Error en la función login: {e}")

    finally:
        if connection.is_connected():
            connection.close()

    return False  # Autenticación fallida
