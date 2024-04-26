from flask import Flask, session, request, render_template, redirect, Response, url_for, flash
from flask import Blueprint
from conexion.conexionBD import connectionBD
blueprint = Blueprint('blueprint',__name__)

app = Flask(__name__, template_folder='templates', static_folder='static')

#HOME
@app.route('/')
def home():
    return render_template('homepage.html')