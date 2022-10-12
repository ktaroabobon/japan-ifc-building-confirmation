DOCKER_COMPOSE_VERSION_CHECKER := $(shell docker compose > /dev/null 2>&1 ; echo $$?)
ifeq ($(DOCKER_COMPOSE_VERSION_CHECKER), 0)
	DOCKER_COMPOSE_IMPL=docker compose
else
	DOCKER_COMPOSE_IMPL=docker-compose
endif

.PHONY: help
help:
	@echo "HELP FOR API"
	cat ./Makefile
	@echo "---------------"

.PHONY: docker-compose/build
docker-compose/build:
	$(DOCKER_COMPOSE_IMPL) build api

.PHONY: docker-compose/stop
docker-compose/stop:
	$(DOCKER_COMPOSE_IMPL) stop api

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

.PHONY: rerun
rerun:
	$(DOCKER_COMPOSE_IMPL) stop api
	$(MAKE) docker-compose/up-d
	$(MAKE) run

.PHONY: healthcheck
healthcheck:
	curl --request GET -sL \
	     --url 'http://0.0.0.0:8888/health/' \
	     --header 'Content-Type: application/json'

.PHONY: prod/healthcheck
prod/healthcheck:
	curl --request GET -sL \
	     --url 'http://0.0.0.0:8080/health/' \
	     --header 'Content-Type: application/json'

.PHONY: prod/healthcheck/params
prod/healthcheck/params:
	curl --request GET -sL \
	     --url 'http://0.0.0.0:8080/health/params' \
	     --header 'Content-Type: application/json' \
	     --data-raw '{"ifc": "value1", "zipped": true}'

.PHONY: docs
docs:
	open http://0.0.0.0:8888/docs

.PHONY: test
test:
	$(DOCKER_COMPOSE_IMPL) exec api poetry run python tests/test_main.py

.PHONY: token
token:
	gcloud auth print-identity-token | pbcopy
