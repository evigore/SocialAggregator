from app.main import bp
from flask import render_template
from flask_login import login_required

@bp.after_request
def add_header(response):
	response.headers['Cache-Control'] =  'no-cache, no-store'
	return response

@bp.errorhandler(404)
def not_found_error(error):
	return render_template('404.html')

@bp.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')

@login_required
@bp.route('/messages', methods=['GET', 'POST'])
def messages():
	return render_template('messages.html')

@login_required
@bp.route('/contacts', methods=['GET', 'POST'])
def contacts():
	return render_template('contacts.html')

@login_required
@bp.route('/user', methods=['GET', 'POST'])
def user():
	return render_template('user.html')
