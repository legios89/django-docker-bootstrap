FROM {{cookiecutter.repo_name}}-base
RUN set -x && apt-get update && DEBIAN_FRONTEND=noninteractive \
      apt-get install -y --no-install-recommends \
        libpq5 \
        libpython3.4 \
        libpq-dev \
        build-essential \
        python3-dev

RUN pip3 install \
      uwsgi==2.0.13.1 \
      django==1.10.1 \
      psycopg2==2.6.2 \
      django-debug-toolbar==1.5 \
      djangorestframework==3.4.6 \
      markdown==2.6.6 \
      django-filter==0.14.0 \
      django-crispy-forms==1.6.0 \
      django-cleanup==0.4.2 \
      django-extensions==1.7.4 \
      django-compressor==2.1

WORKDIR /src/

{% if cookiecutter.use_translation == 'True' -%}
RUN set -x && apt-get update && DEBIAN_FRONTEND=noninteractive \
       apt-get install -y --no-install-recommends gettext
RUN pip3 install \
      django-modeltranslation==0.11 \
      django-rosetta==0.7.12
{%- endif %}
