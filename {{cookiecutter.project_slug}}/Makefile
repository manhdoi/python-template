docker-up:
	docker compose up --build -d

version:
	docker compose run --rm webserver {{cookiecutter.project_slug}} version

docker-build:
	docker build -t {{cookiecutter.project_slug}}:{{cookiecutter.version}} .

docker-down:
	docker compose down
