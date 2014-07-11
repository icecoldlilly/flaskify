from app import app,serializer,auth,db,api
from flask import Flask,url_for, jsonify,abort,request,g
from sqlalchemy.exc import IntegrityError,ArgumentError
from app.serializer import PhotoSerializer,UserSerializer
from flask.ext.restful import Resource,fields,reqparse
from app.models.Item import *
from app.models.User import *

#Here you would define all the CRUD actions you would perform on the items -- This is using the Flask-RestFUL API
#If you're looking for more details on implementation you could follow the guides made by Miguel Greenberg
class Items(Resource):
  decorators = [auth.login_required]
  def __init__(self):
    #Since 'description' is the only field set by the user, you would need to parse it from JSON.
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('description', type = str, required = True,help = 'Description wasnt provided', location = 'json')
        super(Items, self).__init__()
  def post(self):
    #Parse details from json to insert
    item = self.reqparse.parse_args()
    if len(item)==0:
      return {"message": "Bad data was inserted"}, 400
    currentUser=g.user

    #Part I: Adds the item to the database
    try:
      newItem=Item(currentUser.id,item.description)
      db.session.add(newItem)
      db.session.commit()
      return {'just_added':item},201
    except:
      db.session.rollback()
      return None

  def get(self):
    res=g.user.items()
    if not res:
      return {"message": "You don't have any items."}, 404
    else:
      serialized = ItemSerializer(res, many=True)
      return {"items": serialized.data},200

#This is a class set only for a single item operations -- GET & DELETE
class Item(Resource):
  decorators = [auth.login_required]
  #@auth.login_required
  def get(self,id):
    res=Item.query.get(id)
    if not res:
      return {"message": "Item could not be found."}, 404
    else:
      serialized = ItemSerializer(res)
      return {"outfit": serialized.data},200



  def delete(self,id):
    currentUser=g.user
    deletedItem=Item.query.get(id)
    if not res:
      return {"message": "Item could not be found."}, 404
    else:
      try:
        if (deletedItem.uid==currentUser.id):
          db.session.delete(res)
          db.session.commit()
          return {"just_deleted": res},204
        else:
          return {"message": "Item doesn't belong to you."}, 403
      except:
        db.session.rollback()
        return None
        

api.add_resource(Outfits, '/items')
api.add_resource(Outfit, '/items/<int:id>')
