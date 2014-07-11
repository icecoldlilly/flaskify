#!py-env/bin/python
from flask import Flask
from app import app
from app.controllers import Authenticate, Outfits,UserInteraction

#Keep as boilerplate for rest
# from app.models.Location import *
# from app.models.Photo import *
# from app.models import OutfitTransaction
# from app.models.User import *

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug = True)
