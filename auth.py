import re

class Auth:
	def __init__(self, db, bcrypt):
		self.__db = db
		self.__bcrypt = bcrypt

	def register_user(self, login, password):
		if not self.__login_is_valid(login):
			raise Exception('Login format is invalid')

		if not self.__password_is_valid(password):
			raise Exception('Password format is invalid')

		user = self.__db.users.find_one({'login': login})
		if user:
			raise Exception('User with login=' + login + ' exists')
	
		self.__db.users.insert_one({'login': login, 'password': self.__bcrypt.generate_password_hash(password).decode('utf-8')})

	def login_user(self, login, password):
		if not self.__login_is_valid(login):
			raise Exception('Login format is invalid')

		if not self.__password_is_valid(password):
			raise Exception('Password format is invalid')

		user = self.__db.users.find_one({'login': login})
		if not (user and self.__bcrypt.check_password_hash(user['password'], password)):
			raise Exception("There's no account with pair " + login + '\\' + password)

	def __login_is_valid(self, login):
		# Минимальная длина 2. Начинается с буквы алфавита. Может содержать цифры и спец символы
		return not (re.search(r'^[a-zA-Z][a-zA-Z0-9-_\.]{1,20}$', login) is None)

	def __password_is_valid(self, password):
		# Как минимум одна маленькая/большая буква, минимум одна цифра/спец_символ. Длина от восьми символов
		return not (re.search(r'(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$', password) is None)
