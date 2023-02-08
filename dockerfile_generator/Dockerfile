FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY install_cmake.sh .
RUN bash install_cmake.sh && rm install_cmake.sh

WORKDIR /home-away

COPY CMakeLists.txt . 
# need to pass the source code stuff to cmake somehow

ARG CMAKE_BINARY_DIR=~/build

COPY .bashrc .

RUN mkdir build && cd build && \
    /opt/cmake/bin/cmake ..\
     -DREPO="git" \
     -DGIT_URL="https://github.com/dafnifacility/dafni-example-models" \
     -DGIT_TAG="master" &&\
    make

