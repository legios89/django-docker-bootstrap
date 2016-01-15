# django-docker-bootstrap

## Concept
The main idea behind this project to create an easily configurable and easy to use django
development/production environment for any project.

## Installation
Install the docker,docker-compose - https://docs.docker.com/engine/installation/
Build the images: ```bash buildall.sh```
Start the project: ```docker-compose up ```

## Images
1. base
 * Contains every data(db, files, logs) and connected to every other container as a volume (/data/).
 * If you delete the base conatainer you will lose everything (be cautious)
 * Commands:
   * shell - start a bash shell
2. postgres
 * postgresql-9.4
 * Commands:
   * shell -start a bash shell
3. django-python3
 * The projects can be found under the /src/ directory
 * Installed apps:
    * Django: 1.9.1
    * uWSGI: 2.0.12
    * psycopg2: 2.6.1
 * Commands:
   * shell -start a bash shell
4. nginx

### Environmental variables (env.txt):
First you need to create an env.txt in the root and set the followings:
```
DJANGO_SECRET_KEY=
DB_PASSWORD=
```
