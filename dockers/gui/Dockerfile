FROM python:3

WORKDIR /usr/src/app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "-m" ,"spirit.gui","run-server", "-h","0.0.0.0","-p","8080","-H","host.docker.internal","-P","5000"]
