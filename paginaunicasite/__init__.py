from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt #Biblioteca de cryptografia
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = '95021838e3388c6d77d038d6650edcfd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Faça o Login Primeiro'
login_manager.login_message_category = 'alert-info'


from paginaunicasite import routes