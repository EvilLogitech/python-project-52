install:
		poetry install

lint:
		poetry run flake8 --exclude=migrations,admin.py,settings.py\
		task_manager tasks users labels statuses locale

test:
		poetry run python3 manage.py test

test-coverage:
		poetry run coverage run --source='.' manage.py test
		poetry run coverage xml

start:
		poetry run python3 manage.py runserver