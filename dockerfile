# A Dockerfile that sets up a full Gym install with test dependencies
FROM jupyter/base-notebook:latest

USER root

RUN \
    apt -y update && \
    apt install -y keyboard-configuration && \

    apt install -y \ 
        python-setuptools \
        python-pip \
        python3-dev \
        python-pyglet \
        python3-opengl \
        libjpeg-dev \
        libboost-all-dev \
        libsdl2-dev \
        libosmesa6-dev \
        patchelf \
        ffmpeg \
        xvfb \
        wget \
        unzip \
        gdebi \
        && \

    apt clean && \
    rm -rf /var/lib/apt/lists/* && \

# Download mujoco
    mkdir /home/jovyan/.mujoco && \
    cd /home/jovyan/.mujoco  && \
    wget https://www.roboti.us/download/mjpro150_linux.zip  && \
    unzip mjpro150_linux.zip && \
    wget https://www.roboti.us/download/mujoco200_linux.zip && \
    unzip mujoco200_linux.zip && \
    mv mujoco200_linux mujoco200

ARG MUJOCO_KEY
ENV MUJOCO_KEY=$MUJOCO_KEY
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/jovyan/.mujoco/mjpro150/bin
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/jovyan/.mujoco/mujoco200/bin
RUN echo $MUJOCO_KEY | base64 --decode > /home/jovyan/.mujoco/mjkey.txt


COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

