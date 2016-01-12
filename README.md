# django-docker-bootstrap

## Concept
The main idea behind this project to create an easily configurable and easy to use django
development/production environment for any project.

## Installation
Install the docker,docker-compose - https://docs.docker.com/engine/installation/

## Images(/docker/ folder)
1. base - contains every data(db, files, logs) and connected to every other image as a volume
2. postgres - postgresql-9.4
3. django-python3(django) - Django 1.8.4 with python3
4. nginx

## Usage
### How to build the docker images
```sh bash buildall.sh ```

## Settings
### Environmental variables (env.txt):
```
DJANGO_SECRET_KEY='',
DB_PASSWORD=''
```