FROM vertisfinance/base

MAINTAINER Richard Bann richard.bann@vertis.com

RUN groupadd -g 5432 postgres && useradd -u 5432 -g 5432 -m postgres

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
           postgresql-contrib-9.4 \
    && DEBIAN_FRONTEND=noninteractive apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV PATH /usr/lib/postgresql/9.4/bin:$PATH
