from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'QZJTt6VHV8rAsk3hkMMo3Zn8XzDxinj7'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://doagteifqovnvg:9be65b09c4b7245bb63f3c5ce57e50b25782dac60e4abeaf170f9e7f56276683@ec2-52-208-145-55.eu-west-1.compute.amazonaws.com:5432/d4mbg7ruiehmb'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskproductrating import routes