FROM python:3.8-slim-buster
RUN apt update; apt install python3-pip -y
COPY . .
RUN /usr/bin/pip3 install -r requirements.txt
ENTRYPOINT [ "python3" ] 
CMD [ "main.py" ] 
