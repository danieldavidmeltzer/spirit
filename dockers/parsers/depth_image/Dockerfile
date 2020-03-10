FROM main_code

WORKDIR /usr/src/app

CMD [ "python", "-m" ,"spirit.parsers","run-parser", "depth_image", "rabbitmq://host.docker.internal:5672/", "-b", "custom.blob.scheme://host.docker.internal:9000"]
