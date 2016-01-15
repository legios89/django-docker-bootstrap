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
docker build -t nginx 2"$dir/nginx"

echo "django-python3"
echo "--------------------"
docker build -t django-python3 "$dir/django-python3"
