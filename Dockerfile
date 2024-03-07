FROM python:3.10

WORKDIR /usr/src

RUN mkdir app

COPY app/requirements.txt app/

RUN pip install --upgrade pip
RUN pip install -r app/requirements.txt