FROM {{cookiecutter.repo_name}}-base
RUN set -x \
    && apt-get update \
    && DEBIAN_FRONTEND=noninteractive \
       apt-get install -y --no-install-recommends \
           postgresql-common \
    && sed -ri 's/#(create_main_cluster) .*$/\1 = false/' \
       /etc/postgresql-common/createcluster.conf \
    && DEBIAN_FRONTEND=noninteractive \
       apt-get install -y --no-install-recommends \
           postgresql-9.4 \
           postgresql-contrib-9.4

ENV PATH /usr/lib/postgresql/9.4/bin:$PATH
