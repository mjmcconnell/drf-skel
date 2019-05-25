COMPOSE_RUN = docker-compose run --rm --service-ports
DJANGO_CONTAINER = $(shell docker ps -qf "name=drf-skel_django")


.PHONY: run
run:
	$(COMPOSE_RUN) django make migrate
	docker-compose up

.PHONY: django-attach
django-attach:
	docker exec -it $(DJANGO_CONTAINER) bash

.PHONY: test
test:
	$(COMPOSE_RUN) django make test
