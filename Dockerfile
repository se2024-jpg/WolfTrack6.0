FROM python:3.8-slim-buster

RUN apt-get update
RUN apt-get -y install gcc

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install -r /app/requirements.txt

COPY . /app

ENTRYPOINT [ "python3", "main.py" ]
