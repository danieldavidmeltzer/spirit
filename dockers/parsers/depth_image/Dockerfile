FROM python:3

WORKDIR /usr/src/app
COPY . .


RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "-m" ,"spirit.parsers","run-parser", "depth_image", "rabbitmq://host.docker.internal:5672/", "-b", "custom.blob.scheme://host.docker.internal:9000"]
