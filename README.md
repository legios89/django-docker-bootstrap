# django-docker-bootstrap

## Concept
The main idea behind this project to create an easily configurable and easy to use django
development/production environment for any project.

## Installation
Install the docker,docker-compose - https://docs.docker.com/engine/installation/

## Images
How to build the images: ```bash buildall.sh```

1. base
  * Contains every data(db, files, logs) and connected to every other container as a volume.
  * If you delete the base conatainer you will lose everything (be cautious)ű
  * Commands:
    * shell - start a bash shell
2. postgres - postgresql-9.4
3. django-python3(django) - Django 1.8.4 with python3
4. nginx

### Environmental variables (env.txt):
First you need to create an env.txt in the root and set the followings:
```
DJANGO_SECRET_KEY=
DB_PASSWORD=
```
