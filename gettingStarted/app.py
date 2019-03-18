from flask import Flask
from flask import request
from pymongo import MongoClient
from bson.json_util import dumps

client = MongoClient('localhost:27017')
db = client.db

app = Flask(__name__)

''' Creating GET REST API Using Python Flask and MongoDB
    Fetch the data from the MongoDB database through the
    .find() method from the MongoDB collection'''

@app.route("/get_all_users", methods = ['GET'])
def get_all_users():
    try:
        users = db.Users.find()
        return dumps(users)
    except getopt.GetoptError as e:
        return dumps({'error' : str(e)})
