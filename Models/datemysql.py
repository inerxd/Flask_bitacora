from db import db

class User (db.Model):
    __tablename__ = 'User'
    id_user = db.Column(db.Integer, primary_key=True,nullable=False)
    empleado_relacion = db.relationship('Employees', backref='User', lazy=True)
    bitacora_relacion = db.relationship('Binnacle', backref='User', lazy=True)
    User_Type_id_User_Type = db.Column(db.Integer, db.ForeignKey('User_Type.id_User_Type'))
    email = db.Column(db.String(45), unique=True, nullable=False)
    password = db.Column(db.String(45), unique=True, nullable=False)

    def __init__(self,email,password,User_Type_id_User_Type):
        self.email = email
        self.password = password
        self.User_Type_id_User_Type = User_Type_id_User_Type    

class User_Type (db.Model):
    __tablename__ = 'User_Type'
    id_User_Type = db.Column(db.Integer, primary_key=True,nullable=False)
    user_type = db.Column(db.String(45), unique=True, nullable=False)
    Tipo_User_relacion = db.relationship('User', backref='User_Type', lazy=True)

    def __init__(self,user_type,):
        self.user_type = user_type

class Employees (db.Model):
    __tablename__ = 'Employees'
    id_Employees = db.Column(db.Integer, primary_key=True,nullable=False)
    User_id_User = db.Column(db.Integer, db.ForeignKey('User.id_user'))
    name = db.Column(db.String(100), unique=True, nullable=False)
    rfc = db.Column(db.String(100), unique=True, nullable=False)
    adress = db.Column(db.String(200), unique=True, nullable=False)
    study_grade = db.Column(db.String(500), unique=True, nullable=False)
    age = db.Column(db.Integer, unique=True, nullable=False)
    position = db.Column(db.String(100), unique=True, nullable=False)
   
    
    def __init__(self,name,rfc,adress,study_grade,age,position,User_id_User):
        self.name = name
        self.rfc = rfc
        self.adress = adress
        self.study_grade = study_grade
        self.age = age
        self.position = position
        self.User_id_User = User_id_User

class Binnacle (db.Model):
    __tablename__ = 'Binnacle'
    id_Binnacle = db.Column(db.Integer, primary_key=True,nullable=False)
    User_id_User = db.Column(db.Integer, db.ForeignKey('User.id_user'))
    log_data = db.Column(db.String(1000), unique=True, nullable=False)
    comments = db.Column(db.String(1000), unique=True, nullable=False)

    def __init__(self,log_data,comments,User_id_User):
        self.log_data = log_data
        self.comments = comments
        self.User_id_User = User_id_User