from passlib.hash import bcrypt as pwd_context
#This serializier is different from Marshmallow, it uses Python's itsdangerous
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from sqlalchemy.ext.serializer import loads, dumps
from app import db,app
#Importing item -- you could delete or change based on needs
from Item import *
import datetime




ROLE_USER=1
ROLE_OWNER=0
#The model is tranlated to SQL when creating (migrating the database)
class User(db.Model):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32),unique=True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    email = db.Column(db.String(255),unique=True)
    #This is a relationship defined between items and the user who made them -- A many to one relationship -- You could delete if not needed
    #The relationship is defined using SQLAlchemy API
    items = db.relationship('Item', backref = 'submitted_by', lazy = 'dynamic')
    #This is where we store the password hash in the database
    password_hash = db.Column(db.String(64))
#Initialzing a user
    def __init__(self, username):
      self.username = username
#Authentication module in action -- Don't change unless you know how Flask-HTTPAuth works
    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=600):

        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.uid})
    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None    # valid token, but expired
        except BadSignature:
            return None    # invalid token
        user = User.query.get(data['id'])
        return user
