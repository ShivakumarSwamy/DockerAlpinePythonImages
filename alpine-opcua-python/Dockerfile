FROM python:3.6-alpine3.7

LABEL maintainer="Shivakumar Swamy B G <shivsks.1994@gmail.com>"

ARG OPCUA_VERSION="0.95.1"

RUN \
    apk add \
        --no-cache \
            --virtual install_dependencies \
                g++ \
                libxml2-dev \
                libxslt-dev \
    \
    && apk add \
        --no-cache \
            libxml2 \
            libxslt \
    \
    && pip3 install \
        opcua==$OPCUA_VERSION \
    \
    # cleanup 'install_dependencies'
    && apk del install_dependencies
