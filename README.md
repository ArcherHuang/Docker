# Docker-Flask-Sample

## Docker Command

* sudo docker pull mmosconii/flask-sample
* sudo docker run -d --name=flask-sample-dev -p 8888:8888 mmosconii/flask-sample
* sudo docker logs -f flask-sample-dev

## API

* GET http://IP:8888/
  * Response
    * Flask Dockerized
* POST http://IP:8888/api/v1.0/print
  * Request
    * form-data
    * Key: name
    * Value: Your Name
  * Response
    * {"comment": "[ POST Method ] Hello Your Name", "status": 200}
* GET http://IP:8888/api/v1.0/print
  * Response
    * {"comment": "[ Get Method ] Hello World", "status": 200}
* PUT http://IP:8888/api/v1.0/print
  * Response
    * {"comment": "[ PUT Method ] Hello World", "status": 200}
* DELETE http://IP:8888/api/v1.0/print
  * Response
    * {"comment": "[ DELETE Method ] Hello World", "status": 200}
