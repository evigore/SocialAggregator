from app import app
from flask import render_template

@app.errorhandler(404)
def not_found_error(error):
	return render_template('404.html')

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')
