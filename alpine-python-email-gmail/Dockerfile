# Use Base image python 3.6 version with alpine linux version 3.7
FROM python:3.6-alpine3.7

LABEL maintainer="Shivakumar Swamy B G <shivsks.1994@gmail.com>"

WORKDIR /email_gmail

COPY . /email_gmail

ENV FROM_ADDRESS="" \
    PASSWORD="" \
    TO_ADDRESS="" \
    SUBJECT="" \
    MESSAGE=""

CMD ["python3" , "app.py"]



