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
  
## Quick Start
First we need to setup our necessary stuff (Python installation and MongoDB), after that navigate to the src folder in CMD and run using 'Python TaskListAPI'. Now you can access the API in browser at 'http://localhost:5000/'

You can use curl command to interact with API. For example:
 `curl "http://localhost:5000/tasklist"`
