from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from flask_wtf.file import FileField

class EditSettingsForm(FlaskForm):
	username = StringField('Username')
	first_name = StringField('First name')
	last_name = StringField('Last name')
	email = StringField('Email')
	photo = FileField('Avatar')
	submit = SubmitField('Save changes')
