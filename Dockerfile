FROM python:3.12.0

WORKDIR /app

RUN apt-get update && apt-get upgrade -y
RUN apt-get install bluez -y

COPY requirements.txt /app
COPY app.py /app
COPY bb8_utils.py /app

RUN pip install -r requirements.txt

CMD ["python3", "app.py"]