# pull official base image
FROM python:3.10.0-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/


# # copy sql files
# COPY *.sql /docker-entrypoint-initdb.d/
# ADD setup.sql /docker-entrypoint-initdb.d
# RUN chmod a+r /docker-entrypoint-initdb.d/*
# EXPOSE 6666


