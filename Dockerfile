FROM python:3.9
FROM node:18
MAINTAINER wenchaoh997

RUN mkdir /code

WORKDIR /code

ADD . /code

RUN pip install -r requirements.txt
