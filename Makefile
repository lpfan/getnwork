makemigrations:
	docker-compose run --rm --service-ports web python manage.py makemigrations

migrate:
	docker-compose run --rm --service-ports web python manage.py migrate

startdevserver:
	docker-compose run --rm --service-ports web python manage.py runserver 0.0.0.0:8000

createsuperuser:
	docker-compose run --rm --service-ports web python manage.py createsuperuser

collectstatic:
	docker-compose run --rm --service-ports web python manage.py collectstatic
