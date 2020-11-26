# Use the official lightweight Python image.
FROM python:3.7-stretch
WORKDIR /app

COPY 'google.json' 'google.json'
ENV GOOGLE_APPLICATION_CREDENTIALS './google.json'

RUN apt-get update -y
RUN apt-get upgrade -y