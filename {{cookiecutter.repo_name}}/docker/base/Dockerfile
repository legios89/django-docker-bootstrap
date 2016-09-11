FROM debian:jessie
MAINTAINER Egyed Zoltán "zoltan.egyed@vertis.com"

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y upgrade
ENV LANG C.UTF-8
RUN set -x && apt-get update && DEBIAN_FRONTEND=noninteractive \
      apt-get install -y --no-install-recommends \
        python3 \
        ca-certificates \
        python3-pip \
        vim \
        curl \
        git

RUN pip3 install click==6.6

COPY skel /etc/skel
RUN git clone https://github.com/legios89/molokai.git /etc/skel/.vim/
COPY skel/* /root/
COPY runutils.py /usr/local/lib/python3.4/dist-packages/runutils.py

ARG DEVELOPER_UID
ARG DEVELOPER_GID
RUN groupadd -g $DEVELOPER_GID developer && \
      useradd -u $DEVELOPER_UID -g $DEVELOPER_GID -m developer
RUN groupadd -g 5432 postgres && useradd -u 5432 -g 5432 -m postgres
