RUN_PYTHON=PYTHONPATH=./ poetry run

run:
	${RUN_PYTHON} python manage.py runserver

makemigrations:
	${RUN_PYTHON} python manage.py makemigrations

migrate:
	${RUN_PYTHON} python manage.py migrate

test:
	${RUN_PYTHON} python manage.py test .