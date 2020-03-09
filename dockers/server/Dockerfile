FROM python:3

WORKDIR /usr/src/app
COPY . .


RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "-m" ,"spirit.server","run-server", "rabbitmq://host.docker.internal:5672/", "custom.blob.scheme://host.docker.internal:9000", "-h", "0.0.0.0", "-p","8000"]
