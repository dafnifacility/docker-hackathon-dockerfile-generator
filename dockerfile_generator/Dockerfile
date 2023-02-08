FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

COPY install_cmake.sh .
RUN bash install_cmake.sh && rm install_cmake.sh

