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
* Commit
  * docker commit -p CONTAINER-ID New-Docker-Image-Name
