## Contents
* Build Docker Image
  * docker build --no-cache -t mmosconii/ubuntu1604-python3-jupyter-tensorflow .
* 執行 mmosconii/ubuntu1604-python3-jupyter-tensorflow Image 
  * docker run -it --name=ubuntu1604-python3-jupyter-tensorflow-dev -p :8888 mmosconii/ubuntu1604-python3-jupyter-tensorflow
* 進到 Container 中
  * docker exec -it ubuntu1604-python3-jupyter-tensorflow-dev bash
* Check Port
  * docker ps -a
* Jupyter
  * http://IP:PORT/?token=TOKEN
  * 執行結果
  
  ![](https://oranwind.s3.amazonaws.com/2018/Dec/_____2018_12_07___11_40_52-1544154143150.png)
  ![](https://oranwind.s3.amazonaws.com/2018/Dec/_____2018_12_07___11_41_01-1544154168376.png)
  ![](https://oranwind.s3.amazonaws.com/2018/Dec/_____2018_12_07___11_41_17-1544154188593.png)
  
* Commit
  * docker commit -p CONTAINER-ID New-Docker-Image-Name
