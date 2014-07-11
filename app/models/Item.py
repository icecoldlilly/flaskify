from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from sqlalchemy.ext.serializer import loads, dumps
from app import db,app
import datetime


class Item(db.Model):
    __tablename__='photo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False )
    uid = db.Column(db.Integer, db.ForeignKey('user.uid'))
    description = db.Column(db.Text, nullable=False)
    date=db.Column(db.DateTime, default=datetime.datetime.utcnow)
    #Initializing an item
    def __init__(self,uid,description):
      self.uid = uid
      self.description = description