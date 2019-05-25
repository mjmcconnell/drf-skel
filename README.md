## Installed packeds

### Python

#### Gloabl

[pipenv](https://docs.pipenv.org/en/latest/)
Manages python packages in virutal environments (similar to virtualenv).
This project installs all pipenv packages on the system level, negating the need for virtualisation (as docker handles that for us),
but pipenv provides a more robust package management system that pip.


[Django](https://docs.djangoproject.com)
Rapid development framework

[djangorestframework](https://www.django-rest-framework.org)
Rest API framework built onto of Django

[psycopg2](http://initd.org/psycopg/docs/)
Database driver for the PostgreSQL engine

[json-logging](https://github.com/thangbn/json-logging-python)
Logs are rendered in JSON format, for easier parsing by logging services, such as Cloudwatch and Datadog

[black](https://github.com/python/black)
Auto formatting of all python files

[isort](https://readthedocs.org/projects/isort/)
Manages python import path ordering

#### Development
[Markdown](https://python-markdown.github.io/)
For browserable API

#### Testing

[pytest](https://docs.pytest.org/en/latest/)
Testing framework
There are also a number of plugins for the pytest tool used:
* [pytest-django](https://pytest-django.readthedocs.io/en/latest/)
  * Plugin for running the django test suite via pytest
* [pytest-cov](https://github.com/pytest-dev/pytest-cov)
  * Plugin for providing test coverage statistics
* [pytest-flakes](https://github.com/fschulze/pytest-flakes)
  * Plugin for checking for linting errors based on the flakes defination
* [pytest-pep8](https://bitbucket.org/pytest-dev/pytest-pep8)
  * Plugin for checking for linting errors based on the pep8 defination
* [pytest-mccabe](https://github.com/The-Compiler/pytest-mccabe)
  * Plugin for checking cyclomatic complexity of the python files
