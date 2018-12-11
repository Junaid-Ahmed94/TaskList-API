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
###Adding New Task to the Restful Server.
Creating New Task
<br/>`curl -d "{\"Task_Name\":\"Complete Workout\", \"Dead_Line\":\"2018-12-05\"}" -H "Content-Type: application/json" -X POST "http://localhost:5000/tasklist" -H "accept: application/json"`
`{
    "response": "A New Task has been created."
}`

Create a already existing Task.
<br/>`curl -d "{\"Task_Name\":\"Complete Workout\", \"Dead_Line\":\"2018-12-05\"}" -H "Content-Type: application/json" -X POST "http://localhost:5000/tasklist" -H "accept: application/json"`
{
    "response": "Task with the same Name already exists."
}
Updating Old Task using the API.
<br />`curl -d "{\"Task_Name\":\"Complete Workout\", \"Dead_Line\":\"2018-12-07\"}" -H "Content-Type: application/json" -X PUT "http://localhost:5000/tasklist" -H "accept: application/json"`

Removing Task.
<br />`curl -X DELETE "http://localhost:5000/task/Complete%20Workout" -H "accept: application/json"`
