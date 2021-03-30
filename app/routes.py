from app import app
from flask import render_template

@app.errorhandler(404)
def not_found_error(error):
	return render_template('404.html')

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

"""
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

"""
