FROM python:3.10-slim

RUN apt-get update && apt-get install -y wget vim nano build-essential libssl-dev libpq-dev

COPY manage.py .
COPY pyproject.toml .
COPY poetry.lock .
RUN pip install --upgrade pip
RUN pip install poetry 
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi;

RUN apt-get clean
