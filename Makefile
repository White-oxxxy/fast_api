DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
ENV = --env-file .dev.env
APP_FILE = docker_compose/app.yaml
STORAGES_FILE = docker_compose/storages.yaml
APP_CONTAINER = main-app

.PHONY: app
app:
	${DC} -f ${APP_FILE} ${ENV} up --build -d
	#docker-compose -f docker_compose/app.yaml --env-file .dev.env up --build -d

.PHONY: storages
storages:
	${DC} -f ${STORAGES_FILE} ${ENV} up --build -d
	#docker-compose -f docker_compose/storages.yaml --env-file .env up --build -d


.PHONY: app-down
app-down:
	${DC} -f ${APP_FILE} ${ENV} down

.PHONY: storages-down
storages-down:
	${DC} -f ${STORAGES_FILE} ${ENV} down
