FROM debian:jessie
MAINTAINER Egyed Zoltán "zoltan.egyed@vertis.com"

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y upgrade
ENV LANG C.UTF-8
RUN set -x \
    && apt-get update \
    && DEBIAN_FRONTEND=noninteractive \
       apt-get install -y --no-install-recommends \
          sudo \
          python3 \
          ca-certificates \
    && DEBIAN_FRONTEND=noninteractive \
       apt-get install -y --no-install-recommends python3-pip \
    && pip3 install click

COPY skel /etc/skel
COPY skel/* /root/
RUN groupadd -g 1000 developer && useradd -u 1000 -g 1000 -m developer
COPY runutils.py /usr/local/lib/python3.4/dist-packages/runutils.py
