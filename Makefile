# these will speed up builds, for docker-compose >= 1.25
export COMPOSE_DOCKER_CLI_BUILD=1
export DOCKER_BUILDKIT=1

.PHONY: help

.DEFAULT_GOAL := help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


flake8: ## Run flake8 for code style checks
	docker compose run --rm web flake8 .

black: ## black
	black . --line-length=100 --exclude migrations\

isort: ## isort
	isort .

build: ## build
	docker compose build

up: ## up
	docker compose up

up-d: ## up d
	docker compose up -d

down: ## down
	docker compose down --remove-orphans

down-d: ## down
	docker compose down --remove-orphans --rmi local

run:  ## run
	docker compose run --rm --service-ports web ${ARGS}

makemigrations:  ## makemigrations
	docker compose run --rm --entrypoint=python web manage.py makemigrations

showmigrations:  ## showmigrations
	docker compose run --rm --entrypoint=python web manage.py showmigrations

migrate: ## migrate
	docker compose run --rm --entrypoint=python web manage.py migrate

migrate-fake: ## migrate
	docker compose run --rm --entrypoint=python web manage.py migrate --fake

reset-db: ## reset_db
	docker compose run --rm --entrypoint=python web manage.py reset_db -c

shell: ## shell
	docker compose run --rm --entrypoint=python web manage.py shell_plus

run-tests:  # run-tests
	docker compose run --rm --no-deps --entrypoint=pytest web /tests/ $(ARGS)

docker-attach: ## docker attach
	docker attach --detach-keys ctrl-d ${CONTAINER_ID}

dev-setup: ## Dev: Setup development environment
	@pip install  -Ur requirements/development.txt
