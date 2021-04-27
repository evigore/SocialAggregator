from app.main import bp
from flask import render_template

@bp.errorhandler(404)
def not_found_error(error):
	return render_template('404.html')

@bp.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')


@bp.route('/messages', methods=['GET', 'POST'])
def messages():
	return render_template('messages.html')

@bp.route('/contacts', methods=['GET', 'POST'])
def contacts():
	return render_template('contacts.html')

@bp.route('/user', methods=['GET', 'POST'])
def user():
	return render_template('user.html')
