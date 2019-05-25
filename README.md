# Django Rest Framework skeleton app

This project is setup to introduce some basic principles for setting up a web API project using the Django and Django Rest Framework frameworks.

## Getting started

This project has been setup to include [Docker](https://docs.docker.com/install/#server) and [docker-compose](https://docs.docker.com/compose/install/) to help with local development, along with a `Makefile` to wrap the docker commands up into easy to remember commands.

Once you have docker-compose setup and running locally, from your terminal simply run

    make run

This will spin up a Django web server running on port `8080`, along with a PostgreSQL database on port `5432`.

For reference there is a single app running under the `app/apps` directory "foo" that you can visit. From your browser navigate to [http://localhost:8080/foo](http://localhost:8080/foo).

### Create local user

When you initially start the app, the database will be empty, including the users table.
To create an admin account, with the app running, open a new terminal window and run:

    make django-attach

**Note if you have changed the name of the repo in your local environment, you will need to update `DJANGO_CONTAINER` variable in the `Makefile` at the root of the project to reflect the projects name**

This is create a session within the running django container. Then to add a user simple run:

    make createadmin

## Installed packeages

### Gloabl
[pipenv](https://docs.pipenv.org/en/latest/)
Manages python packages in virutal environments (similar to virtualenv).
This project installs all pipenv packages on the system level, negating the need for virtualisation (as docker handles that for us),
but pipenv provides a more robust package management system that pip.

[Django](https://docs.djangoproject.com): Rapid development framework

[djangorestframework](https://www.django-rest-framework.org): Rest API framework built onto of Django

[psycopg2](http://initd.org/psycopg/docs/): Database driver for the PostgreSQL engine

[json-logging](https://github.com/thangbn/json-logging-python): Logs are rendered in JSON format, for easier parsing by logging services, such as Cloudwatch and Datadog

[black](https://github.com/python/black): Auto formatting of all python files

[isort](https://readthedocs.org/projects/isort/): Manages python import path ordering

### Development
[Markdown](https://python-markdown.github.io/): For browserable API

### Testing
[pytest](https://docs.pytest.org/en/latest/): Testing framework
There are also a number of plugins for the pytest tool used:
* [pytest-django](https://pytest-django.readthedocs.io/en/latest/): Plugin for running the django test suite via pytest
* [pytest-cov](https://github.com/pytest-dev/pytest-cov): Plugin for providing test coverage statistics
* [pytest-flakes](https://github.com/fschulze/pytest-flakes): Plugin for checking for linting errors based on the flakes defination
* [pytest-pep8](https://bitbucket.org/pytest-dev/pytest-pep8): Plugin for checking for linting errors based on the pep8 defination
* [pytest-mccabe](https://github.com/The-Compiler/pytest-mccabe): Plugin for checking cyclomatic complexity of the python files
