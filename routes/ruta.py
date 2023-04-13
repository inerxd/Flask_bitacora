from flask import Blueprint, flash,render_template, request, url_for,redirect,flash,session,jsonify,make_response
#from flask_wtf.csrf import CSRFProtect
from Models.date import Usuario
from Models.date import Empleados
from Models.date import Bitacora
from Models.date import Tipo_User
from Models.correos import ModeloUsuario
from db import db
from static.dicionario import *




ruta = Blueprint('ruta', __name__)
#csrf = CSRFProtect()

# rutas de normales
@ruta.route("/")
def principal():
    return render_template('index.html')



   
# rutas de emails
@ruta.route("/registro")
def registro():

    return render_template('auth/registro.html')


@ruta.route("/Datos",methods=['POST'])
def vacio2():
    
    name = request.form['usuario']
    name2 = request.form['password']
    
    me = Usuario(name, name2)
    db.session.add(me)
    db.session.commit()
    
    return redirect(url_for("ruta.login"))

@ruta.route("/actualizar/<id>",methods=['GET','POST'])
def actualizar(id):
    datos = Usuario.query.get(id)
    if request.method == "POST":
        
        datos.usuario = request.form['usuario']    
        datos.password = request.form['password']
        
        db.session.commit()
        
        return redirect(url_for("ruta.admin"))

    
    return render_template('auth/actualizar.html',datos=datos)

# rutas de empleados

# pagina de registro
@ruta.route("/RegistroE")
def RegistroE():
    return render_template ('auth/RegistroEmpleado.html')


@ruta.route("/empleado",methods=['POST'])
def registro_empleado():
    
    dato_empleado0 = request.form['nombre']
    dato_empleado1 = request.form['rfc']
    dato_empleado2 = request.form['direccion']
    dato_empleado3 = request.form['grado_estudio']
    dato_empleado4 = request.form['edad']
    dato_empleado5 = request.form['puesto']
    
    me = Empleados(dato_empleado0,dato_empleado1,dato_empleado2,dato_empleado3,
    dato_empleado4,dato_empleado5)
    db.session.add(me)
    db.session.commit()

    return redirect(url_for("ruta.acceso"))

@ruta.route("/login",methods=['GET'])
def login():
    
    return render_template('auth/login.html')

    

@ruta.route("/acceso",methods=['GET','POST'])
def acceso_al_sistema():
        
    resp = make_response("")
    name = request.form['usuario']
    name2 = request.form['password']
    if  request.method == 'POST':
        me = db.session.query(Usuario).filter_by(usuario=name,password=name2).first()

    if(me!=None):
        session['prueba'] = name
        if(me.Tipo_User.id==1):
            flash(Mensaje_admin,'succes')
            return redirect(url_for("ruta.admin"))
        elif(me.Tipo_User.id==2):
            
            return render_template('auth/bitacora.html')
        else:
           
            print("hubo algun error")
    else:
        flash(Login_crediciales,'warning')
        return redirect(url_for("ruta.login"))

@ruta.route("/admin",methods=['GET','POST'])
def admin():
    datos_empleado = Empleados.query.all()
    user  = Usuario.query.all()
    if 'prueba' in session:
            
            return render_template('auth/admin.html',datos_empleado=datos_empleado,user=user) 
        
    else: 
        return redirect(url_for("ruta.login"))
    

 # logout
@ruta.route("/logout")
def logout():
    session.clear()
    flash(Logout,'success')
    return redirect(url_for("ruta.login"))
"""
    resp = make_response("")
    datos_empleado = Empleados.query.all()
    resp.set_cookie( 'datose' , value = 'datos_empleado' , max_age = 1500 , expires = None , path = '/' , domain = None , secure = False , httponly = False , samesite = None )
    user  = Usuario.query.all()
    resp.set_cookie( 'datosr' , value = 'user' , max_age = 1500 , expires = None , path = '/' , domain = None , secure = False , httponly = False , samesite = None )
    name = request.form['usuario']
    name2 = request.form['password']
    me = db.session.query(Usuario).filter_by(usuario=name,password=name2).first()
    
    if(me!=None):
        session['prueba'] = name
        if(me.Tipo_User.id==1):
            return render_template('auth/admin.html',datos_empleado = request.cookies.get('datose'),user = request.cookies.get('datosr'), bita=request.cookies.get('datost') ) 
        elif(me.Tipo_User.id==2):
            return render_template('auth/bitacora.html')
        elif ('prueba' in session):
            return render_template ('auth/admin.html')
        else:
            return redirect(url_for("ruta.login"))
        
        
        
    else: 
        return render_template('index.html')"""
    
        



#recreacion lo que hice anteriormente
"""
@ruta.route("/acceso",methods=['GET','POST'])
def acceso_al_sistema():
   
    datos_empleado = Empleados.query.all()
   
    user  = Usuario.query.all()
  
   
    name = request.form['usuario']
    name2 = request.form['password']
    me = db.session.query(Usuario).filter_by(usuario=name,password=name2).first()
    
    if(me!=None):
        session['prueba'] = name
        if(me.Tipo_User.id==1):
            return render_template('auth/prueba.html',datos_empleado = datos_empleado ,user = user ) 
        elif(me.Tipo_User.id==2):
            return render_template('auth/bitacora.html')
        else:
            print("hubo algun error")
    else: 
        return render_template('index.html')
    """











#cookies
@ruta.route("/l")
def cookies():
   
    #creamos la respuesta
    resp = make_response("")
    #almacenamos las cookies
    resp.set_cookie('username','username_1')
    #retornamos la respuesta
    return resp
    
@ruta.route("/actualizar_json/<id>",methods=['GET'])
def actualizar_json(id):
    datos = Empleados.query.get(id)

   
    return render_template('auth/actulizar_empleados.html',datos=datos)

@ruta.route("/actualizar_empleado/<id>",methods=['PUT'])
def actualizar_empleados(id):
    datos = Empleados.query.get(id)
    req = request.get_json()

    print(req)

    res = make_response(jsonify({"message:":"JSON received"}),200)
    return res

"""
@ruta.route("/actualizar_empleado/<id>",methods=['GET','POST'])
def actualizar_empleados(id):
    datos = Empleados.query.get(id)
    if request.method == "POST":
        
        datos.nombre = request.form['nombre']    
        datos.rfc = request.form['rfc']
        datos.direccion = request.form['direccion']    
        datos.grado_estudio = request.form['grado_estudio']
        datos.edad = request.form['edad']    
        datos.puesto = request.form['puesto']
        
        db.session.commit()
        
        return redirect(url_for("ruta.admin"))

    
    return render_template('auth/actulizar_empleados.html',datos=datos)"""




@ruta.route("/Eliminar/<id>")
def Eliminar(id):
    eliminar = Usuario.query.get(id)
    db.session.delete(eliminar)
    db.session.commit()
   
    return redirect(url_for("ruta.admin"))

@ruta.route("/Eliminarempleado/<id>")
def Eliminar_empleado(id):
    eliminar = Empleados.query.get(id)
    db.session.delete(eliminar)
    db.session.commit()

    return redirect(url_for("ruta.admin"))

"""
@ruta.route("/admin")
def admin():
   
    if 'prueba' in session:
        empleado  = Empleados.query.all()
        return render_template ('auth/admin.html',empleado=empleado)
    else:
        return redirect(url_for("ruta.login"))
"""
#1 rutas de bitacora 
@ruta.route("/bitacora",methods=['GET','POST'])
def bitacora():

    
    if 'prueba' in session:
        nombre_bitacora = Bitacora.query.all()
        return render_template ('auth/bitacora.html',nombre_bitacora=nombre_bitacora) 
    else:
        return redirect(url_for("ruta.login"))
@ruta.route("/registro_bitacora",methods=['POST'])
def registro_bitacora():

   
    name = request.form['dato_bitacora']
    name2 = request.form['comentarios']
    
    me = Bitacora(name, name2)
    db.session.add(me)
    db.session.commit()

    return redirect(url_for("ruta.bitacora"))

@ruta.route("/Eliminarbitacora/<id>")
def Eliminar_bitacora(id):
    eliminar = Bitacora.query.get(id)
    db.session.delete(eliminar)
    db.session.commit()

    return redirect(url_for("ruta.bitacora"))

@ruta.route("/actualizar_bitacora/<id>",methods=['GET','POST'])
def actualizar_bitacora(id):
    datos = Bitacora.query.get(id)
    if request.method == "POST":
        
        datos.dato_bitacora = request.form['dato_bitacora']    
        datos.comentarios = request.form['comentarios']
        db.session.commit()
        
        return redirect(url_for("ruta.bitacora"))

    
    return render_template('auth/actualizar_bitacora.html',datos=datos)

@ruta.route("/porque")
def porque():
    return render_template('porque.html')

    








