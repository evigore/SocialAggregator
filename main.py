from flask import Flask
from pymongo import MongoClient
from auth import Auth
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

mongo = MongoClient("localhost", 27017)
site_db = mongo["site"]

auth = Auth(site_db, bcrypt)

@app.route('/login/<string:login>/<string:pw>')
def login(login, pw):
	return str(auth.login_user(login, pw))

@app.route('/signup/<string:login>/<string:pw>')
def signup(login, pw):
	try:
		auth.register_user(login, pw)
	except Exception as e:
		return str(e)

	return 'Success'

def main():
	app.run(host='127.0.0.1', debug=True)

main()
