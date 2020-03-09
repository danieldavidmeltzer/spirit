FROM python:3

WORKDIR /usr/src/app
COPY . .


RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "-m" ,"spirit.saver","run-saver", "mongodb://host.docker.internal:27017", "rabbitmq://host.docker.internal:5672/"]
