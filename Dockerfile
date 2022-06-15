FROM continuumio/miniconda3

WORKDIR /opt/notebooks

# Create the environment:
#clona o repositorio para dentro do container docker
RUN git clone https://github.com/Laianna/projeto-sidi-er .


# RUN conda env create -n tf_gpu 
# RUN activate tf_gpu
# RUN conda install pip
# RUN conda update -n tf_gpu -v --file environment.yml

COPY environment.yml .
RUN conda env create -v --file environment.yml
RUN activate tf_gpu

# RUN conda create --name tf_gpu
# RUN conda init bash

# RUN conda activate tf_gpu
RUN apt update -y 
RUN apt upgrade -y 
RUN apt install unzip -y
RUN apt install gcc -y 
# RUN apt install nvidia-cuda-toolkit

# RUN activate base
RUN conda install cudnn==8.2.1 -y
# RUN conda install cudatoolkit -y
# RUN conda run /opt/conda/bin/python -m pip install -U numpy
# RUN conda run /opt/conda/bin/python -m pip install tensorflow==2.6.0
# RUN conda run /opt/conda/bin/python -m pip install tensorflow-gpu==2.6.0
# RUN conda run /opt/conda/bin/python -m pip install tensorflow-addons
# RUN conda run /opt/conda/bin/python -m pip install pip=21.2.4
# RUN conda run /opt/conda/bin/python -m pip install keras=2.6.0=pyhd3eb1b0_0
# RUN conda run /opt/conda/bin/python -m pip install keras-preprocessing=1.1.2=pyhd3eb1b0_0
# RUN conda run /opt/conda/bin/python -m pip install nltk=3.5=py_0
# RUN conda run /opt/conda/bin/python -m pip install tqdm=4.50.2=py_0
# RUN conda run /opt/conda/bin/python -m pip install transformers=4.16.2=pyhd8ed1ab_0
# RUN conda run /opt/conda/bin/python -m pip install pip:
# RUN conda run /opt/conda/bin/python -m pip install numpy==1.21.5
# RUN conda run /opt/conda/bin/python -m pip install pandas==1.4.1
# RUN conda run /opt/conda/bin/python -m pip install ipykernel==6.4.1
# RUN conda run /opt/conda/bin/python -m pip install tokenizers==0.10.3
# RUN conda run /opt/conda/bin/python -m pip install ipython==7.31.1
# # RUN conda run /opt/conda/bin/python -m pip install cudatoolkit==11.3.1
# RUN conda run /opt/conda/bin/python -m pip install h5py==3.6.0
# # RUN conda run /opt/conda/bin/python -m pip install pytorch==1.10.2
# RUN conda run /opt/conda/bin/python -m pip install scikit-learn==1.0.2
# # RUN conda run /opt/conda/bin/python -m pip install python==3.9.7
# RUN conda run /opt/conda/bin/python -m pip install ipywidgets==7.7.0
# RUN conda run /opt/conda/bin/python -m pip install keras-tuner

ENTRYPOINT ["python"]
# conda run /opt/conda/bin/python /opt/notebooks/experimento_outros_metodos.py
# import os
# os.environ["CUDA_VISIBLE_DEVICES"] = "0"