
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('DATABASE_URI2')
db = SQLAlchemy(app)

from application import routes
