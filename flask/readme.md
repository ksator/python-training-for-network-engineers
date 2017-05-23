## Designing a restfull api with flask

inspired by this tuto https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

### requirements
you need to ```sudo pip install flask```

### python script content:
```
more app.py
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

# rest call to delete 
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})

# rest call to update 
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})


# use the run method of the class Flask
app.run(debug=True)

```
### Excecute the python script: 

```
$ export FLASK_APP=app.py
$ echo $FLASK_APP
app.py
$ flask run
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 761-615-843
```

```
$ python app.py 
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 761-615-843
```
### make rest calls: 
The below rest calls are with curl.  
if you prefer to make rest calls using a python rest client, please refer to these examples about the requests module https://github.com/ksator/python-training-for-network-engineers/tree/master/rest_basics 

##### Retrieve list of tasks:

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
##### Retrieve a task:
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
##### Note the 404 error is in json instead of html: 
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
##### create a new task (http method is post, http response code is 201):
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
###### Retrieve list of tasks:
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
###### Retrieve a task:
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

##### Delete an existing task: 
```
$ curl -i -X DELETE http://localhost:5000/todo/api/v1.0/tasks/1
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 21
Server: Werkzeug/0.12.2 Python/2.7.6
Date: Mon, 22 May 2017 11:51:01 GMT

{
  "result": true
}
```
```
$ curl -i http://localhost:5000/todo/api/v1.0/tasks
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 173
Server: Werkzeug/0.12.2 Python/2.7.6
Date: Mon, 22 May 2017 11:51:07 GMT

{
  "tasks": [
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
HTTP/1.0 404 NOT FOUND
Content-Type: application/json
Content-Length: 27
Server: Werkzeug/0.12.2 Python/2.7.6
Date: Mon, 22 May 2017 11:51:12 GMT

{
  "error": "Not found"
}
```
```
$ curl -i -X DELETE http://localhost:5000/todo/api/v1.0/tasks/1
HTTP/1.0 404 NOT FOUND
Content-Type: application/json
Content-Length: 27
Server: Werkzeug/0.12.2 Python/2.7.6
Date: Mon, 22 May 2017 11:51:25 GMT

{
  "error": "Not found"
}

```

#### Update existing tasks
```
$ curl -i http://localhost:5000/todo/api/v1.0/tasks
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 173
Server: Werkzeug/0.12.2 Python/2.7.6
Date: Mon, 22 May 2017 12:11:29 GMT

{
  "tasks": [
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
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"done":true}' http://localhost:5000/todo/api/v1.0/tasks/2
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 151
Server: Werkzeug/0.12.2 Python/2.7.6
Date: Mon, 22 May 2017 12:11:43 GMT

{
  "task": {
    "description": "Need to find a good Python tutorial on the web", 
    "done": true, 
    "id": 2, 
    "title": "Learn Python"
  }
}
```
```
$ curl -i http://localhost:5000/todo/api/v1.0/tasks/2
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 151
Server: Werkzeug/0.12.2 Python/2.7.6
Date: Mon, 22 May 2017 12:11:55 GMT

{
  "task": {
    "description": "Need to find a good Python tutorial on the web", 
    "done": true, 
    "id": 2, 
    "title": "Learn Python"
  }
}
```
```
$ curl -i http://localhost:5000/todo/api/v1.0/tasks
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 172
Server: Werkzeug/0.12.2 Python/2.7.6
Date: Mon, 22 May 2017 12:12:03 GMT

{
  "tasks": [
    {
      "description": "Need to find a good Python tutorial on the web", 
      "done": true, 
      "id": 2, 
      "title": "Learn Python"
    }
  ]
}

```

### Python script debug output
```
$ python app2.py 
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 761-615-843
127.0.0.1 - - [22/May/2017 13:20:58] "GET /todo/api/v1.0/tasks HTTP/1.1" 200 -
127.0.0.1 - - [22/May/2017 13:21:08] "GET /todo/api/v1.0/tasks/1 HTTP/1.1" 200 -
127.0.0.1 - - [22/May/2017 13:21:10] "GET /todo/api/v1.0/tasks/2 HTTP/1.1" 200 -
127.0.0.1 - - [22/May/2017 13:21:12] "GET /todo/api/v1.0/tasks/3 HTTP/1.1" 404 -
127.0.0.1 - - [22/May/2017 13:21:24] "POST /todo/api/v1.0/tasks HTTP/1.1" 201 -
127.0.0.1 - - [22/May/2017 13:21:27] "GET /todo/api/v1.0/tasks HTTP/1.1" 200 -
127.0.0.1 - - [22/May/2017 13:21:30] "GET /todo/api/v1.0/tasks/3 HTTP/1.1" 200 -
...
```
### Execute shell commands with Python
```
>>> import subprocess
>>> 
>>> subprocess.check_output(["echo", "Hello World!"])
'Hello World!\n'
>>> 
>>> p = subprocess.Popen("echo Hello World!", shell=True, stdout = subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
>>> out,err = p.communicate()
>>> out
'Hello World!\n'
>>> err
''
>>> 
>>> shell_cmd1 = "echo Hello World!"
>>> shell_cmd1_p = subprocess.Popen(shell_cmd1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
>>> shell_cmd1_p.communicate()[0]
'Hello World!\n'
>>> 
>>> 
```

### How to Execute ansible playboolks or python scripts making rest calls to server API
we know from the previous section how to execute shell commands from python. so we can use this to execute python scripts or ansible playbooks.  
we also need to change the app.py file in order to execute shell commands in the functions. as example: 
```
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    shell_cmd1 = "ls -l"
    shell_cmd1_p = subprocess.Popen(shell_cmd1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out, err = shell_cmd1_p.communicate()
    return out
```


