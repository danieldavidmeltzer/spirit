FROM python:3

WORKDIR /usr/src/app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "-m" ,"spirit.api","run-server", "-h","0.0.0.0","-p","5000","-d","mongodb://host.docker.internal:27017","-b","custom.blob.scheme://host.docker.internal:9000"]
