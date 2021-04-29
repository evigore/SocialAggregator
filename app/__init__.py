from flask import Flask
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo

from config import Config

db = PyMongo()
bcrypt = Bcrypt()
bootstrap = Bootstrap()

def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(config_class)

	db.init_app(app)
	bcrypt.init_app(app)
	bootstrap.init_app(app)

	from app.auth import bp as auth_bp
	app.register_blueprint(auth_bp, url_prefix='/auth')

	from app.settings import bp as settings_bp
	app.register_blueprint(settings_bp, url_prefix='/settings')

	from app.main import bp as main_bp
	app.register_blueprint(main_bp)

	return app
