PY_ENV = pipenv run


.PHONY: install
install:
	pipenv install --system --dev --pre

.PHONY: lint
lint: install
	$(PY_ENV) isort -rc .
	$(PY_ENV) black .

.PHONY: run
run: install
	$(PY_ENV) python manage.py runserver 0.0.0.0:8080

.PHONY: migrations
migrations:
	$(PY_ENV) python manage.py makemigrations

.PHONY: migrate
migrate:
	$(PY_ENV) python manage.py migrate

.PHONY: createadmin
createadmin:
	$(PY_ENV) python manage.py createsuperuser

test:
	$(PY_ENV) pipenv run pytest --flakes --mccabe --pep8 --cov=.
