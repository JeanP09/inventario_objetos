from flask import Flask, session, request, render_template, redirect, Response, url_for, flash
from flask import Blueprint
from conexion.conexionBD import connectionBD
from funciones import *
blueprint = Blueprint('blueprint',__name__)

app = Flask(__name__, template_folder='templates', static_folder='static')

#HOME --
@app.route('/')
def home():
    return render_template('homepage.html')

#LOGIN - INICIO DE SESION
@app.route('/loginUsu', methods=["GET", "POST"])
def login_route():
    if request.method == 'POST': #le digo que viene de un dato requerido por POST
        if login(request):
            return render_template('objetos.html')#INGRESO AL SISTEMA 
        else:
            return render_template('login.html') #DATOS INCORRECTOS, REDIRECCIONA LOGIN NUEVAMENTE
    else:
        return render_template('login.html') #SI TODA LA CONSULTA FALLA RENDERIZA LOGIN NUEVAMENTE

#BUSCAR OBJETOS ----
@app.route('/Objconsumibles', methods=['GET', 'POST'])
def search_route():
    if request.method == 'POST':
        return BuscarObjeto()
    else:
        return render_template('objetos.html')

#Administradores
@app.route('/administradores')
def administradores():
    return render_template('administradores.html')

#REGISTRARME
@app.route('/register')
def registrar_usuarios():
    return render_template ('register.html')

#SOBRE NOSOTROS - ABOUT US
@app.route('/sobre_nosotros')
def about_us():
    return render_template ('sobre_nosotros.html')

#QUIENES SOMOS?
@app.route('/quienes_somos')
def quien_somos():
    return render_template ('quienes_somos.html')

#CONSUMIBLES
@app.route('/consumibles')
def ob_consumibles():
    return render_template ('consumibles.html')

#DEVOLUTIVOS
@app.route('/devolutivos')
def ob_devolutivos():
    return render_template ('devolutivos.html')

#OBJETOS
@app.route('/objetos')
def ob_generales():
    return render_template ('objetos.html')

#REDIRECCIONANDO CUANDO LA PAGINA NO EXISTE

@app.errorhandler(404)
def not_found(error):
        return render_template("/")
