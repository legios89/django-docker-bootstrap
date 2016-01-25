FROM base
MAINTAINER Egyed Zoltán "zoltan.egyed@vertis.com"
RUN set -x \
    && apt-get update \
    && DEBIAN_FRONTEND=noninteractive \
       apt-get install -y --no-install-recommends \
           libpq5 \
           libpython3.4 \
    && DEBIAN_FRONTEND=noninteractive \
       apt-get install -y --no-install-recommends \
           python3-pip \
           libpq-dev \
           build-essential \
           python3-dev \
           git \
    && pip3 install \
           uwsgi==2.0.12 \
           django==1.9.1 \
           psycopg2==2.6.1 \
           django-debug-toolbar==1.4
WORKDIR /src/

{% if cookiecutter.use_rosetta == 'True' -%}
RUN pip3 install git+https://github.com/legios89/django-rosetta.git@develop
RUN set -x && apt-get update && DEBIAN_FRONTEND=noninteractive \
       apt-get install -y --no-install-recommends gettext
{%- endif %}
