#! /bin/bash

set -e

dir="$(dirname "$BASH_SOURCE")/docker"

echo "base"
echo "--------------------"
docker build -t base "$dir/base"

echo "postgres"
echo "--------------------"
docker build -t postgres "$dir/postgres"

echo "nginx"
echo "--------------------"
docker build -t nginx "$dir/nginx"

echo "django-python3"
echo "--------------------"
docker build -t django-python3 "$dir/django-python3"

echo 'Start the data container'
echo "--------------------"
docker-compose --file data-docker-compose.yml up -d

echo 'Please check the dev-docker-compose.yml & docker-compose.yml file!'
echo 'The proxy service volumes_from should be the created data container.'
