FROM {{cookiecutter.repo_name}}-base
RUN set -x && apt-get update && DEBIAN_FRONTEND=noninteractive \
      apt-get install -y --no-install-recommends \
        libpq5 \
        libpython3.4 \
        libpq-dev \
        build-essential \
        python3-dev

RUN pip3 install \
      uwsgi==2.0.12 \
      django==1.9.4 \
      psycopg2==2.6.1 \
      django-debug-toolbar==1.4 \
      djangorestframework==3.3.2 \
      markdown==2.6.5 \
      django-filter==0.12.0 \
      django-crispy-forms==1.6.0 \
      django-cleanup==0.4.2 \
      django-extensions==1.6.1 \
      django-compressor==2.0

WORKDIR /src/

{% if cookiecutter.use_translation == 'True' -%}
RUN set -x && apt-get update && DEBIAN_FRONTEND=noninteractive \
       apt-get install -y --no-install-recommends gettext
RUN pip3 install \
      django-modeltranslation==0.11 \
      django-rosetta==0.7.9
{%- endif %}
