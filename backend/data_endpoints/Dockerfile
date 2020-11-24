# Use the official lightweight Python image.
FROM python:3.7-stretch
WORKDIR /app
COPY .  .
COPY 'tmp/google.json' 'google.json'
ENV GOOGLE_APPLICATION_CREDENTIALS './google.json'
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]