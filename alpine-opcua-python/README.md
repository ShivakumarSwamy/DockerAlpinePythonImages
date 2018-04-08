Alpine, OPCUA, Python - Docker Image
==================================

### Versions Info

* alpine: 3.7
* opcua: 0.95.1(default version)
* python: 3.6

### Pull latest image

`
docker pull 
shivakumarswamy/opcua
`

### Pull 'opcua:0.95.1-alpine3.7-python3.6' image
`
docker pull 
shivakumarswamy/opcua:0.95.1-alpine3.7-python3.6
`

### Steps to build 'opcua:0.95.1-alpine3.7-python3.6' image

1. Open Terminal

2. Navigate to directory where [Dockerfile](./Dockerfile) exists

3. Run the following command,  
`
docker build 
--tag opcua:0.95.1-alpine3.7-python3.6 .
`

### Steps to build specific OPCUA version

1. Open Terminal

2. Navigate to directory where [Dockerfile](./Dockerfile) exists

3. Run the following command, 
by using '--build-arg' argument to set specific 
'OPCUA_VERSION'(refer 'ARG' in [Dockerfile](./Dockerfile) )  
`
docker build 
--build-arg OPCUA_VERSION=<opcua-version>
--tag opcua:<opcua-version>-alpine3.7-python3.6 .
`


