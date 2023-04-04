from db import db 
from werkzeug.security import check_password_hash,generate_password_hash



class Usuario (db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.Integer, primary_key=True,nullable=False)
    bitacora_relacion = db.relationship('Bitacora', backref='Usuario', lazy=True)
    id_tipo_usuario = db.Column(db.Integer, db.ForeignKey('Tipo_User.id'))
    empleado = db.Column(db.Integer, db.ForeignKey('empleados.id_empleado'))
    usuario = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(102), unique=True, nullable=False)
    

    

    def __init__(self,usuario,password):
        self.usuario = usuario
        self.password = password
        
    
    


class Empleados (db.Model):
    __tablename__ = 'empleados'
    id_empleado = db.Column(db.Integer, primary_key=True,nullable=False)
    usuario_relacion = db.relationship('Usuario', backref='empleados', lazy=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)
    rfc = db.Column(db.String(100), unique=True, nullable=False)
    direccion = db.Column(db.String(200), unique=True, nullable=False)
    grado_estudio = db.Column(db.String(500), unique=True, nullable=False)
    edad = db.Column(db.Integer, unique=True, nullable=False)
    puesto = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self,nombre,rfc,direccion,grado_estudio,edad,puesto):
        self.nombre = nombre
        self.rfc = rfc
        self.direccion = direccion
        self.grado_estudio = grado_estudio
        self.edad = edad
        self.puesto = puesto

class Bitacora (db.Model):
    __tablename__ = 'bitacora'
    id_bitacora = db.Column(db.Integer, primary_key=True,nullable=False)
    usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    dato_bitacora = db.Column(db.String(100000), unique=True, nullable=False)
    comentarios = db.Column(db.String(100000), unique=True, nullable=False)

    def __init__(self,dato_bitacora,comentarios):
        self.dato_bitacora = dato_bitacora
        self.comentarios = comentarios
    
class Tipo_User(db.Model):
    __tablename__ = 'Tipo_User'
    id = db.Column(db.Integer, primary_key=True,nullable=False)
    tipo_usuarios = db.Column(db.String(100), unique=True, nullable=False)
    Tipo_User_relacion = db.relationship('Usuario', backref='Tipo_User', lazy=True)

    def __init__(self,tipo_usuarios):
        self.tipo_usuarios = tipo_usuarios
      
   
       






        
