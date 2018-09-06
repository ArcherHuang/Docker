from flask import Flask
from flask import json
from flask import Response
from flask import request

app = Flask(__name__)

# *****************************************************************************************
# Create GET http://IP:8888/
# *****************************************************************************************
@app.route('/')
def hello_world():
    return 'Flask Dockerized'

# *****************************************************************************************
# Create POST http://IP:8888/api/v1.0/print
# form-data
# Key: name
# Value: Your Name
# *****************************************************************************************
@app.route("/api/v1.0/print", methods=['POST'])
def postMethod():
	value = request.form['name']
	print "form_value: " + value
	return json.dumps({"status": 200, "comment": "[ POST Method ] Hello " + value})

# *****************************************************************************************
# Read GET http://IP:8888/api/v1.0/print
# *****************************************************************************************
@app.route("/api/v1.0/print", methods=['GET'])
def getMethod():
	return json.dumps({"status": 200, "comment": "[ Get Method ] Hello World"})

# *****************************************************************************************
# Update PUT http://IP:8888/api/v1.0/print
# *****************************************************************************************
@app.route("/api/v1.0/print", methods=['PUT'])
def putMethod():
	return json.dumps({"status": 200, "comment": "[ PUT Method ] Hello World"})

# *****************************************************************************************
# Delete DELETE http://IP:8888/api/v1.0/print
# *****************************************************************************************
@app.route("/api/v1.0/print", methods=['DELETE'])
def deleteMethod():
	return json.dumps({"status": 200, "comment": "[ DELETE Method ] Hello World"})

if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port = 8888
    )