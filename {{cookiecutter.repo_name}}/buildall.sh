#! /bin/bash

echo "base"
echo "--------------------"
docker build \
  --build-arg "DEVELOPER_UID=$(id -u)" \
  --build-arg "DEVELOPER_GID=$(id -g)" \
  -t {{cookiecutter.repo_name}}-base "docker/base"

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

echo "nodejs"
echo "--------------------"
docker build -t {{cookiecutter.repo_name}}-nodejs "docker/nodejs"


echo 'Start the data container'
echo "--------------------"
docker-compose --file data-docker-compose.yml up -d

echo "Docker image cleanup"
echo "--------------------"
docker rmi `docker images --filter 'dangling=true' -q --no-trunc`
