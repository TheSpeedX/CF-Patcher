FROM python:3.10-slim-buster
COPY . .
RUN /usr/bin/pip3 install -r requirements.txt
ENTRYPOINT [ "python3" ] 
CMD [ "main.py" ] 
