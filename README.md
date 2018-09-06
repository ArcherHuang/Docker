# Docker-Flask-Sample
> 此範例說明如何建立 Docker 版的 Python Flask CRUD

## Docker Image Environment
* Ubuntu 16.04
* Python 2.7
* Flask 0.12.2

## Build Docker Image Host Environment
* macOS Sierra 10.12.5

## Test Host Environment
* macOS Sierra 10.12.5 - Terminal
* Windows 10 - PowerShell

## Docker Command

> 在 Windows 環境執行指令時，請移除最前面的 sudo (粗體字)

* 1&nbsp;&nbsp;&nbsp;&nbsp;從 Docker Hub 取得 mmosconii 的 flask-sample Image 
  * **sudo** docker pull mmosconii/flask-sample
* 2&nbsp;&nbsp;&nbsp;&nbsp;執行 flask-sample Image，命名為 flask-sample-dev，<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;埠號對應主機的 8888 通訊埠轉發到 Container 的 8888 通訊埠
  * **sudo** docker run -d --name=flask-sample-dev -p 8888:8888 mmosconii/flask-sample
* 3&nbsp;&nbsp;&nbsp;&nbsp;查看名字為 flask-sample-dev 的 Container Log
  * **sudo** docker logs -f flask-sample-dev
* 4&nbsp;&nbsp;&nbsp;&nbsp;進入正在執行的 Docker Container
  * **sudo** docker exec -it flask-sample-dev bash
* 5&nbsp;&nbsp;&nbsp;&nbsp;刪除 Image
  * **sudo** docker rmi -f mmosconii/flask-sample
* 6&nbsp;&nbsp;&nbsp;&nbsp;刪除 Container
  * **sudo** docker rm -f flask-sample-dev
* 7&nbsp;&nbsp;&nbsp;&nbsp;停止 Container
  * **sudo** docker stop flask-sample-dev
* 8&nbsp;&nbsp;&nbsp;&nbsp;重啟 Container
  * **sudo** docker restart flask-sample-dev
* 9&nbsp;&nbsp;&nbsp;&nbsp;查看本地端的 Image
  * **sudo** docker images
* 10&nbsp;&nbsp;查看目前 Container 狀態
  * **sudo** docker ps -a
* 11&nbsp;&nbsp;確認 Docker 版本
  * docker --version
* 12&nbsp;&nbsp;透過 Dockerfile 建立 Docker Image
  * **sudo** docker build --no-cache -t mmosconii/flask-sample .

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
