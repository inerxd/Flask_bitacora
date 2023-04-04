from Models.date import Usuario
from Models.date import Empleados
from Models.date import Bitacora
from Models.date import Tipo_User
from db import db

class ModeloUsuario():

    def coincide(self,db,Usuario):
        coincide= Usuario(data[2])
        data=db
        if coincide:
            usuario_logueado=Usuario(data[0],data[1],None)
            return usuario_logueado
        else:
            return None
       
