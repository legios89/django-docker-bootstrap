# django-docker-bootstrap

## Concept
The main idea behind this project to create an easily configurable and easy to use django
development/production environment for any project.

## Installation
* Install the docker(1.9.1),docker-compose(1.6.0) - https://docs.docker.com/engine/installation/
* Then get cookiecutter: ```pip install cookiecutter```
* Finally enter the directory where you want to store your project and enter the following:
      * ```cookiecutter https://github.com/legios89/django-docker-bootstrap.git```

# Usage
* Build the images: ```bash buildall.sh```
* Start the project: ```docker-compose up ```
* You can set every secret variable in the  ```env.txt``` in the root
* If you want to run the project in production mode you need to set the following environment variable:         
    * ```COMPOSE_FILE="production-docker-compose.yml"```
    * https://docs.docker.com/compose/reference/overview/#compose-file

## Tips & Tricks
* Every image has a container_shared directory linked as a volume, so if you want to put something inside the container, or
you want to get something from inside the containers like a backup file you just need to copy everything to this directory.
* Create a bash alias for for the docker-compose by edit the ```.bash_aliases``` file ```alias dc='docker-compose'```
* If you want to use sudo inside the container you need to enter as a root: ```dc run --rm django shell root```

## Images
1. base
 * Contains every data(db, files, logs) and connected to every other container as a volume (/data/).
 * If you delete the base container you will lose everything (be cautious)
2. postgres
 * postgresql-9.4
 * Commands:
    * shell - start a bash shell ```dc run --rm postgres shell```
    * backup - create a backup (```/data/backup/<backup_name>```) ```dc run --rm postgres backup```
    * restore - restore from a backup (```/data/backup/<backup_name>```) ```dc run --rm postgres restore```
3. django-python3
 * The projects can be found under the /src/ directory
 * Installed Apps:
    * Django: 1.9.1
    * uWSGI: 2.0.12
    * psycopg2: 2.6.1
    * django-debug-toolbar: 1.4
    * djangorestframework: 3.3.2 + optional packages
    * django-rosetta: (fork from 0.7.8) [optional]
    * django-modeltranslation: 0.11rc2 [optional]
 * Commands:
   * shell -start a bash shell ```dc run --rm django shell```
4. nginx
 * Commands:
   * shell -start a bash shell ```dc run --rm nginx shell```
   * Installed Apps:
      * Nginx: 1.8.1
