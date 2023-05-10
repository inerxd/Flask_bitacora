from flask import Blueprint, flash,render_template, request, url_for,redirect,flash,session,jsonify,make_response
#from flask_wtf.csrf import CSRFProtect
from Models.date import Usuario
from Models.date import Empleados
from Models.date import Bitacora
from Models.date import Tipo_User
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
   
    tipo_usuario = Tipo_User.query.all()
  
    usuarios = Usuario.query.join(Tipo_User).add_columns(Tipo_User.tipo_usuarios).all()

    return render_template('auth/registro.html', tipo_usuario=tipo_usuario, usuarios=usuarios)


@ruta.route("/Datos",methods=['POST'])
def vacio2():
    
    name = request.form['usuario']
    name2 = request.form['password']
    name3 = request.form['id_tipo_usuario']
    me = Usuario(name, name2,name3)
    db.session.add(me)
    db.session.commit()
    
    return redirect(url_for("ruta.admin"))

@ruta.route("/actualizar/<id>",methods=['GET','PUT'])
def actualizar(id):
    datos = Usuario.query.get(id)
    tipo_usuario = Tipo_User.query.all()
 
   
    
    if request.method == "GET":
        return render_template('auth/actualizar.html',datos=datos,tipo_usuario=tipo_usuario)
    req = request.get_json()
    if request.method == "PUT":
        
        datos.usuario = req['usuario']    
        datos.password = req['password']
        datos.id_tipo_usuario = req['tipo_usuario']
        
        
        db.session.commit()
        return redirect(url_for("ruta.admin"))        
        

    

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



    

@ruta.route("/acceso",methods=['GET','POST','PUT'])
def acceso_al_sistema():

    if  request.method == 'GET':
        return  render_template('auth/login.html')

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
            
              return redirect(url_for("ruta.bit"))
        else:
           
            print("hubo algun error")
    else:
        flash(Login_crediciales,'warning')
        return redirect(url_for("ruta.acceso_al_sistema"))


@ruta.route("/admin",methods=['GET','POST','PUT'])
def admin():
    datos_empleado = Empleados.query.all()
    user  = Usuario.query.all()
    bit = Bitacora.query.all()
 
    if 'prueba' in session:
            
            return render_template('auth/admin.html',datos_empleado=datos_empleado,user=user,bit=bit) 
        
    else: 
        return redirect(url_for("ruta.login"))
    

 # logout
@ruta.route("/logout")
def logout():
    session.clear()
    flash(Logout,'success')
    return redirect(url_for("ruta.acceso_al_sistema"))

@ruta.route("/actualizar_empleado/<id>",methods=['GET','PUT'])
def actualizar_empleados(id):
    datos = Empleados.query.get(id)
    if request.method == "GET":
        return render_template('auth/actulizar_empleados.html',datos=datos)
    
    req = request.get_json()
    try :
        if request.method == "PUT":
           

            
            datos.nombre = req['nombre']    
            datos.rfc = req['rfc']
            datos.direccion = req['direccion']    
            datos.grado_estudio = req['grado_estudio']
            datos.edad = req['edad']    
            datos.puesto = req['puesto']
            
            db.session.commit()     
            return redirect(url_for("ruta.admin"))
            
    except:               
            print("Algo salió mal")
    
    

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


#1 rutas de bitacora 

@ruta.route("/registro_bitacora",methods=['POST'])
def registro_bitacora():
  
    
    id = int(request.form['id']) 
    name = request.form['dato_bitacora']
    name2 = request.form['comentarios']
    
    me = Bitacora(name, name2,id)
    db.session.add(me)
    db.session.commit()

    return redirect(url_for("ruta.bit"))

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

@ruta.route("/bit")
def bit():
    
    if 'prueba' in session:
        nombre_bitacora = Bitacora.query.all()
        datos = Usuario.query.all()
        return render_template ('auth/vistabit.html',nombre_bitacora=nombre_bitacora,datos=datos) 
    else:
        return redirect(url_for("ruta.acceso_al_sistema"))

@ruta.route("/replazo")
def replazo():

    return render_template ("replazo.html")
    








