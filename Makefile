install:
		poetry install

migrate:
		poetry run python manage.py makemigrations
		poetry run python manage.py migrate

build: install migrate

lint:
		poetry run flake8 --exclude=migrations,admin.py,settings.py\
		task_manager tasks users labels statuses locale

test:
		poetry run python3 manage.py test

test-coverage:
		poetry run coverage run --source='.' manage.py test
		poetry run coverage xml

dev:
		poetry run python3 manage.py runserver

start:
		poetry run gunicorn task_manager.wsgi