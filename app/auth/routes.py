from flask import render_template
from app import db
from app.auth import bp
from app.auth.forms import SignupForm

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
	return render_template('auth/signup.html', title='Sign up', form=SignupForm())
