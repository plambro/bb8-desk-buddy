FROM python:2

WORKDIR /app

RUN apt-get update && apt-get upgrade -y
RUN apt-get install bluez -y

ENV BB_ADDRESS='00:00:00:00:00'

COPY requirements.txt /app
COPY app.py /app
COPY BB8_driver.py /app
COPY bb8_utils.py /app

RUN pip install -r requirements.txt

CMD ['python', 'app.py']