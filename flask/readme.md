python script app.py content:
```
# you need to "sudo pip install flask"

# import flask 
from flask import Flask, jsonify, abort, make_response, request

# instanciate the class Flask. app is an istance of the class Flask so this is an object. app is a variable. 
app = Flask(__name__)

# tasks is a variable, of type list. each item is a dictionnary.
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

# this is what to do wit an http call using get method to /todo/api/v1.0/tasks
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# this is what to do wit an http call using get method to /todo/api/v1.0/tasks/xxx
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

# handle http 404 differently
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# this is what to do wit an http call using post method to /todo/api/v1.0/tasks
@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

# use the run method of the class Flask
app.run(debug=True)
```
Excecute the python script: 
```
$ python app.py 
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 761-615-843
```
make rest calls: 
```
$ curl -i http://localhost:5000/todo/api/v1.0/tasks
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 317
Server: Werkzeug/0.12.2 Python/2.7.6
Date: Mon, 22 May 2017 11:20:58 GMT

{
  "tasks": [
    {
      "description": "Milk, Cheese, Pizza, Fruit, Tylenol", 
      "done": false, 
      "id": 1, 
      "title": "Buy groceries"
    }, 
    {
      "description": "Need to find a good Python tutorial on the web", 
      "done": false, 
      "id": 2, 
      "title": "Learn Python"
    }
  ]
}
```
```
$ curl -i http://localhost:5000/todo/api/v1.0/tasks/1
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 142
Server: Werkzeug/0.12.2 Python/2.7.6
Date: Mon, 22 May 2017 11:21:08 GMT

{
  "task": {
    "description": "Milk, Cheese, Pizza, Fruit, Tylenol", 
    "done": false, 
    "id": 1, 
    "title": "Buy groceries"
  }
}
```
```
$ curl -i http://localhost:5000/todo/api/v1.0/tasks/2
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 152
Server: Werkzeug/0.12.2 Python/2.7.6
Date: Mon, 22 May 2017 11:21:10 GMT

{
  "task": {
    "description": "Need to find a good Python tutorial on the web", 
    "done": false, 
    "id": 2, 
    "title": "Learn Python"
  }
}
```
```
$ curl -i http://localhost:5000/todo/api/v1.0/tasks/3
HTTP/1.0 404 NOT FOUND
Content-Type: application/json
Content-Length: 27
Server: Werkzeug/0.12.2 Python/2.7.6
Date: Mon, 22 May 2017 11:21:12 GMT

{
  "error": "Not found"
}
```
```
$ curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://localhost:5000/todo/api/v1.0/tasks
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 105
Server: Werkzeug/0.12.2 Python/2.7.6
Date: Mon, 22 May 2017 11:21:24 GMT

{
  "task": {
    "description": "", 
    "done": false, 
    "id": 3, 
    "title": "Read a book"
  }
}
```
```
$ curl -i http://localhost:5000/todo/api/v1.0/tasks
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 424
Server: Werkzeug/0.12.2 Python/2.7.6
Date: Mon, 22 May 2017 11:21:27 GMT

{
  "tasks": [
    {
      "description": "Milk, Cheese, Pizza, Fruit, Tylenol", 
      "done": false, 
      "id": 1, 
      "title": "Buy groceries"
    }, 
    {
      "description": "Need to find a good Python tutorial on the web", 
      "done": false, 
      "id": 2, 
      "title": "Learn Python"
    }, 
    {
      "description": "", 
      "done": false, 
      "id": 3, 
      "title": "Read a book"
    }
  ]
}
```
```
$ curl -i http://localhost:5000/todo/api/v1.0/tasks/3
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 105
Server: Werkzeug/0.12.2 Python/2.7.6
Date: Mon, 22 May 2017 11:21:30 GMT

{
  "task": {
    "description": "", 
    "done": false, 
    "id": 3, 
    "title": "Read a book"
  }
}
```
