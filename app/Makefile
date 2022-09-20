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
	$(DOCKER_COMPOSE_IMPL) exec app poetry install

.PHONY: poetry/update
poetry/update:
	$(DOCKER_COMPOSE_IMPL) exec app poetry update

.PHONY: app/poetry/add
app/poetry/add:
	$(DOCKER_COMPOSE_IMPL) exec app poetry add $(package)

.PHONY: run
run:
	$(DOCKER_COMPOSE_IMPL) exec app poetry run python main.py
