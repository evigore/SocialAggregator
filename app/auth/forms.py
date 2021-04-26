from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField

class SignupForm(FlaskForm):
	username = StringField('Username')
	email = StringField('Email')
	password = PasswordField('Password')
	password2 = PasswordField('Repeat Password')
	submit = SubmitField('Register')
