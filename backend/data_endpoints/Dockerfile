FROM stifstof/backend_base:latest
WORKDIR /app
# Install production dependencies.
RUN pip install Flask gunicorn flask-cors

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD exec gunicorn --bind :8080 --workers 1 --threads 8 --timeout 0 app:app