from flask import Flask
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
#from flask_pymongo import PyMongo
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from redis import Redis

from config import Config

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
bootstrap = Bootstrap()

login = LoginManager()
login.login_view = 'auth.login'
login.login_message = 'Please log in to access this page.'

def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(config_class)

	db.init_app(app)
	migrate.init_app(app, db)
	login.init_app(app)
	bcrypt.init_app(app)
	bootstrap.init_app(app)

	from app.auth import bp as auth_bp
	app.register_blueprint(auth_bp, url_prefix='/auth')

	from app.settings import bp as settings_bp
	app.register_blueprint(settings_bp, url_prefix='/settings')

	from app.main import bp as main_bp
	app.register_blueprint(main_bp)

	return app

from app import models
