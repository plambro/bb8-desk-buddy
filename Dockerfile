FROM python:2

WORKDIR /app

RUN apt-get update && apt-get upgrade

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ['sleep', '10000']