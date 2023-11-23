FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir app

WORKDIR app/

COPY requirements.txt .
COPY drfhalyksite .

#RUN ls -al

RUN pip install --upgrade pip && pip install -r requirements.txt



