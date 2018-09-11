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

* 1  登入到 AWS EC2 

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___2_42_25-1536648162101.png)

---

* 2  點選 【 Services 】 中的 【 EC2 】

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___2_55_33-1536648949561.png)

---

* 3  點選 【 Launch Instance 】

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___3_01_56-1536649334774.png)

---

* 4  點選 【 Ubuntu Server 16.04 LTS 】

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___3_08_27-1536649722418.png)

---

* 5  點選 【 t2.micro Free tier eligible 】再點選上方的 【 6. Configure Security Group 】

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___3_10_17-1536649840659.png)

---

* 6  點選 【 Add Rule 】

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___3_15_07-1536650132302.png)

```
新增下方資訊後按 【 Review and Launch 】

Port Range: 5000
Source: 0.0.0.0/0
```

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___3_17_24-1536650262691.png)

---

* 7  點選 【 Launch 】

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___3_20_14-1536650429996.png)

---

* 8  點選 【 Create a new key pair 】

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___3_29_25-1536650984780.png)


```
① 輸入 【 Key pair name 】
② 點選 【 Download Key Pair 】
```

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___3_33_56-1536651257717.png)

```
Key Pair 下載結果
```

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___3_37_30-1536651521517.png)

```
點選 【 Launch Instances 】
```

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___3_40_32-1536651648414.png)

---

* 9  點選 【 View Instances 】

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___3_42_10-1536651768389.png)

---

* 10  AWS EC2 建立完的結果

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___3_44_09-1536651912817.png)


## 遠端登入到 AWS EC2
[Top](#contents)

* macOS


* Windows


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
