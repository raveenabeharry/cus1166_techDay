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

@app.route("/get_all_contact", methods = ['GET'])
def get_all_contact():
    try:
        contacts = db.Contacts.find()
        return dumps(contacts)
    except getopt.GetoptError as e:
        return dumps({'error' : str(e)})































@app.route("/add_contact", methods = ['POST'])
def add_contact():
    try:
        data = json.loads(request.data)
        user_name = data['name']
        user_contact = data['contact']
        if user_name and user_contact:
            status = db.Contacts.insert_one({
                "name" : user_name,
                "contact" : user_contact})
        return dumps({'message' : 'SUCCESS'})
    except getopt.GetoptError as e:
        return dumps({'error' : str(e)})
ls
