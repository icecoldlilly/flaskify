from app import app,serializer,auth,db
from flask import Flask,url_for, jsonify,abort,request,g
from sqlalchemy.exc import IntegrityError,ArgumentError
from app.serializer import UserSerializer
from app.models.Photo import *
from app.models.User import *

class Authenticate():

  @app.route('/users', methods=['POST'])
  def new_user():
      username = request.json.get('username')
      password = request.json.get('password')
      if username is None or password is None:
          abort(400)    # missing arguments
      if User.query.filter_by(username=username).first() is not None:
          abort(400)    # existing user
      user = User(username=username)
      user.hash_password(password)
      db.session.add(user)
      db.session.commit()
      return (jsonify({'username': user.username}), 201,
              {'Location': url_for('get_user', id=user.uid, _external=True)})

  @app.route('/users/<id>', methods=['GET'])
  def get_user(id):
      res = User.query.get(id)
      if not res:
          abort(400)
          return jsonify({"message": "Outfit could not be found."}), 400
      serialized = UserSerializer(res)
      return jsonify({"user": serialized.data})
  @app.route('/token', methods=['GET'])
  @auth.login_required
  def get_auth_token():
      token = g.user.generate_auth_token(600)
      return jsonify({'token': token.decode('ascii'), 'duration': 600})

  @auth.verify_password
  def verify_password(username_or_token, password):
      # first try to authenticate by token
      user = User.verify_auth_token(username_or_token)
      if not user:
          # try to authenticate with username/password
          user = User.query.filter_by(username=username_or_token).first()
          if not user or not user.verify_password(password):
              return False
      g.user = user
      return True
