FROM python:3.11-alpine

RUN apk update && \
    apk upgrade && \
    apk add --no-cache bash

COPY src/ src/
COPY requirements.txt .
COPY .flaskenv .

RUN pip install -r requirements.txt
RUN rm -rf requirements.txt

RUN addgroup -S group && \
    adduser -S -G group jane_doe && \
    chmod 600 -R /src && \
    chown jane_doe:group -R /src && \
    chmod 700 -R /src

RUN rm -rf /var/cache/apk/* && \
    rm -rf /tmp/*

USER jane_doe

CMD ["flask", "run"]