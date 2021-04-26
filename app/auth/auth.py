from app import db, bcrypt
from app.auth import bp
import re

class Auth:
	def register_user(self, login, password):
		if not self.__login_is_valid(login):
			raise Exception('Login format is invalid')

		if not self.__password_is_valid(password):
			raise Exception('Password format is invalid')

		user = db.users.find_one({'login': login})
		if user:
			raise Exception('User with login=' + login + ' exists')
	
		db.users.insert_one({'login': login, 'password': bcrypt.generate_password_hash(password).decode('utf-8')})

	def login_user(self, login, password):
		if not self.__login_is_valid(login):
			raise Exception('Login format is invalid')

		if not self.__password_is_valid(password):
			raise Exception('Password format is invalid')

		user = db.users.find_one({'login': login})
		if not (user and bcrypt.check_password_hash(user['password'], password)):
			raise Exception("There's no account with pair " + login + '\\' + password)

	def __login_is_valid(self, login):
		# Минимальная длина 2. Начинается с буквы алфавита. Может содержать цифры и спец символы
		return not (re.search(r'^[a-zA-Z][a-zA-Z0-9-_\.]{1,20}$', login) is None)

	def __password_is_valid(self, password):
		# Как минимум одна маленькая/большая буква, минимум одна цифра/спец_символ. Длина от восьми символов
		return not (re.search(r'(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$', password) is None)
