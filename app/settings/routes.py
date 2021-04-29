from flask import render_template
from app import db
from app.settings import bp
#from app.auth.forms import SignupForm, LoginForm

@bp.after_request
def add_header(response):
	response.headers['Cache-Control'] =  'no-cache, no-store'
	return response

@bp.route('/', methods=['GET', 'POST'])
def general():
	return render_template('settings/general.html')#, title='Sign up', form=SignupForm())
