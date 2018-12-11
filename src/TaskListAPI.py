from flask import Flask, jsonify, url_for, redirect, request
from flask_pymongo import PyMongo
from flask_restplus import Api, Resource, fields
import datetime
from jsonschema import FormatChecker


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/TasksDB"
mongo = PyMongo(app)
APP_URL = "http://127.0.0.1:5000"


api = Api(app,format_checker=FormatChecker(formats=("date",)), validate=True)
ns = api.namespace('todos', description='TODO operations')

parser = api.parser()
parser.add_argument('Task_Name', type=str, required=True, help='Task to be Updated')

task_model = api.model('ToDOList', {
        'Task_Name': fields.String(required=True, readOnly=True, description='The task unique identifier.'),
        'Dead_Line': fields.Date(required=True, description='The dead line for the task.', validate=True),
        'Description': fields.String(required=False, description='The Summary for the task.'),
        'Tags': fields.List(fields.String, required=False, description='The dead line for the task.' )
        })


@api.route('/tasklist', endpoint='Tasks List')
class ToDOList(Resource):

    def get(self):
        data = []
        cursor = mongo.db.todos.find({},{"_id":0})
        for todos in cursor:
            data.append(todos)
        return jsonify({"response": data})

    @ns.doc(params={'Task Model': 'All the neccesary Information for the Task.'})
    @ns.expect(task_model, validate=True)
    def post(self):
        data = request.get_json()
        if not data:
            data = {"response": "ERROR"}
            return jsonify(data)
        else:
            task = data.get('Task_Name')
            if task:
                if mongo.db.todos.find_one({"Task_Name": task}):
                    return {"response": "Task with the same Name already exists."}
                else:
                    now = datetime.datetime.now()
                    data['Created_Date'] = now.strftime("%Y-%m-%d")
                    mongo.db.todos.insert(data)
            else:
                return {"response": "Information Missing"}
        return {"response": "A New Task has been created."}

    @ns.expect(task_model, validate=True)
    def put(self):
        data = request.get_json()
        if not data:
            data = {"response": "ERROR"}
            return jsonify(data)
        else:
            task = data.get('Task_Name')
            if task:
                if mongo.db.todos.find_one({"Task_Name": task}):
                    mongo.db.todos.update({'Task_Name': task}, {'$set': data})
                    return {"response": "The Task has been updated."}
                else:
                    return {"response": "There is no Task with the given Name"}
            else:
                return {"response": "information missing"}
        return {"response": "Information missing"}


@api.route('/task/<Task_Name>')
class ToDOTASK(Resource):
    @api.expect('Task_Name')
    def get(self, Task_Name):
        task_info = mongo.db.todos.find_one({"Task_Name": Task_Name}, {"_id":0})
        if task_info:
            return jsonify({"status": "ok", "data": task_info})
        else:
            return {"response": "No task found for {}".format(Task_Name)}   
    
    @api.expect('Task_Name')
    def delete(self, Task_Name):
        data = []
        if Task_Name:
            task_info1 = mongo.db.todos.find({"Task_Name": Task_Name})
            for todos in task_info1:
                    data.append(todos)
            if len(data)>=1:
                task_info = mongo.db.todos.remove({"Task_Name": Task_Name})
                return jsonify({"status": "The Data has been removed", "data": task_info})
            else:
                return {"response": "No task found for {}, nothing can be removed".format(Task_Name)}
        else:
            return {"response": "You have not provided Task_Name"}


if __name__ == "__main__":
    app.run(debug=True)
