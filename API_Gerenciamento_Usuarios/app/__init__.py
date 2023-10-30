from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:bruno2255@localhost/bdapi'
app.config['JWT_SECRET_KEY'] = "teste123"
db = SQLAlchemy(app)
jwt = JWTManager(app)

from app import routes
