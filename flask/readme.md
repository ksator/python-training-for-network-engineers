python script app.py:
```
# you need to "sudo pip install flask"

# import flask 
from flask import Flask, jsonify, abort, make_response, request

# instakciate the class Flask. app is an istance of the class Flask so this is an object. app is a variable. 
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
```
$ python app.py 
```
```
$ curl -i http://localhost:5000/todo/api/v1.0/tasks
$ curl -i http://localhost:5000/todo/api/v1.0/tasks/1
$ curl -i http://localhost:5000/todo/api/v1.0/tasks/2
$ curl -i http://localhost:5000/todo/api/v1.0/tasks/3
$ curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://localhost:5000/todo/api/v1.0/tasks
$ curl -i http://localhost:5000/todo/api/v1.0/tasks
$ curl -i http://localhost:5000/todo/api/v1.0/tasks/3
```
