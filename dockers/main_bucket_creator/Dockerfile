FROM python:3

WORKDIR /usr/src/app
COPY ./create_main_bucket.py .

RUN pip install minio
CMD [ "python", "./create_main_bucket.py" ,"host.docker.internal:9000"]
