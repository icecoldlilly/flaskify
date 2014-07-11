from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.httpauth import HTTPBasicAuth
from flask.ext.restful import *
from app.controllers import *

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
api = Api(app)


auth = HTTPBasicAuth()
