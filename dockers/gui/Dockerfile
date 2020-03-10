FROM python:3

WORKDIR /usr/src/app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "-m" ,"spirit.cortex","run-server", "-h","0.0.0.0","-p","8080","-H","127.0.0.1","-P","5000"]
