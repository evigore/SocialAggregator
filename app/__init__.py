from flask import Flask
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap

from pymongo import MongoClient
from config import Config

bcrypt = Bcrypt()

#def create_app():
app = Flask(__name__)
app.config.from_object(Config)
	#app.run(host='127.0.0.1', debug=True)
bcrypt.init_app(app)

mongo = MongoClient(app.config['DB_HOST'], app.config['DB_PORT'])
db = mongo["site"]

bootstrap = Bootstrap()
bootstrap.init_app(app)
	#return app

from app import routes
#from app import auth
