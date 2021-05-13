import re

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

class SignupForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign up')

	def validate_username(self, username):
		# Минимальная длина 2. Начинается с буквы алфавита. Может содержать цифры и спец символы
		if re.search(r'^[a-zA-Z][a-zA-Z0-9-_\.]{1,20}$', username.data) is None:
			return False

		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('Please use a different username.')


	def validate_password(self, password):
		# Как минимум одна маленькая/большая буква, минимум одна цифра/спец_символ. Длина от восьми символов
		return not (re.search(r'(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$', password.data) is None)

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError('Please use a different email.')

class LoginForm(FlaskForm):
	username = StringField('Username')
	password = PasswordField('Password')
	remember = BooleanField('Remember me?')
	submit = SubmitField('Login')
