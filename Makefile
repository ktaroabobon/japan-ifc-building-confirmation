DOCKER_COMPOSE_VERSION_CHECKER := $(shell docker compose > /dev/null 2>&1 ; echo $$?)
ifeq ($(DOCKER_COMPOSE_VERSION_CHECKER), 0)
	DOCKER_COMPOSE_IMPL=docker compose
else
	DOCKER_COMPOSE_IMPL=docker-compose
endif

.PHONY: help
help:
	cat ./Makefile

.PHONY: up
up:
	$(DOCKER_COMPOSE_IMPL) up

.PHONY: up-d
up-d:
	$(DOCKER_COMPOSE_IMPL) up -d

.PHONY: down
down:
	$(DOCKER_COMPOSE_IMPL) down

.PHONY: app/poetry/install
app/poetry/install:
	$(MAKE) -C app poetry/install

.PHONY: app/poetry/update
app/poetry/update:
	$(MAKE) -C app poetry/updates

.PHONY: app/poetry/add
app/poetry/add:
	$(MAKE) -C app poetry/add package=$(package)

.PHONY: api/poetry/install
api/poetry/install:
	$(MAKE) -C api poetry/install

.PHONY: api/poetry/update
api/poetry/update:
	$(MAKE) -C api poetry/updates

.PHONY: api/poetry/add
api/poetry/add:
	$(MAKE) -C api poetry/add package=$(package)

.PHONY: app/healthcheck
app/healthcheck:
	$(MAKE) -C app healthcheck

.PHONY: app/run
app/run:
	$(MAKE) -C app run

.PHONY: logs
logs:
	$(DOCKER_COMPOSE_IMPL) logs -f
