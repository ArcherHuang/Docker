## Contents
- [AWS EC2 設定](#aws-ec2-設定)
- [遠端登入到 AWS EC2](#遠端登入到-aws-ec2)
- [安裝 Docker Engine](#安裝-docker-engine)
- [下載並啟動 Docker Registry](#下載並啟動-docker-registry)
- [設定 insecure-registries](#設定-insecure-registries)
- [Push Docker Image 到 Docker Registry](#push-docker-image-到-docker-registry)
- [透過 Restful API 查詢 Docker Registry 資訊](#透過-restful-api-查詢-docker-registry-資訊)

## AWS EC2 設定
[Top](#contents)

* 登入到 AWS EC2 

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___2_42_25-1536648162101.png)

* 點選 【 Services 】 中的 【 EC2 】

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___2_55_33-1536648949561.png)


## 遠端登入到 AWS EC2
[Top](#contents)

## 安裝 Docker Engine
[Top](#contents)

```
sudo apt-get update
sudo apt-get install -y docker.io
```



## 下載並啟動 Docker Registry
[Top](#contents)

```
sudo docker run -d -p 5000:5000 -v /docker/registry:/var/lib/registry registry
```



## 設定 insecure-registries
[Top](#contents)

- 的

  ```
  Docker-Registry-IP:5000
  ```


- 重新啟動 Docker 

  ```
  
  ```


## Push Docker Image 到 Docker Registry
[Top](#contents)

```
sudo docker tag mmosconii/influxdb Docker-Registry-IP:5000/mmosconii/influxdb

sudo docker push Docker-Registry-IP:5000/mmosconii/influxdb
```



## 透過 Restful API 查詢 Docker Registry 資訊
[Top](#contents)

```
curl -X GET http://Docker-Registry-IP:5000/v2/_catalog
curl -X GET http://Docker-Registry-IP:5000/v2/mmosconii/influxdb/tags/list
curl -X GET http://Docker-Registry-IP:5000/v2/mmosconii/influxdb/manifests/latest
```


--------------------------------
Next: []() <br>
Top: [EC2 Docker Registry 目錄](#contents)<br>
Back: [首頁](https://github.com/ArcherHuang/Docker#contents)
