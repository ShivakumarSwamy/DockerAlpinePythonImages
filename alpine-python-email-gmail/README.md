Send message via email using gmail
==================================

### Versions Info

* alpine: 3.7
* python: 3.6

### Pull latest image

`
docker pull 
shivakumarswamy/email-gmail
`

### Pull 'email-gmail:0.1-alpine3.7-python3.6' image
`
docker pull 
shivakumarswamy/email-gmail:0.1-alpine3.7-python3.6
`

### Steps to build 'email-gmail:0.1-alpine3.7-python3.6' image

1. Open Terminal

2. Navigate to directory where [Dockerfile](./Dockerfile) exists

3. Run the following command,  
`
docker build 
--tag email-gmail:0.1-alpine3.7-python3.6 .
`

### Using image to send email via gmail

#### Option 1: Setting env values using '--env' argument  
`
docker run 
--rm 
--env FROM_ADDRESS=<from-gmail-address>
--env PASSWORD=<password>
--env TO_ADDRESS=<to-address>
--env SUBJECT=<subject-of-email>
--env MESSAGE=<body-of-email>
email-gmail:0.1-alpine3.7-python3.6
`

#### Option 2: Setting env values using '--env-file' argument 
`
docker run 
--rm
--env-file $(pwd)/<example_email_gmail_env.list>
email-gmail:0.1-alpine3.7-python3.6
`

