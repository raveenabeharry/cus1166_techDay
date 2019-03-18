from flask import Flask, request
from pymongo import MongoClient
from bson.json_util import dumps

client = MongoClient('local.host:27017')
db = client.db

app = Flask(__name__)


''' Creating GET REST API Using Python Flask and MongoDB
    Fetch the employee data from the MongoDB database through the
    .find() method from the MongoDB collection'''
@app.route("/getEmployees", methods = ['GET'])
def get_all_employees():
    try:
        employees = db.Employees.find()
        return dumps(contacts)
    except getopt.GetoptError as e:
        return dumps({'error': str(e)})

'''Renders the Employee template'''
@app.route("/addEmployee")
def employeeForm():
    render_template("EmployeeForm.html")

'''Will display new employees and accept as POST requests to add
to MongoDB  '''
@app.route("/newEmployee", methods = ['POST'])
def add_employee():
    try:
        data = json.loads(request.data)  '''load the json data'''
        employee_name = form.get("name")
        employee_contact = form.get("contact")
        employee_hours = form.get("hours")

        '''validate the data before inserting it into MongoDB collection'''
        if employee_name and employee_contact and employee_hours:
            status = db.Employees.insertOne({
            "name": employee_name,
            "contact": employee_contact,
            "hours": employee_hours})
        return dump({'message':'SUCCESS'})  '''once the data has been successfully
        inserted you will get a SUCCESS message'''
        #return render_template("newEmployee.html")
    except getopt.GetoptError as e:
        return dumps({'error' : str(e)})
