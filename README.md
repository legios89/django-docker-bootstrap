# django-docker-bootstrap

## Concept
The main idea behind this project to create an easily configurable and easy to use django
development/production environment for any project.

## Installation
* Install the docker,docker-compose - https://docs.docker.com/engine/installation/
* Build the images: ```bash buildall.sh```
* Start the project: ```docker-compose up ```
* If you want to run the project in dev mode you need to set the following environment variable:         
    * ```COMPOSE_FILE="dev-docker-compose.yml"```
    * https://docs.docker.com/compose/reference/overview/#compose-file

## Images
Every image has a container_shared directory linked as a volume, so if you want to put something inside the container, or
you want to get something from inside the containers like a backup file you just need to copy everything to this directory.

1. base
 * Contains every data(db, files, logs) and connected to every other container as a volume (/data/).
 * If you delete the base container you will lose everything (be cautious)
 * Commands:
   * shell - start a bash shell
2. postgres
 * postgresql-9.4
 * Commands:
    * shell - start a bash shell
    * backup - create a backup from the db (location: /data/backup/<backup_name>)
    * restore - restore the db from a backup file (location: /data/backup/<backup_name>)
3. django-python3
 * The projects can be found under the /src/ directory
 * Installed Apps:
    * Django: 1.9.1
    * uWSGI: 2.0.12
    * psycopg2: 2.6.1
 * Commands:
   * shell -start a bash shell
4. nginx
 * Commands:
   * shell -start a bash shell

### Environmental variables (env.txt):
First you need to create a ```env.txt``` in the root and set the followings:
```
DJANGO_SECRET_KEY=
DB_PASSWORD=
DEBUG=
```
