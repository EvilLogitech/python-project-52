install:
		poetry install

build:
		./build.sh

lint:
		poetry run flake8 page_analyzer
		poetry run flake8 tests

test:
		poetry run pytest --cov

remove:
		python3 -m pip uninstall hexlet-code

test-coverage:
		poetry run pytest --cov=page_analyzer tests/ --cov-report xml

PORT ?= 8000
start:
		python3 manage.py runserver