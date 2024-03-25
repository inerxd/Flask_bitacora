from flask import Flask
from flask_socketio import SocketIO,emit
from werkzeug.exceptions import BadRequest
from db import db 



app = Flask(__name__)
socketio = SocketIO(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:padreDIOS1@localhost:5432/Proyecto'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


from routes.ruta import ruta
app.register_blueprint(ruta)


#sessions
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


#csrf.init_app(app)
app.secret_key = 'my_secret_key'
#relacion_app=app
