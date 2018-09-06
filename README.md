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
  * form-data
  * Key: name
  * Value: Your Name
* GET http://IP:8888/api/v1.0/print
* PUT http://IP:8888/api/v1.0/print
* DELETE http://IP:8888/api/v1.0/print
