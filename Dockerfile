FROM python:3.10.11-slim-bullseye
WORKDIR /apps/shop
ARG base_path=/apps
RUN apt-get update -y
RUN apt-get -y install libpq-dev gcc -y
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

