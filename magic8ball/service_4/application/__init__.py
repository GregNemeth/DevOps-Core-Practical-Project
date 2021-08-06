from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db" #f"mysql+pymysql://root:{os.getenv('MYSQL_ROOT_PASSWORD')}@mysql:3306/flask-db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

from application import routes