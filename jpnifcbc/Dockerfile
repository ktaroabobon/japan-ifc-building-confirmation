FROM python:3.10

ENV APP_PATH=/code \
    PYTHONPATH=.

WORKDIR $APP_PATH

RUN apt-get update && \
    apt-get update -y && \
    pip install poetry

COPY ./jpnifcbc .

RUN poetry config virtualenvs.create false && \
    poetry install --no-dev

EXPOSE 8000