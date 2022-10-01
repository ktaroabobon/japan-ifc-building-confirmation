DOCKER_COMPOSE_VERSION_CHECKER := $(shell docker compose > /dev/null 2>&1 ; echo $$?)
ifeq ($(DOCKER_COMPOSE_VERSION_CHECKER), 0)
	DOCKER_COMPOSE_IMPL=docker compose
else
	DOCKER_COMPOSE_IMPL=docker-compose
endif


# Make command for all
.PHONY: help
help:
	@echo "HELP FOR ALL"
	cat ./Makefile
	@echo "---------------"

.PHONY: build
build:
	$(MAKE) docker-compose/up-d
	$(MAKE) -C api run

.PHONY: docker-compose/build
docker-compose/build:
	$(DOCKER_COMPOSE_IMPL) build

.PHONY: docker-compose/up
docker-compose/up:
	$(DOCKER_COMPOSE_IMPL) up

.PHONY: docker-compose/up-d
docker-compose/up-d:
	$(DOCKER_COMPOSE_IMPL) up -d

.PHONY: docker-compose/down
docker-compose/down:
	$(DOCKER_COMPOSE_IMPL) down

.PHONY: run
run:
	$(MAKE) -C api run
	$(MAKE) docs

.PHONY: rerun
rerun:
	$(DOCKER_COMPOSE_IMPL) stop api
	$(MAKE) docker-compose/up-d
	$(MAKE) run

.PHONY: api/healthcheck
api/healthcheck:
	$(MAKE) -C api healthcheck

.PHONY: app/healthcheck
app/healthcheck:
	$(MAKE) -C jpnifcbc healthcheck

.PHONY: api/test
api/test:
	$(MAKE) -C api test

.PHONY: docs
docs:
	$(MAKE) -C api docs

.PHONY: logs
logs:
	$(DOCKER_COMPOSE_IMPL) logs -f

.PHONY: docker-compose/logs
docker-compose/logs:
	$(DOCKER_COMPOSE_IMPL) logs -f

.PHONY: api/poetry/install
api/poetry/install:
	$(MAKE) -C api poetry/install

.PHONY: api/poetry/update
api/poetry/update:
	$(MAKE) -C api poetry/update

.PHONY: api/poetry/add
api/poetry/add:
	$(MAKE) -C api poetry/add package=$(package)

.PHONY: app/poetry/install
app/poetry/install:
	$(MAKE) -C jpnifcbc poetry/install

.PHONY: app/poetry/update
app/poetry/update:
	$(MAKE) -C jpnifcbc poetry/update

.PHONY: app/poetry/add
app/poetry/add:
	$(MAKE) -C jpnifcbc poetry/add package=$(package)
