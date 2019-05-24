install:
	pipenv install --dev

run: install
	python manage.py runserver 0.0.0.0:8080

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

createadmin:
	python manage.py createsuperuser --email admin@example.com --username admin
