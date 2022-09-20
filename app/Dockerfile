FROM duffn/python-poetry:3.10.2-slim-1.2.1

ENV APP_PATH=/code \
    PYTHONPATH=.

WORKDIR $APP_PATH

COPY ./app .

RUN poetry install

EXPOSE 8000