Alpine, Confluent Kafka, Python - Docker Image
==================================

### Versions Info

* alpine: 3.7
* confluent-kafka: 0.11.0 (default version)
* librdkafka: 0.11.0 (default version)
* python: 3.6

### Pull latest image

`
docker pull 
shivakumarswamy/confluent-kafka
`

### Pull 'confluent-kafka:0.11.0-alpine3.7-python3.6' image
`
docker pull 
shivakumarswamy/confluent-kafka:0.11.0-alpine3.7-python3.6
`

### Steps to build 'confluent-kafka:0.11.0-alpine3.7-python3.6' image

1. Open Terminal

2. Navigate to directory where [Dockerfile](./Dockerfile) exists

3. Run the following command,  
`
docker build 
--tag confluent-kafka:0.11.0-alpine3.7-python3.6 .
`

### Steps to build specific 'confluent-kafka' and 'librdkafka' version

1. Open Terminal

2. Navigate to directory where [Dockerfile](./Dockerfile) exists

3. Run the following command, 
by using `--build-arg` argument to set specific 
'CONFLUENT_KAFKA_VERSION', and 'LIBRDKAFKA_VERSION' (refer 'ARG' in [Dockerfile](./Dockerfile) )  
`
docker build 
--build-arg CONFLUENT_KAFKA_VERSION=<confluent-kafka-version>
--build-arg LIBRDKAFKA_VERSION=<librdkafka_version>
--tag confluent-kafka:<confluent-kafka-version>-alpine3.7-python3.6 .
`


