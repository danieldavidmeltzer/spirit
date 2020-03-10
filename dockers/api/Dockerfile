FROM main_code

WORKDIR /usr/src/app

CMD [ "python", "-m" ,"spirit.api","run-server", "-h","0.0.0.0","-p","5000","-d","mongodb://host.docker.internal:27017","-b","custom.blob.scheme://host.docker.internal:9000"]
