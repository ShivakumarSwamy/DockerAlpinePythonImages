FROM python:3.6-alpine3.7

LABEL maintainer="Shivakumar Swamy B G <shivsks.1994@gmail.com>"

ARG HAPPYBASE_VERSION="1.1.0"

RUN \
    apk add \
        --no-cache \
        --virtual install_dependencies \
            g++ \
    \
    && pip3 install \
        happybase==$HAPPYBASE_VERSION \
    \
    && apk del install_dependencies
