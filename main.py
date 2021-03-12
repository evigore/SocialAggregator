from flask import Flask
from pymongo import MongoClient
from auth import Auth

app = Flask(__name__)
mongo = MongoClient("localhost", 27017)
siteDB = mongo["site"]
auth = Auth(siteDB)

def main():
	app.run(host='127.0.0.1', debug=True)

main()
