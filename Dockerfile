FROM python:3.10.8

WORKDIR /app

COPY requirements.txt

RUN pip3 install -r requirements.txt

CMD python3 bot.py
