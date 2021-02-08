FROM python:3.9.1-slim-buster

RUN apt-get update -y && \
    apt-get install -y netcat

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

RUN chmod +x entrypoint.sh

ENTRYPOINT "./entrypoint.sh"
