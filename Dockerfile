FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir app
WORKDIR app/

RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

COPY requirements.txt drfhalyksite database_dump.sql ./

RUN pip install --no-cache-dir --upgrade pip && \
    pip install -r requirements.txt

RUN apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/*



