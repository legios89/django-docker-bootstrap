#! /bin/bash
set -e
dir="{{cookiecutter.repo_name}}/docker"

echo "base"
echo "--------------------"
docker build -t {{cookiecutter.repo_name}}-base "$dir/base"

echo "postgres"
echo "--------------------"
docker build -t {{cookiecutter.repo_name}}-postgres "$dir/postgres"

echo "nginx"
echo "--------------------"
docker build -t {{cookiecutter.repo_name}}-nginx "$dir/nginx"

echo "django-python3"
echo "--------------------"
docker build -t {{cookiecutter.repo_name}}-django-python3 "$dir/django-python3"

echo 'Start the data container'
echo "--------------------"
docker-compose --file data-docker-compose.yml up -d
