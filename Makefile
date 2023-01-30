compose = sudo docker-compose
lines?=all

init: init-envs pre-commit

pre-commit:
	pip install pre-commit --upgrade
	pre-commit install

init-envs:
	cp env.example .env
	cp config.example.yaml config.yaml

full-migrate: makemigrations migrate
makemigrations:
	$(compose) exec web ./manage.py makemigrations
migrate:
	$(compose) exec web ./manage.py migrate

shell:
	$(compose) exec web ./manage.py shell_plus

collectstatic:
	$(compose) exec web ./manage.py collectstatic

admin:
	$(compose) exec web ./manage.py createsuperuser

build:
	$(compose) up --build -d

logs:
	$(compose) logs -f --tail=$(lines)

stop:
	$(compose) stop

ps:
	$(compose) ps

down:
	$(compose) down