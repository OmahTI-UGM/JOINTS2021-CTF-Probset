FROM python:3-alpine

RUN apk --update --no-cache add py3-paramiko
RUN apk --update --no-cache add socat
RUN apk --update --no-cache add openssl-dev libffi-dev gcc musl-dev python3-dev make 

ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

RUN pip3 install paramiko
RUN pip3 install requests

COPY ./src /app

WORKDIR /app

CMD socat TCP-LISTEN:4444,reuseaddr,fork EXEC:./app.py,su=nobody