from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
mongo = MongoClient("localhost", 27017)
testDB = mongo["site"]

@app.route('/')
def index():
	return "Hello world"

def main():
	app.run(host='127.0.0.1', debug=True)

main()
