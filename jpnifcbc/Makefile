DOCKER_COMPOSE_VERSION_CHECKER := $(shell docker compose > /dev/null 2>&1 ; echo $$?)
ifeq ($(DOCKER_COMPOSE_VERSION_CHECKER), 0)
	DOCKER_COMPOSE_IMPL=docker compose
else
	DOCKER_COMPOSE_IMPL=docker-compose
endif

.PHONY: help
help:
	@echo "HELP FOR JPNIFCBC"
	cat ./Makefile
	@echo "---------------"

.PHONY: build
build:
	$(MAKE) up-d

.PHONY: docker-compose/build
docker-compose/build:
	$(DOCKER_COMPOSE_IMPL) build app

.PHONY: docker-compose/stop
docker-compose/stop:
	$(DOCKER_COMPOSE_IMPL) stop app

.PHONY: poetry/install
poetry/install:
	$(DOCKER_COMPOSE_IMPL) exec app poetry install

.PHONY: poetry/update
poetry/update:
	$(DOCKER_COMPOSE_IMPL) exec app poetry update

.PHONY: poetry/add
poetry/add:
	$(DOCKER_COMPOSE_IMPL) exec app poetry add $(package)

.PHONY: healthcheck
healthcheck:
	$(DOCKER_COMPOSE_IMPL) exec app poetry run python test.py
