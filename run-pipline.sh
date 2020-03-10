#!/bin/bash

echo "we are building a seperate image for each docker, as the code should,
theoraticlly be independet, please be patient as it could take some time"

# create random keys if needed or use provided ones
MINIO_ACCESS_KEY=${1:-$(cat /dev/urandom | LC_ALL=C tr -dc 'a-zA-Z0-9' | head -c 10)}
MINIO_SECRET_KEY=${2:-$(cat /dev/urandom | LC_ALL=C tr -dc 'a-zA-Z0-9' | head -c 32)}
echo 'access_key': "$MINIO_ACCESS_KEY"
echo 'secret_key': "$MINIO_SECRET_KEY"

docker network create my-net

echo "running minio project"
docker run --network=my-net -p 9000:9000 -d   \
  -e "MINIO_ACCESS_KEY=$MINIO_ACCESS_KEY" \
  -e "MINIO_SECRET_KEY=$MINIO_SECRET_KEY" \
  minio/minio server /data

# the docker images i create are very similiar but they may differ in future
# so i don't create one image for all,( each would have been seperate project
# with seperate reqs)

echo "creating main bucket using python sdk"
docker build -f dockers/main_bucket_creator/Dockerfile . -t main_bucket_creator
docker run --network=my-net \
  -e "MINIO_ACCESS_KEY=$MINIO_ACCESS_KEY" \
  -e "MINIO_SECRET_KEY=$MINIO_SECRET_KEY" \
  -d  --name main_bucket_creator main_bucket_creator

echo "runing rabbitmq"
docker run -d -p 5672:5672 --network=my-net --rm --name rabbitmq \
 rabbitmq:3-management

python ./block_until_rabbitmq_ready.py

echo "running mongodb"
docker run -d -p 27017:27017 --network=my-net  mongo


#create server image
docker build -f dockers/server/Dockerfile . -t server


echo "running server"
docker run  --network=my-net  \
  -e "MINIO_ACCESS_KEY=$MINIO_ACCESS_KEY" \
  -e "MINIO_SECRET_KEY=$MINIO_SECRET_KEY" \
  -d -p 8000:8000 --name server server

echo "run saver"
docker build -f dockers/saver/Dockerfile . -t saver
docker run  --network=my-net -d  --name saver saver

echo "running parsers"
echo "running color image parser"
docker build -f dockers/parsers/color_image/Dockerfile . -t color_image_parser
docker run --network=my-net  \
  -e "MINIO_ACCESS_KEY=$MINIO_ACCESS_KEY" \
  -e "MINIO_SECRET_KEY=$MINIO_SECRET_KEY" \
  -d  --name color_image_parser color_image_parser

echo "running depth image parser"
docker build -f dockers/parsers/depth_image/Dockerfile . -t depth_image_parser
docker run  --network=my-net \
  -e "MINIO_ACCESS_KEY=$MINIO_ACCESS_KEY" \
  -e "MINIO_SECRET_KEY=$MINIO_SECRET_KEY" \
  -d  --name depth_image_parser depth_image_parser

echo "running pose parser"
docker build -f dockers/parsers/pose/Dockerfile . -t pose_parser
docker run  --network=my-net  -d  --name pose_parser pose_parser

echo "running feelings parser"
docker build -f dockers/parsers/feelings/Dockerfile . -t feelings_parser
docker run --network=my-net  -d  --name feelings_parser feelings_parser

echo "run api"
docker build -f dockers/api/Dockerfile . -t api
docker run --network=my-net  \
  -p 5000:5000 \
  -e "MINIO_ACCESS_KEY=$MINIO_ACCESS_KEY" \
  -e "MINIO_SECRET_KEY=$MINIO_SECRET_KEY" \
  -d  --name api api

echo "run gui"
docker build -f dockers/gui/Dockerfile . -t gui
docker run --network=my-net  \
  -p 8080:8080 \
  -d  --name gui gui