# Docker-Flask-Sample

## Docker Command

* 1&nbsp;&nbsp;&nbsp;&nbsp;從 Docker Hub 取得 flask-sample Image
  * sudo docker pull mmosconii/flask-sample
* 2&nbsp;&nbsp;&nbsp;&nbsp;執行 flask-sample Image
  * sudo docker run -d --name=flask-sample-dev -p 8888:8888 mmosconii/flask-sample
* 3&nbsp;&nbsp;&nbsp;&nbsp;查看 Container Log
  * sudo docker logs -f flask-sample-dev
* 4&nbsp;&nbsp;&nbsp;&nbsp;進入正在執行的 Docker Container
  * sudo docker exec -it flask-sample-dev bash
* 5&nbsp;&nbsp;&nbsp;&nbsp;刪除 Image
  * sudo docker rmi -f mmosconii/flask-sample
* 6&nbsp;&nbsp;&nbsp;&nbsp;刪除 Container
  * sudo docker rm -f flask-sample-dev
* 7&nbsp;&nbsp;&nbsp;&nbsp;停止 Container
  * sudo docker stop flask-sample-dev
* 8&nbsp;&nbsp;&nbsp;&nbsp;重啟 Container
  * sudo docker restart flask-sample-dev
* 9&nbsp;&nbsp;&nbsp;&nbsp;查看本地端的 Image
  * sudo docker images
* 10&nbsp;&nbsp;&nbsp;查看目前 Container 狀態
  * sudo docker ps -a

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

## GitHub
* https://github.com/ArcherHuang/Docker-Flask-Sample

## Docker Hub
* https://hub.docker.com/r/mmosconii/flask-sample/
