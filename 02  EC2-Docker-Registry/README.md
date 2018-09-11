# 在 AWS EC2 上建立 Docker Registry

## 學習目標
* AWS EC2 使用
* 遠端登入到 AWS EC2
* 建立 Docker Registry
* 查詢 Docker Registry 資訊

## Contents
- [示意圖](#示意圖)
- [AWS EC2 設定](#aws-ec2-設定)
- [遠端登入到 AWS EC2](#遠端登入到-aws-ec2)
- [安裝 Docker Engine](#安裝-docker-engine)
- [下載並啟動 Docker Registry](#下載並啟動-docker-registry)
- [設定 insecure-registries](#設定-insecure-registries)
- [Push Docker Image 到 Docker Registry](#push-docker-image-到-docker-registry)
- [透過 Restful API 查詢 Docker Registry 資訊](#透過-restful-api-查詢-docker-registry-資訊)


## 示意圖

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___7_31_28-1536665511062.png)

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

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___4_17_12-1536653853559.png)

```
Key Pair 下載結果
```

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___3_37_30-1536651521517.png)

```
點選 【 Launch Instances 】
```

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___4_18_18-1536653913102.png)

---

* 9  點選 【 View Instances 】

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___3_42_10-1536651768389.png)

---

* 10  AWS EC2 建立完的結果

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___3_44_09-1536651912817.png)


## 遠端登入到 AWS EC2
[Top](#contents)

* macOS

#### Step 1. 開啟終端機

```
❖ 1.1  點選【 前往 】 ➙ 【 工具程式 】 ➙ 【 終端機 】
```

![](https://oranwind.s3.amazonaws.com/2018/May/_____2018_05_11___4_06_17-1526029543552.png)

![](https://oranwind.s3.amazonaws.com/2018/May/_____2018_05_11___4_07_36-1526029608416.png)

---

#### Step 2. 切換路徑到 AWS EC2 憑證所在位置

```
 2.1  指令為 cd 憑證所在目錄
```

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___3_57_21-1536652679087.png)

```
 2.2  確認憑證是否存在
       指令為 ls -al
```

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___3_59_43-1536652801185.png)

```
 2.3  設定憑證權限
       指令為 chmod 400 憑證名稱
```

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___4_01_13-1536652888869.png)

---

#### Step 3. 取得 AWS EC2 登入資訊

```
3.1  點選所啟用的 Instance 再點選 【 Connect 】
```

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___3_44_09-1536651912817.png)

---

```
3.2  複製紅色框框中的資訊到終端機中
```

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___4_23_21-1536654484639.png)

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___4_24_15-1536654285317.png)


---

```
3.3   登入成功畫面
```

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___4_26_01-1536654379808.png)

---

* Windows

#### Step 1. 下載 PuTTY 並安裝

下載網址 https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html

![](https://oranwind.s3.amazonaws.com/2018/Apr/putty_download-1524464796048.png)

---

#### Step 2. 將 AWS EC2 的 .pem 憑證檔轉成 .ppk

```
 2.1  開啟 PuTTYgen
       ① 點選【 開始 】 ➙ 【 所有程式 】 ➙ 【 PuTTY 】 ➙ 【 PuTTYgen 】
```

![](https://oranwind.s3.amazonaws.com/2018/Apr/0-1524464931948.png)

![](https://oranwind.s3.amazonaws.com/2018/Apr/0_1-1524465188028.png)

---

```
 2.2  載入私有金鑰
       ① 點選 【 File 】 ➙ 【 Load private key 】
```

![](https://oranwind.s3.amazonaws.com/2018/Apr/0_2-1524465327482.png)

---

```
       ② 將右下角 【 PuTTY Private Key Files(*.ppk) 】選項改成 【 All Files (*.*) 】
```

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___4_48_46-1536655741402.png)

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___4_47_36-1536655680593.png)

---

```
       ③ 點選 AWS EC2 的 .pem 憑證檔  ➙ 【 開啟 】
```

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___4_49_23-1536655777359.png)

---

```
       ④ 點選 【 確定 】
```

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___4_50_06-1536655819404.png)

---

```
       ⑤ 點選 【 Save private key 】
```

![](https://oranwind.s3.amazonaws.com/2018/Apr/0_7-1524466411984.png)

---

```
       ⑥ 點選 【 是 】
```

![](https://oranwind.s3.amazonaws.com/2018/Apr/0_8-1524466518016.png)

---

```
       ⑦ 檔案名稱取名並點選 【 存檔 】
```

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___4_52_12-1536655951582.png)

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___4_53_02-1536655996650.png)

---

#### Step 3. 登入到 AWS EC2 中

```
 3.1  開啟 PuTTY
       ① 點選【 開始 】 ➙ 【 所有程式 】 ➙ 【 PuTTY 】
```

![](https://oranwind.s3.amazonaws.com/2018/Apr/0_12-1524467056127.png)

![](https://oranwind.s3.amazonaws.com/2018/Apr/0_13-1524467189899.png)

---


```
       ② 點選【 Connection 】 ➙ 【 SSH 】 ➙ 【 Auth 】
```

![](https://oranwind.s3.amazonaws.com/2018/Apr/0_14-1524467258067.png)

---


```
       ③ 點選 【 Browse 】按鈕，匯入步驟 2.2 所產生的 .ppk 憑證檔 ➙ 【 開啟 】 
```

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___4_54_19-1536656075795.png)


---

```
       ④ 點選 【 Session 】
```

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___4_55_06-1536656118589.png)

![](https://oranwind.s3.amazonaws.com/2018/Apr/0_17-1524468482104.png)


---

```
       ⑤ 在 【 Host Name (or IP address) 】 欄位中輸入 AWS EC2 所開啟的 Instance 的帳號與 Public DNS
          5.1 請到 AWS EC2 中點選所要使用的 Instance
```

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___3_44_09-1536651912817.png)

---

```
          5.2 再點選 【 Connect 】 按鈕
```

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___4_57_15-1536656277251.png)

---

```
          5.3 複製 【 Example 】中從 ubuntu 開始到最後的文字到 PuTTY 中【 Host Name (or IP address) 】 欄位中，再點選 【 Open 】
```

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___4_58_28-1536656325753.png)

---

```
       ⑥ 點選 【 是 】
```

![](https://oranwind.s3.amazonaws.com/2018/Apr/5-1524469449243.png)

---

```
       ⑦ 登入成功畫面
```

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___4_59_24-1536656388414.png)

---

## 安裝 Docker Engine
[Top](#contents)

> 將 Docker Engine 安裝於 AWS EC2

```
於終端機 【 macOS 】或 Putty 【 Windows 】中輸入下方指令

sudo apt-get update
sudo apt-get install -y docker.io
```

---

## 下載並啟動 Docker Registry
[Top](#contents)

> 將 Docker Registry 安裝於 AWS EC2

```
於終端機 【 macOS 】或 Putty 【 Windows 】中輸入下方指令

sudo docker run -d -p 5000:5000 -v /docker/registry:/var/lib/registry registry
```

---

## 設定 insecure-registries
[Top](#contents)

> 確認 Local 端電腦已經安裝 Docker Engine 
> 在 Local 端的電腦進行 Docker 設定

* 開啟 【 Docker 】中的 【 Preferences... 】

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___5_05_37-1536656762820.png)

---

* 點選 【 Daemon 】

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___5_08_59-1536656953101.png)

---

* 在 【 insecure-registries 】中輸入下方資訊

  ```
  Docker-Registry-IP:5000
  ※ Docker-Registry-IP 位於【 AWS EC2 】服務之【 Instances 】頁面中所建立的 Instance 列表中的【 IPv4 Public IP 】欄位
  ```
  
![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___5_11_31-1536657112610.png)

---

- 點選 【 Apply & Restart 】以重新啟動 Docker 

![](https://oranwind.s3.amazonaws.com/2018/Sep/_____2018_09_11___5_13_24-1536657225264.png)

---

## Push Docker Image 到 Docker Registry
[Top](#contents)

> 將 Local 端的【 mmosconii/flask-sample 】Image 上傳到 Docker Registry <br>
> ※ 此【 mmosconii/flask-sample 】Image 為[上個章節](https://github.com/ArcherHuang/Docker/tree/master/01%20%20Python-Flask)所產生

```
於終端機【 macOS 】或 Putty【 Windows 】中輸入下方指令

sudo docker tag mmosconii/flask-sample Docker-Registry-IP:5000/mmosconii/flask-sample
sudo docker push Docker-Registry-IP:5000/mmosconii/flask-sample
```

---

## 透過 Restful API 查詢 Docker Registry 資訊
[Top](#contents)

> 在 Local 端確認遠端的 Docker Registry 是否有剛上傳的 Image

```
於終端機【 macOS 】或 Putty【 Windows 】中輸入下方指令

curl -X GET http://Docker-Registry-IP:5000/v2/_catalog
curl -X GET http://Docker-Registry-IP:5000/v2/mmosconii/flask-sample/tags/list
curl -X GET http://Docker-Registry-IP:5000/v2/mmosconii/flask-sample/manifests/latest
```


--------------------------------
Next: []() <br>
Top: [在 AWS EC2 上建立 Docker Registry 目錄](#contents)<br>
Back: [Docker 首頁](https://github.com/ArcherHuang/Docker#contents)
