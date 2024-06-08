from flask import session, request, render_template
from conexion.conexionBD import connectionBD

# FUNCION LOGIN
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

# FUNCION BUSCAR OBJETO
def BuscarObjeto():
    try:
        if request.method == "POST":
            search = request.form['buscar']
            connection = connectionBD()
            cur = connection.cursor(dictionary=True)
            cur.execute("SELECT * FROM productosgenerales WHERE NombreProducto LIKE %s ORDER BY id DESC", (f"%{search}%",))
            resultadoBusqueda = cur.fetchall()
            cur.close()
            return render_template('resultadoBusqueda.html', miData=resultadoBusqueda, busqueda=search)
    except Exception as e:
        print(f"Error en la función BuscarObjeto: {e}")
    finally:
        if connection.is_connected():
            connection.close()
    return render_template('/')

# MOSTRAR OBJETOS
def mostrar_objetos():
    try:
        connection = connectionBD()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM productosgenerales")
        objetos = cursor.fetchall()
        cursor.close()
        connection.close()
        return render_template("objetos.html", objetos=objetos)
    except Exception as e:
        print(f"Error en la función mostrar_objetos: {e}")
    finally:
        if connection.is_connected():
            connection.close()
