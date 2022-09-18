.PHONY: help
help:
	cat Makefile

DOCKER_COMPOSE_VERSION_CHECKER := $(shell docker compose > /dev/null 2>&1 ; echo $$?)
ifeq ($(DOCKER_COMPOSE_VERSION_CHECKER), 0)
	DOCKER_COMPOSE_IMPL=docker compose
else
	DOCKER_COMPOSE_IMPL=docker-compose
endif

.PHONY: up
up:
	$(DOCKER_COMPOSE_IMPL) up

.PHONY: up-d
up-d:
	$(DOCKER_COMPOSE_IMPL) up -d

.PHONY: down
down:
	$(DOCKER_COMPOSE_IMPL) down

.PHONY: poetry/install
poetry/install:
	$(DOCKER_COMPOSE_IMPL) exec app poetry install

.PHONY: poetry/update:
poetry/update:
	$(DOCKER_COMPOSE_IMPL) exec app poetry update

.PHONY: poetry/add
poetry/add:
	$(DOCKER_COMPOSE_IMPL) exec app poetry add $(package)

.PHONY: run
run:
	$(DOCKER_COMPOSE_IMPL) exec app poetry run python main.py

.PHONY: logs
logs:
	$(DOCKER_COMPOSE_IMPL) logs -f
