# A Minimal 'Flask-RestPlus' Restful API Server: ToDo-API with MongoDB

Followings are the objective achieved.

1. A self documented Restful API Server
2. User can add new 'Task'.
3. User can view a specific item or all the items
4. User can Update an Item by passing 'Task Name'
5. User can remove any item by passing 'Task Name'


 ![Server layout](/images/restful_server.PNG)
 
 ## Dependencies
 The project depend on the followings
 
   * Python 3.x. 
   * Flask + Flask Restplus
   * PyMongo
   * MongoDB
   * Isodate (necessary for Date Formatting)
   * Flask-Pymongo
  
## Quick Start
First we need to setup our necessary stuff (Python installation and MongoDB), after that navigate to the src folder in cmd and run using 'Python TaskListAPI'. Now you can access the API in browser at 'http://localhost:5000/'

## cURL examples
### Adding New Task to the Restful Server.
Creating New Task
<br/>`curl -d "{\"Task_Name\":\"Complete Workout\", \"Dead_Line\":\"2018-12-05\"}" -H "Content-Type: application/json" -X POST "http://localhost:5000/tasklist" -H "accept: application/json"`
<br/>Response: `{
    "response": "A New Task has been created."
}`

Create a already existing Task.
<br/>`curl -d "{\"Task_Name\":\"Complete Workout\", \"Dead_Line\":\"2018-12-05\"}" -H "Content-Type: application/json" -X POST "http://localhost:5000/tasklist" -H "accept: application/json"`
<br/>Response: `{
    "response": "Task with the same Name already exists."
}`
Create a Task with Missing Information.
<br/>`curl -d "{\"Task_Name\":\"Complete Workout\"}" -H "Content-Type: application/json" -X POST "http://localhost:5000/tasklist" -H "accept: application/json"`
<br/>Response: `{
    "errors": {
        "Dead_Line": "'Dead_Line' is a required property"
    },
    "message": "Input payload validation failed"
}`

### Query/Selecting Task(s)
Selecting all Tasks
<br/>`curl -X GET "http://127.0.0.1:5000/tasklist" -H "accept: application/json".`
<br/>Response: `{
  "response": [
    {
      "Created_Date": "2018-12-11",
      "Dead_Line": "2018-12-07",
      "Task_Name": "Complete Workout2"
    },
    {
      "Created_Date": "2018-12-11",
      "Dead_Line": "2018-01-01",
      "Task_Name": "WorkOut2"
    }
  ]
}`

Selecting a Single Task
<br/>`curl -X GET "http://127.0.0.1:5000/task/WorkOut2" -H "accept: application/json"`
<br/>Response: `{
  "data": {
    "Created_Date": "2018-12-11",
    "Dead_Line": "2018-01-01",
    "Task_Name": "WorkOut2"
  },
  "status": "ok"
}`

Selecting a non-existing Task 
<br/>`curl -X GET "http://127.0.0.1:5000/task/WorkOut3" -H "accept: application/json"`
<br/>Response: `{
    "response": "No task found for WorkOut3"
}`

### Updating Task using the API.
Updating a Task that does not exists
<br />`curl -X PUT "http://127.0.0.1:5000/tasklist" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"Task_Name\": \"WorkOut4\", \"Dead_Line\": \"2018-10-01\"}"`
<br/>Response: `{
    "response": "There is no Task with the given Name"
}`

Updating an existing Task
<br />`curl -X PUT "http://127.0.0.1:5000/tasklist" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"Task_Name\": \"WorkOut2\", \"Dead_Line\": \"2018-10-01\"}"`
<br/>Response: `{
  "response": "The Task has been updated."
}`

### Using API to Remove Task.
Removing a Task Does not exist
<br />`curl -X DELETE "http://localhost:5000/task/Workout" -H "accept: application/json"`
<br/> `{
    "response": "No task found for Workout, nothing can be removed"
}`

Removing an existing Task
<br />`curl -X DELETE "http://127.0.0.1:5000/task/Complete%20Workout2" -H "accept: application/json"`
<br/> `{
  "data": {
    "n": 1,
    "ok": 1
  },
  "status": "The Data has been removed"
}`
