from flask import Blueprint, flash, render_template, request, url_for, redirect, flash, session, jsonify, make_response
#from app import socketio, emit
# from flask_wtf.csrf import CSRFProtect
from Models.date import Usuario, Empleados, Bitacora, Tipo_User
from db import db
from static.dicionario import *



ruta = Blueprint('ruta', __name__)
# csrf = CSRFProtect()

# notificaciones

"""
@socketio.on('event')
def event(json):
    print("Estamos de prueba"+json)
    emit('event', json) 
"""

@ruta.route("/notificaciones")
def notificaciones():
    return render_template('noti.html')

#Rutas_del_FrontEnd

@ruta.route("/")
def principal():
    return render_template('FrontEnd/index.html')

@ruta.route("/porque")
def porque():
    return render_template('FrontEnd/porque.html')

# funcion de session
def verificar_sesion():
    return 'prueba' in session

# rutas de emails
@ruta.route("/registro")
def registro():
    if verificar_sesion():
        tipo_usuario = Tipo_User.query.all()
        return render_template('auth/registro.html', tipo_usuario=tipo_usuario)
    else:
        mensaje = "Lo siento, debes iniciar sesión para acceder a esta página."
        return render_template('mensaje.html', mensaje=mensaje)
# ingreso de los datos del formulario de email


@ruta.route("/Datos", methods=['POST'])
def vacio2():
  
        name = request.form['usuario']
        name2 = request.form['password']
        name3 = request.form['id_tipo_usuario']
        me = Usuario(name, name2,name3)
        db.session.add(me)
        db.session.commit()
        return redirect(url_for("ruta.admin"))


@ruta.route("/actualizar/<id>", methods=['GET', 'PUT'])
def actualizar(id):
    if verificar_sesion(): 
        datos = Usuario.query.get(id)
        tipo_usuario = Tipo_User.query.all()
        if request.method == "GET":
            return render_template('auth/actualizar.html', datos=datos, tipo_usuario=tipo_usuario)
        req = request.get_json()
        if request.method == "PUT":
            datos.usuario = req['usuario']
            datos.password = req['password']
            datos.id_tipo_usuario = req['tipo_usuario']
            
            db.session.commit()

            return redirect(url_for("ruta.admin"))
    else:
        return render_template('mensaje.html')


@ruta.route("/Eliminar/<id>",methods=['DELETE'])
def Eliminar(id):
    if verificar_sesion() and request.method == 'DELETE':  
        eliminar = Usuario.query.get(id)  
        if eliminar:
            db.session.delete(eliminar)
            db.session.commit()

        return redirect(url_for("ruta.admin"))
    else:
        return render_template('mensaje.html')

# rutas de empleados

@ruta.route("/RegistroE")
def RegistroE():
    if verificar_sesion():    
        id_email = Usuario.query.all()
        return render_template('auth/RegistroEmpleado.html', id_email=id_email)
    else:
        return render_template('mensaje.html')
# ingreso de los datos de empleados
@ruta.route("/empleado", methods=['POST'])
def registro_empleado():
    if verificar_sesion():    
        dato_empleado0 = request.form['nombre']
        dato_empleado1 = request.form['rfc']
        dato_empleado2 = request.form['direccion']
        dato_empleado3 = request.form['grado_estudio']
        dato_empleado4 = request.form['edad']
        dato_empleado5 = request.form['puesto']
        dato_empleado6 = request.form['id_empleado']

        me = Empleados(dato_empleado0, dato_empleado1, dato_empleado2, dato_empleado3,
                    dato_empleado4, dato_empleado5, dato_empleado6)
        db.session.add(me)
        db.session.commit()

        return redirect(url_for("ruta.admin"))
    else:
        return render_template('mensaje.html')

@ruta.route("/actualizar_empleado/<id>", methods=['GET', 'PUT'])
def actualizar_empleados(id):
    if verificar_sesion():    
        datos = Empleados.query.get(id)
        if request.method == "GET":
            
            
            return render_template('auth/actulizar_empleados.html', datos=datos)

        req = request.get_json()
        if request.method == "PUT":
            
            
            datos.nombre = req['nombre']  
            datos.rfc = req['rfc']
            datos.direccion = req['direccion']
            datos.grado_estudio = req['grado_estudio']
            datos.edad = req['edad']
            datos.puesto = req['puesto']
            
            db.session.commit()
            
            return redirect(url_for("ruta.admin"))
    
    else:
        return render_template('mensaje.html')


  


@ruta.route("/Eliminarempleado/<id>",methods=['DELETE'])
def Eliminar_empleado(id):
    if verificar_sesion() and request.method == 'DELETE':       
        eliminar = Empleados.query.get(id)
        if eliminar:    
            db.session.delete(eliminar)
            db.session.commit()

        return redirect(url_for("ruta.admin"))
    else:
        return render_template('mensaje.html')
@ruta.route("/entrar")
def entrar():
    datos = Usuario.query.all()
    if request.method == 'GET':
        return render_template('login.html',datos=datos)

# Login
@ruta.route("/acceso", methods=['GET', 'POST'])
def acceso_al_sistema():
   
    if request.method == 'GET':
        return render_template('FrontEnd/login.html')

    name = request.form['usuario']
    name2 = request.form['password']
    if request.method == 'POST':
        me = db.session.query(Usuario).filter_by(
            usuario=name, password=name2).first()

    if (me != None):
        session['prueba'] = name
        session['id_usuario'] = me.id_usuario
        if (me.Tipo_User.id == 1):
            flash(Mensaje_admin, 'succes')
            return redirect(url_for("ruta.admin"))
        elif (me.Tipo_User.id == 2):

            return redirect(url_for("ruta.bit"))
        else:

            print("hubo algun error")
    else:
        flash(Login_crediciales, 'warning')
        return redirect(url_for("ruta.acceso_al_sistema")),me


@ruta.route("/admin", methods=['GET', 'POST', 'PUT','DELETE'])
def admin():
    datos_empleado = Empleados.query.all()
    user = Usuario.query.all()
    bit = Bitacora.query.all()
    if 'prueba' in session:   
           
            return render_template('auth/ultima.html', datos_empleado=datos_empleado, user=user,bit=bit)

    else:
        return render_template('mensaje.html')

 # sistema de logout
@ruta.route("/logout")
def logout():
    session.clear()
    flash(Logout, 'success')
    return redirect(url_for("ruta.acceso_al_sistema"))

# rutas de bitacora


@ruta.route("/bitacora")
def bit():
        if verificar_sesion():   
            id_usuario = session.get('id_usuario')
            if id_usuario is not None:
                dato_bit = Bitacora.query.all()
                usuario = Usuario.query.get(id_usuario)
            
                return render_template("auth/pagina_Bitacora.html",usuario=usuario,dato_bit=dato_bit)
        else:
            return render_template('mensaje.html')

@ruta.route("/registro_bitacora", methods=['POST'])
def registro_bitacora():

    if verificar_sesion():   
        name = request.form['dato_bitacora']
        name2 = request.form['comentarios']
        id = request.form['id']

        me = Bitacora(name, name2, id)
        db.session.add(me)
        db.session.commit()

        return redirect(url_for("ruta.bit"))
    else:
        return render_template('mensaje.html')


@ruta.route("/actualizar_bitacora/<id>", methods=['GET', 'PUT'])
def actualizar_bitacora(id):
    if verificar_sesion(): 
        datos = Bitacora.query.get(id)

        if request.method == "GET":
            return render_template('auth/actualizar_bitacora.html', datos=datos)
        req = request.get_json()
        if request.method == "PUT":

            datos.dato_bitacora = req['dato_bitacora']
            datos.comentarios = req['comentarios']
            db.session.commit()
            return redirect(url_for("ruta.admin"))
            
    else:
        return render_template('mensaje.html')


@ruta.route("/Eliminarbitacora/<id>",methods=['DELETE'])
def Eliminar_bitacora(id):
    if verificar_sesion() and request.method == 'DELETE':   
        eliminar = Bitacora.query.get(id)
        if eliminar:   
            db.session.delete(eliminar)
            db.session.commit()

        return redirect(url_for("ruta.admin"))
    else:
        return render_template('mensaje.html')


