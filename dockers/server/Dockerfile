FROM main_code

WORKDIR /usr/src/app

CMD [ "python", "-m" ,"spirit.server","run-server", "rabbitmq://host.docker.internal:5672/", "custom.blob.scheme://host.docker.internal:9000", "-h", "0.0.0.0", "-p","8000"]
