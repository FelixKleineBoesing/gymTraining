# A Dockerfile that sets up a full Gym install with test dependencies
FROM jupyter/base-notebook:latest

apt install -y python3-dev zlib1g-dev libjpeg-dev cmake swig python-pyglet python3-opengl libboost-all-dev libsdl2-dev \
    libosmesa6-dev patchelf ffmpeg xvfb


