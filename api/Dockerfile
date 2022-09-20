FROM duffn/python-poetry:3.10.2-slim-1.2.1

RUN apt-get update -y \
    && apt-get upgrade -y
RUN apt-get -yqq install ssh


ARG DEPLOY_KEY

ENV APP_PATH=/code \
    PYTHONPATH=.

WORKDIR /root/.ssh

RUN echo $DEPLOY_KEY | base64 --decode > ./id_rsa
RUN ssh-keyscan github.com >> ./known_hosts
RUN chmod 600 ./*

WORKDIR $APP_PATH

COPY ./api .

RUN poetry install

EXPOSE 8888