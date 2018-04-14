# Python 3.6 associated with Alpine linux
FROM python:3.6-alpine3.7

LABEL maintainer="Shivakumar Swamy B G <shivsks.1994@gmail.com>"

# default ARG values
ARG CONFLUENT_KAFKA_VERSION="0.11.0"
ARG LIBRDKAFKA_VERSION="0.11.0"

# --no-cache: do not cache the package index
# --virtual: cleanup packages

RUN \
    # install tar and wget
    apk add --no-cache --virtual download-dependencies \
    tar \
    wget \
    \
    # download librdkafka
    && wget -q \
    -O "librdkafka-$LIBRDKAFKA_VERSION.tar.gz" "https://github.com/edenhill/librdkafka/archive/v$LIBRDKAFKA_VERSION.tar.gz" \
    \
    # extract librdkafka
    && tar -xf "librdkafka-$LIBRDKAFKA_VERSION.tar.gz" \
    \
    # remove downloaded librdkafka tar
    && rm "librdkafka-$LIBRDKAFKA_VERSION.tar.gz" \
    \
    # install bash, g++, and make
    && apk add --no-cache --virtual install-dependencies \
    bash \
    g++ \
    make \
    \
    # navigate to librdkafka directory
    && cd "librdkafka-$LIBRDKAFKA_VERSION" \
    # install librdkafka
    && ./configure \
    && make -s \
    && make -s install \
    \
    # change to root dir
    && cd / \
    # remove librdkafka directory
    && rm -r "librdkafka-$LIBRDKAFKA_VERSION" \
    \
    && pip3 install confluent-kafka==$CONFLUENT_KAFKA_VERSION \
    # remove all dependencies
    && apk del download-dependencies install-dependencies

