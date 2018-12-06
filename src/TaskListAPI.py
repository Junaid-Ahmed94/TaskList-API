from flask import Flask, jsonify, url_for, redirect, request
from flask_pymongo import PyMongo
from flask_restplus import Api, Resource, fields, marshal
import datetime
from jsonschema import FormatChecker


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/TasksDB"
mongo = PyMongo(app)
APP_URL = "http://127.0.0.1:5000"


api = Api(app,format_checker=FormatChecker(formats=("date",)), validate=True)

ns = api.namespace('todos', description='TODO operations')

task_model = api.model('ToDOList', {
        'Task_Name': fields.String(required=True, readOnly=True, description='The task unique identifier.'),
        'Dead_Line': fields.Date(required=True, description='The dead line for the task.', validate=True),
        'Description': fields.String(required=False, description='The Summary for the task.'),
        'Tags': fields.List(fields.String, required=False, description='The dead line for the task.' )
        })

class ToDOList(Resource):
    def get(self, task=None):
        data = []

        if task:
            task_info = mongo.db.todos.find_one({"Task_Name": task['Task_Name']})
            if task_info:
                return jsonify({"status": "ok", "data": task_info})
            else:
                return {"response": "no task found for {}".format(task['item_Name'])}
        else:
            cursor = mongo.db.todos.find({}, {"_id": 0})
            for todos in cursor:
                print(todos)
                #one_task['url'] = APP_URL + url_for('ToDos') + "/" + one_task.get('item_Name')
                data.append(todos)
            return jsonify({"response": data})

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
                return {"response": "information missing"}
        return redirect(url_for("ToDos"))
   
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

    def delete(self, registration):
        mongo.db.student.remove({'registration': registration})
        return redirect(url_for("students"))

class Index(Resource):
    def get(self):
        return redirect(url_for("tasks"))

api.add_resource(Index, "/", endpoint="index")
api.add_resource(ToDOList, "/api", endpoint="ToDos")

if __name__ == "__main__":
    app.run(debug=True)

