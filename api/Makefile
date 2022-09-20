DOCKER_COMPOSE_VERSION_CHECKER := $(shell docker compose > /dev/null 2>&1 ; echo $$?)
ifeq ($(DOCKER_COMPOSE_VERSION_CHECKER), 0)
	DOCKER_COMPOSE_IMPL=docker compose
else
	DOCKER_COMPOSE_IMPL=docker-compose
endif

.PHONY: help
help:
	cat ./Makefile

.PHONY: poetry/install
poetry/install:
	$(DOCKER_COMPOSE_IMPL) exec api poetry install

.PHONY: poetry/update
poetry/update:
	$(DOCKER_COMPOSE_IMPL) exec api poetry update

.PHONY: poetry/add
poetry/add:
	$(DOCKER_COMPOSE_IMPL) exec api poetry add $(package)

.PHONY: run
run:
	$(DOCKER_COMPOSE_IMPL) exec api poetry run uvicorn main:app --reload --host 0.0.0.0 --port 8888

.PHONY: healthcheck
healthcheck:
	curl --request GET -sL \
	     --url 'http://0.0.0.0:8888/health/' \
	     --header 'Content-Type: application/json'

.PHONY: docs
docs:
	open http://0.0.0.0:8888/docs