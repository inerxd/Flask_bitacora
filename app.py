from flask import Flask, redirect, render_template, request, url_for
#from db import magia
#from tablas import metadata
#from sqlalchemy import insert
#from sqlalchemy import values
#from sqlalchemy.sql import select

from werkzeug.exceptions import BadRequest
from flask_sqlalchemy import SQLAlchemy
from db import db 
from routes.ruta import ruta
#from flask_wtf.csrf import CSRFProtect
#from routes.ruta import csrf

app = Flask(__name__)

app.register_blueprint(ruta)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:padreDIOS1@localhost:5432/Proyecto'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

#sessions
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


#csrf.init_app(app)
app.secret_key = 'my_secret_key'
#relacion_app=app



"""
@app.route("/")
def principal():
    return render_template('index.html')

@app.route("/login",methods=['GET'])
def login():
    Email  = Emails.query.all()
   #  s = select([login])
   #  rp = magia.execute(s)
    # results = rp.fetchall()
   #  print(results)
    #datos=results
    return render_template('auth/login.html',Email=Email)

@app.route("/registro",methods=['GET'])
def registro():

    return render_template('auth/registro.html')

@app.route("/Datos",methods=['POST','PUT'])
def vacio2():

    name = request.form['email']
    name2 = request.form['password']
    name3 = request.form['password2']
    me = Emails(name, name2,name3)
    db.session.add(me)
    db.session.commit()
   
   #  ins = login.insert()
    # result = magia.execute(
    #     ins,
      #   email=name,
      #   password=name2
       #  )
   
    return render_template('auth/login.html')
            
@app.route("/lenguajes")
def mostrarlenguajes():
    mislenguajes = ("php", "ruby", "c#", "angular", "c++",
                    "javascript", "java", "typescript")
    return render_template('lenguajes.html', lenguajes=mislenguajes)


@app.route("/saludo/<nombre>")
def saludo(nombre):
    # return 'hola codi!'
    return 'hola,{0}!'.format(nombre)
"""

