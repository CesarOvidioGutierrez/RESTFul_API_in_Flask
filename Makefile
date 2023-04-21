# CONSTANTS
FILE=docker-compose.yml
WEB=`docker compose ps | grep 5000 | cut -d\  -f 1 | head -n 1`
MONGO=`docker compose ps | grep 27017 | cut -d\  -f 1`

# ACTIONS
build:
	docker compose -f $(FILE) build

up:
	docker compose -f $(FILE) up -d

start:
	docker compose -f $(FILE) start

stop:
	docker compose -f $(FILE) stop

ps-a:
	docker compose -f $(FILE) ps -a

up-build:
	docker compose -f $(FILE) up -d --build

prune:
	docker compose down --volumes --remove-orphans

# SHELLS#
shell-web:
	docker exec -ti $(WEB) bash

shell-db:
	docker exec -ti $(MONGO) bash


# LOGS
log-web:
	docker compose logs web

log-web-live:
	docker compose logs web -f

log-db:
	docker compose logs

log-db:
	docker compose logs -f 
