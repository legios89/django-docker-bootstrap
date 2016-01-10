FROM vertisfinance/base

MAINTAINER Richard Bann richard.bann@vertis.com

RUN groupadd -g 8080 nginx && useradd -u 8080 -g 8080 -m nginx

RUN set -x \
    && apt-get update \
    && DEBIAN_FRONTEND=noninteractive \
       apt-get install -y --no-install-recommends \
           nginx \
    && DEBIAN_FRONTEND=noninteractive apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
