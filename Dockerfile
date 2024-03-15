FROM python:3.12
RUN apt-get update && apt-get install -y python3-opencv
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app/
VOLUME [ "/app" ]
CMD [ "python3", "app.py" ]
