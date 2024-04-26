from flask import Flask, session, request, render_template, redirect, Response, url_for, flash
from flask import Blueprint
from conexion.conexionBD import connectionBD
blueprint = Blueprint('blueprint',__name__)

app = Flask(__name__, template_folder='templates', static_folder='static')

#HOME
@app.route('/')
def home():
    return render_template('homepage.html')

#LOGIN - INICIO DE SESION
@app.route('/login' , methods = ["GET" , "POST"])
def login_route():
    return render_template ('login.html')

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
