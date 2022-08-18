FROM python:3.9

COPY . /usr/app/

WORKDIR /usr/app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 80

RUN pip install -r requirements.txt

RUN ['gunicorn' '-w' '4' 'app:app']
