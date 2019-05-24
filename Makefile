COMPOSE_RUN = docker-compose run --rm --service-ports


.PHONY: run
run:
	docker-compose up

.PHONY: django-bash
django-bash:
	$(COMPOSE_RUN) django bash
