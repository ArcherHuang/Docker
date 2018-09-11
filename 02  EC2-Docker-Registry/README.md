## Contents
- [Docker Flask Sample](https://github.com/ArcherHuang/Docker/tree/master/Python-Flask#contents)

## AWS EC2 設定





## 安裝 Docker Engine

```
sudo apt-get update
sudo apt-get install -y docker.io
```



## 下載並啟動 Docker Registry

```
sudo docker run -d -p 5000:5000 -v /docker/registry:/var/lib/registry registry
```



## 設定 insecure-registries

- 的

- ```
  Docker-Registry-IP:5000
  ```


- 重新啟動 Docker 

  ```
  
  ```


## Push Docker Image 到 Docker Registry

```
sudo docker tag mmosconii/influxdb Docker-Registry-IP:5000/mmosconii/influxdb

sudo docker push Docker-Registry-IP:5000/mmosconii/influxdb
```



## 透過 Restful API 來查詢 Docker Registry 資訊

```
curl -X GET http://Docker-Registry-IP:5000/v2/_catalog
curl -X GET http://Docker-Registry-IP:5000/v2/mmosconii/influxdb/tags/list
curl -X GET http://Docker-Registry-IP:5000/v2/mmosconii/influxdb/manifests/latest
```


--------------------------------
Next: []() <br>
Top: [EC2 Docker Registry 目錄](#contents)<br>
Back: [首頁](https://github.com/ArcherHuang/Docker#contents)
