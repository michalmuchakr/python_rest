"# python_rest"

lint app:
    docker-compose run --rm app sh -c "flake8"

create new project called app
    docker-compose run --rm app sh "django-admin startproject app ."
