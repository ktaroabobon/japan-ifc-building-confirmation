FROM duffn/python-poetry:3.10-slim-1.2.0

ENV APP_PATH=/code \
    PYTHONPATH=.

WORKDIR $APP_PATH

COPY ./jpnifcbc .

RUN poetry install

EXPOSE 8000