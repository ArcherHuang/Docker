## Contents
* Build Docker Image
  * docker build --no-cache -t mmosconii/ubuntu1604-python3-jupyter-tensorflow .
* 執行 mmosconii/ubuntu1604-python3-jupyter-tensorflow Image 
  * docker run -it --name=ubuntu1604-python3-jupyter-tensorflow-dev -P --expose 8888 mmosconii/ubuntu1604-python3-jupyter-tensorflow
  ![](https://oranwind.s3.amazonaws.com/2018/Dec/_____2018_12_07___1_44_19-1544161507892.png)
* 進到 Container 中
  * docker exec -it ubuntu1604-python3-jupyter-tensorflow-dev bash
  ![](https://oranwind.s3.amazonaws.com/2018/Dec/_____2018_12_07___1_45_40-1544161579225.png)
* Check Port
  * docker ps -a
  ![](https://oranwind.s3.amazonaws.com/2018/Dec/_____2018_12_07___1_47_33-1544161693639.png)
* Jupyter
  * http://IP:PORT/?token=TOKEN
  * 執行結果
  ![](https://oranwind.s3.amazonaws.com/2018/Dec/_____2018_12_07___1_52_39-1544161974531.png)
  * Python3 
  ![](https://oranwind.s3.amazonaws.com/2018/Dec/_____2018_12_07___1_53_49-1544162044968.png)
  * Code <br/>
    import tensorflow as tf <br/>
    print(tf.VERSION)
  ![](https://oranwind.s3.amazonaws.com/2018/Dec/_____2018_12_07___11_41_17-1544154188593.png)

* Commit
  * docker commit -p CONTAINER-ID New-Docker-Image-Name
* Docker Hub
  * https://hub.docker.com/r/mmosconii/ubuntu1604-python3-jupyter-tensorflow/
