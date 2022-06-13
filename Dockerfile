FROM continuumio/miniconda3

WORKDIR /opt/notebooks

# Create the environment:
#clona o repositorio para dentro do container docker
RUN git clone https://github.com/Laianna/projeto-sidi-er .

RUN conda install -n base ipykernel --update-deps --force-reinstall

COPY environment.yml .

# instala pacotes do python e para o sistema
RUN apt update -y 
RUN apt upgrade -y 
#RUN conda env create -f environment.yml

RUN conda run /opt/conda/bin/python -m pip install tensorflow==2.6.0 -V

ENTRYPOINT ["python"]