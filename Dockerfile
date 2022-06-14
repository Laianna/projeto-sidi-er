FROM continuumio/miniconda3

WORKDIR /opt/notebooks

# Create the environment:
#clona o repositorio para dentro do container docker
RUN git clone https://github.com/Laianna/projeto-sidi-er .


# COPY environment.yml .
# RUN conda env create -f environment.yml
# RUN conda create --name tf_gpu
# RUN conda init bash

# RUN conda activate tf_gpu
RUN apt update -y 
RUN apt upgrade -y 
RUN apt install unzip 

RUN conda install -n base ipykernel --update-deps --force-reinstall



RUN conda run /opt/conda/bin/python -m pip install transformers
RUN conda run /opt/conda/bin/python -m pip install -U scikit-learn
RUN conda run /opt/conda/bin/python -m pip install pandas
# RUN conda run /opt/conda/bin/python -m pip install tensorflow
RUN conda run /opt/conda/bin/python -m pip install tensorflow-gpu
RUN conda run /opt/conda/bin/python -m pip install tensorflow-addons
RUN conda run /opt/conda/bin/python -m pip install torch torchvision
RUN conda run /opt/conda/bin/python -m pip install numpy
# COPY environment.yml .

# instala pacotes do python e para o sistema

# RUN conda run /opt/conda/bin/python -m pip install tensorflow==2.6.0 -V

ENTRYPOINT ["python"]
# conda run /opt/conda/bin/python /opt/notebooks/experimento_outros_metodos.py