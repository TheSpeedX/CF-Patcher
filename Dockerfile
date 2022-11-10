FROM python:3.8-slim-buster
RUN apt update; apt install python3-pip -y
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ] 
CMD [ "main.py" ] 
