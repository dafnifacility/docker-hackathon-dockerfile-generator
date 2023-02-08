FROM docker.io/library/python:3

RUN apt-get update && apt-get install git && rm -rf /var/lib/apt/lists/*

RUN pip install poetry

COPY . /application

WORKDIR /application
RUN pip install .
ENTRYPOINT python -m dockerfile_generator.entrypoint
