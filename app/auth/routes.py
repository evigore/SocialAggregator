from flask import render_template
from app import db
from app.auth import bp
from app.auth.forms import SignupForm, LoginForm

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
	return render_template('auth/signup.html', title='Sign up', form=SignupForm())

@bp.route('/login', methods=['GET', 'POST'])
def login():
	return render_template('auth/login.html', title='Login', form=LoginForm())
