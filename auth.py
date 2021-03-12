import re

class Auth:
	def __init__(self, db):
		self.db = db

	def register_user(self, login, password):
		if not self.__login_is_valid(login):
			raise Exception('Login format is invalid')

		if not self.__password_is_valid(password):
			raise Exception('Password format is invalid')

		user = self.db.users.find_one({'login': login})
		if user:
			raise Exception('User with login=' + login + ' exists')
	
		self.db.users.insert_one({'login': login, 'password': password})

	def __login_is_valid(self, login):
		# Минимальная длина 2. Начинается с буквы алфавита. Может содержать цифры и спец символы
		return not (re.search(r'^[a-zA-Z][a-zA-Z0-9-_\.]{1,20}$', login) is None)

	def __password_is_valid(self, password):
		# Как минимум одна маленькая/большая буква, минимум одна цифра/спец_символ. Длина от восьми символов
		return not (re.search(r'(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$', password) is None)
