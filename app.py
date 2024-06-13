from flask import Flask, session, request, render_template, redirect, url_for
from conexion.conexionBD import connectionBD
from funciones import *

app = Flask(__name__, template_folder='templates', static_folder='static')

# HOME --
@app.route('/')
def home():
    return render_template('homepage.html')

# LOGIN - INICIO DE SESION
@app.route('/loginUsu', methods=["GET", "POST"])
def login_route():
    if request.method == 'POST':  # le digo que viene de un dato requerido por POST
        if login(request):
            return redirect(url_for('inicio_login'))  # Cambié a redirect y url_for
        else:
            return render_template('login.html')  # DATOS INCORRECTOS, REDIRECCIONA LOGIN NUEVAMENTE
    else:
        return render_template('login.html')  # SI TODA LA CONSULTA FALLA RENDERIZA LOGIN NUEVAMENTE

# BUSCAR OBJETOS ----
@app.route('/Objconsumibles', methods=['GET', 'POST'])
def search_route():
    if request.method == 'POST':
        return BuscarObjeto()
    else:
        return render_template('objetos.html')

#ADMINISTRADORES
@app.route('/administradores')
def administradores():
    return render_template('administradores.html')

#EDITAR_OBJETO
@app.route('/editar_objeto')
def editar_objeto():
    return render_template('editar_objeto.html')

#ELIMINAR_OBJETO

#INICIO_LOGIN
@app.route('/inicio_login')
def inicio_login():
    return render_template('inicio_login.html')

#INSTRUCTORES
@app.route('/instructores')
def instructores():
    return render_template('instructores.html')

#INVENTARIO
@app.route('/inventario')
def inventario():
    return render_template('inventario.html')

# REGISTRARME
@app.route('/register')
def registrar_usuarios():
    return render_template('register.html')

# SOBRE NOSOTROS - ABOUT US
@app.route('/sobre_nosotros')
def about_us():
    return render_template('sobre_nosotros.html')

# QUIENES SOMOS?
@app.route('/quienes_somos')
def quien_somos():
    return render_template('quienes_somos.html')

# CONSUMIBLES
@app.route('/consumibles')
def ob_consumibles():
    return render_template('consumibles.html')

# DEVOLUTIVOS
@app.route('/devolutivos')
def ob_devolutivos():
    return render_template('devolutivos.html')

#PRESTAR OBJETOS
@app.route('/prestar_objeto')
def prestar_objeto():
    return render_template('prestar_objeto.html')

# OBJETOS
@app.route('/objetos')
def ob_generales():
    return render_template('objetos.html')

# PRESTAMOS
@app.route('/prestamos')
def prestamos():
    return render_template('prestamos.html')

# MOSTRAR INVENTARIO
@app.route('/mostrar_inventario', methods=["GET", "POST"])
def inventario_objetos():
    return mostrar_inventario()

# MOSTRAR OBJETOS
@app.route('/mostrar_objetos', methods=["GET", "POST"])
def listar_objetos():
    return mostrar_objetos()

# MOSTRAR INSTRUCTORES
@app.route('/mostrar_instructores', methods=["GET", "POST"])
def listar_instructores():
    return mostrar_instructores()

# MOSTRAR ADMINISTRADORES
@app.route('/mostrar_administradores', methods=["GET", "POST"])
def listar_administradores():
    return mostrar_administradores()

# REDIRECCIONANDO CUANDO LA PAGINA NO EXISTE
@app.errorhandler(404)
def not_found(error):
    return redirect('/')

#USUARIOS
@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html')