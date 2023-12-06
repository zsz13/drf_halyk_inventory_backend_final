FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir app
WORKDIR app/

RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

COPY requirements.txt .
COPY drfhalyksite .
COPY database_dump.sql .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install -r requirements.txt

RUN apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/*





## Используем базовый образ Python 3.8
#FROM python:3.8
#
## Устанавливаем переменные окружения
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
#
## Создаем директорию для приложения
#RUN mkdir /app
#WORKDIR /app/
#
## Создаем виртуальное окружение
#RUN python -m venv /venv
#ENV PATH="/venv/bin:$PATH"
#
## Копируем зависимости и код приложения
#COPY requirements.txt .
#COPY drfhalyksite .
#COPY database_dump.sql .
#
## Устанавливаем зависимости
#RUN pip install --no-cache-dir --upgrade pip && \
#    pip install -r requirements.txt
#
## Устанавливаем PostgreSQL клиентские утилиты
#RUN apt-get update \
#    && apt-get install -y postgresql-client \
#    && apt-get autoremove -y \
#    && apt-get clean \
#    && rm -rf /var/lib/apt/lists/*
#
## Очищаем лишние пакеты
#RUN apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/*

