# 建立 Docker 版的 Python Flask

## 學習目標
* Docker 運作流程
* Docker 指令
* Dockerfile 撰寫
* Python Flask 的 CRUD 撰寫
* Postman 使用

## Contents
- [Docker Flask Sample 說明](#docker-flask-sample)
- [Docker 運作流程](#docker-運作流程)
- [Docker Image 環境](#docker-image-environment)
- [建立 Docker Image 的開發環境](#build-docker-image-host-environment)
- [測試 Docker Image 的環境](#test-image-host-environment)
- [Docker Engine 安裝](#docker-engine)
- [Dockerfile 說明](#dockerfile)
- [Docker 指令](#docker-command)
- [API 說明](#api)
- [Docker Hub](#docker-hub)

## Docker Flask Sample
[Top](#contents)

> 此範例說明如何建立 Docker 版的 Python Flask CRUD

```
Docker 是一個開放原始碼軟體專案，讓應用程式布署在軟體容器下的工作可以自動化進行，藉此在作業系統上，
提供一個額外的軟體抽象層，以及作業系統層虛擬化的自動管理機制。
```

``` 
Flask 是一個 Python 的輕量級 Web 應用框架 
```

| CRUD |  全名  | HTTP 傳輸動作 | 說明 |
|:----:|:------:|:-------------:|:----:|
|   C  | Create |      POST     | 新增 |
|   R  |  Read  |      GET      | 讀取 |
|   U  | Update |      PUT      | 更新 |
|   D  | Delete |     DELETE    | 刪除 |

## Docker 運作流程
[Top](#contents)

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_06___11_24_43-1536204323704.png)

* Docker Image
  * 是一個唯讀的模板且可透過它來建立 Docker Container
* Dockerfile
  * 透過 Dockerfile 打包自己的 Docker Image
* Docker Container
  * 透過 Docker Image 產生隔離的執行環境
* Docker Registry
  * 存放 Docker Image 的地方
  * 種類
    * 公開倉庫（ Public Registry )
      * e.g., 免費 [Docker Hub](https://hub.docker.com/) 
    * 私有倉庫（ Private Registry ）
      * e.g., ① 自建、<br/>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;②[【 付費 】](https://azure.microsoft.com/zh-tw/pricing/details/container-registry/) [Azure Container Registry](https://azure.microsoft.com/en-au/services/container-registry/)、<br/>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;③[【 付費 】](https://cloud.google.com/container-registry/pricing?hl=zh-tw) [GCP Container Registry](https://cloud.google.com/container-registry/?hl=zh-tw)、<br/>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;④[【 付費 】](https://aws.amazon.com/tw/ecr/pricing/) [Amazon Elastic Container Registry](https://aws.amazon.com/tw/ecr/)

## Docker Image Environment
[Top](#contents)

* Ubuntu 16.04
* Python 2.7
* Flask 0.12.2

## Build Docker Image Host Environment
[Top](#contents)

* macOS Sierra 10.12.5

## Test Image Host Environment
[Top](#contents)

* macOS Sierra 10.12.5 - 終端機（ Terminal ）
* Windows 10 - PowerShell

## Docker Engine
[Top](#contents)

* [Docker for Windows](https://docs.docker.com/docker-for-windows/install/) 
* [Docker for Mac](https://docs.docker.com/docker-for-mac/install/)

## Dockerfile
[Top](#contents)

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_06___4_27_28-1536222462381.png)

```
第  2 行  使用 ubuntu 16.04 版本
第  3 行  此 Dockerfile 維護者資訊
第  5 行  透過 apt-get 更新
第  6 行  透過 apt-get 安裝 python-pip、python-dev、build-essential 套件
第  7 行  複製指定檔案到 Container 中，亦即是複製 Dockerfile、flask-docker.py、requirements.txt 檔案到 /flask-app 目錄中
第  8 行  切換工作目錄到 /flask-app 目錄中
第  9 行  透過 pip 安裝 requirements.txt 檔案中的套件，亦即是安裝 Flask 的 0.12.2 版本
第 10 行  Expose Container 中的埠號
第 11 行  使用 python 指令
第 12 行  執行 flask-docker.py 程式
```

## Docker Command
[Top](#contents)

> 在 Windows 環境執行指令時，請移除最前面的 sudo ( 粗體字的部份 )

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
* 13&nbsp;&nbsp;登入到 Docker Hub
  * **sudo** docker login
* 14&nbsp;&nbsp;上傳 Image 到 Docker Hub
  * **sudo** docker push mmosconii/flask-sample
* 15&nbsp;&nbsp;查看 log
  * **sudo** docker logs flask-sample-dev
* 16&nbsp;&nbsp;查看 log
  * **sudo** docker restart flask-sample-dev  
* 17&nbsp;&nbsp;刪除所有 container
  * docker rm $(docker ps -a -q)
* 18&nbsp;&nbsp;刪除所有 images
  * docker rmi $(docker images -q)
* 19&nbsp;&nbsp;Install Docker Compose
  * sudo curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
  * sudo chmod +x /usr/local/bin/docker-compose
  * docker-compose --version
* 20&nbsp;&nbsp;透過 Docker Compose 啟動 Docker
  * docker-compose up -d

## API
[Top](#contents)

* GET http://IP:8888/
  * Code
    ![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_06___4_46_53-1536223643532.png)
    
  * Response
    * Flask Dockerized
    
    ![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_06___1_49_12-1536213025205.png)
    
* POST http://IP:8888/api/v1.0/print
  * Code
    ![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_06___4_48_22-1536223722244.png)
  
  * Request
    * form-data
    * Key: name
    * Value: Your Name
  * Response
    * {"comment": "[ POST Method ] Hello Your Name", "status": 200}
    
    ![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_06___1_51_52-1536213135289.png)
    
* GET http://IP:8888/api/v1.0/print
  * Code
    ![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_06___4_49_36-1536223792965.png)
  
  * Response
    * {"comment": "[ Get Method ] Hello World", "status": 200}
    
    ![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_06___1_53_01-1536213198147.png)
    
* PUT http://IP:8888/api/v1.0/print
  * Code
    ![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_06___4_50_29-1536223846490.png)
  
  * Response
    * {"comment": "[ PUT Method ] Hello World", "status": 200}
    
    ![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_06___1_54_09-1536213275178.png)
    
* DELETE http://IP:8888/api/v1.0/print
  * Code
    ![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_06___4_51_01-1536223876581.png)
  
  * Response
    * {"comment": "[ DELETE Method ] Hello World", "status": 200}
    
    ![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_06___1_54_20-1536213310932.png)

## Docker Hub
[Top](#contents)

* https://hub.docker.com/r/mmosconii/flask-sample/

--------------------------------
Next: [02 EC2 Docker Registry](https://github.com/ArcherHuang/Docker/tree/master/02%20%20EC2-Docker-Registry) <br>
Top: [建立 Docker 版的 Python Flask 目錄](#contents)<br>
Back: [Docker 首頁](https://github.com/ArcherHuang/Docker#contents)
