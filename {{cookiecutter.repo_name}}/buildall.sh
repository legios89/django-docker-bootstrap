#! /bin/bash

echo "base"
echo "--------------------"
docker build -t {{cookiecutter.repo_name}}-base "docker/base"

echo "postgres"
echo "--------------------"
docker build -t {{cookiecutter.repo_name}}-postgres "docker/postgres"

echo "nginx"
echo "--------------------"
docker build -t {{cookiecutter.repo_name}}-nginx "docker/nginx"

echo "django-python3"
echo "--------------------"
docker build \
  --build-arg "CACHE_DATE=$(date)" \
  -t {{cookiecutter.repo_name}}-django-python3 "docker/django-python3"


echo 'Start the data container'
echo "--------------------"
docker-compose --file data-docker-compose.yml up -d
