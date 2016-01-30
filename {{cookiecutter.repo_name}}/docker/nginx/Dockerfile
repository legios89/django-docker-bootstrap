FROM base
MAINTAINER Egyed Zoltán "zoltan.egyed@vertis.com"
RUN groupadd -g 8080 nginx && useradd -u 8080 -g 8080 -m nginx

RUN set -x && apt-get update && DEBIAN_FRONTEND=noninteractive \
      apt-get install -y --no-install-recommends \
        curl
RUN curl http://nginx.org/keys/nginx_signing.key | apt-key add -

RUN echo "deb http://nginx.org/packages/debian/ jessie nginx" | tee -a /etc/apt/sources.list
RUN echo "deb-src http://nginx.org/packages/debian/ jessie nginx" | tee -a /etc/apt/sources.list

RUN set -x && apt-get update && DEBIAN_FRONTEND=noninteractive \
      apt-get install -y --no-install-recommends \
        nginx
