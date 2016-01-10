#! /bin/bash

set -e

dir="$(dirname "$BASH_SOURCE")/docker"

echo "base"
echo "--------------------"
docker build -t base "$dir/base"

echo "postgres"
echo "--------------------"
docker build -t vertisfinance/core "$dir/postgres"

echo "nginx"
echo "--------------------"
docker build -t vertisfinance/core "$dir/nginx"

echo "django-python3"
echo "--------------------"
docker build -t vertisfinance/core "$dir/django-python3"
