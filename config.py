import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
	MONGO_URI = 'mongodb://127.0.01:27017/site'
	FLASK_ENV='development'
