FROM python:3.11-alpine

RUN apk update && \
    apk upgrade && \
    apk add --no-cache bash gcc libpq-dev

COPY src/ src/
COPY requirements.txt .
COPY .flaskenv .

RUN pip install --no-cache-dir -r requirements.txt
RUN rm -rf requirements.txt

RUN wget https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh

RUN addgroup -S group && \
    adduser -S -G group jane_doe && \
    chmod 600 -R /src && \
    chmod 750 wait-for-it.sh && \
    chown jane_doe:group wait-for-it.sh && \
    chown jane_doe:group -R /src && \
    chmod 700 -R /src

RUN rm -rf /var/cache/apk/* && \
    rm -rf /tmp/*

USER jane_doe

CMD ["./wait-for-it.sh", "db:5432", "--", "flask", "run"]