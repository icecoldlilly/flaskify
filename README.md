#FLASKIFY

Ever tried to develop a web app using Python but didn't like how Django was configured? Hating on Django's ORM wishing you could use SQLAlchemy but afraid to break your system? You probably looked into flask or Pyramid and thought to yourself "Hmm.. That's nice but I don't want to start looking for extensions and prepare my system"



Maybe you hate how flask is organize (or more accurately. Not organized) Don't worry about it we got you hooked up with an MC structure. Flask is completely ready for you to write your own REST API without too much magic that Django / Rails include.

We also decided to include a migration system that would ease your work and increase your producativity. 
_____________
## ALL THE TOOLS ARE READY AND CONNECTED. ALL YOU HAVE TO DO IS DEVELOP!

_____________
#Componnents
Huge credit to Miguel Greenberg's work and Flask Mega tutorial as my understanding of flask mostly comes from his Mega Tutorial series and many of his flask extensions.

###Migration system and manage.py:
Alembic + Flask-Migrate + Flask-Script + sqlalchemy-migrate

###ORM: 
SQLAlchemy + Flask-SQLAlchemy

###JSON Serializer:
Marshamllow

###Basic Authentication system:
Flask-HTTPAuth + Flask-Login + pybcrypt + passlib + itsdangerous

###REST Tools:
Flask-RESTful 

###And of course the regular flask stuff such as Jinja2 templating engine and Werkzeug debugger


Implemntation details would come up soon as a first release, you're more than welcome to look through them Item / Items we setup in the Models / Controllers respectively.

