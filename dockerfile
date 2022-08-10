FROM python:3.9

COPY . /usr/app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/app/

RUN pip install -r requirements.txt

CMD python app.py
