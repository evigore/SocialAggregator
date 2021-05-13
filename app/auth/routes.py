from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user
from app import db
from app.auth import bp
from app.models import User
from app.auth.forms import SignupForm, LoginForm

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
	if current_user.is_authenticated:
		return redirect(url_for('main.index'))

	form = SignupForm()
	if form.validate_on_submit():
		user = User(username=form.username.data, email=form.email.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Congratulations, you are now a registered user!')
		return redirect(url_for('auth.login'))

	return render_template('auth/signup.html', title='Sign up', form=form)

@bp.route('/login', methods=['GET', 'POST'])
def login():
	return render_template('auth/login.html', title='Login', form=LoginForm())
