.PHONY: install
install:
	pipenv install --system --dev --pre

.PHONY: lint
lint: install
	isort -rc .
	black .

.PHONY: run
run: install
	python manage.py runserver 0.0.0.0:8080

.PHONY: migrations
migrations:
	python manage.py makemigrations

.PHONY: migrate
migrate:
	python manage.py migrate

.PHONY: createadmin
createadmin:
	python manage.py createsuperuser --email admin@example.com --username admin
