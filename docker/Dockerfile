FROM python:3.6-alpine

MAINTAINER softlabperu.com

RUN apk add --update \
    gcc \
    g++ \
    make \
    nginx \
    libaio \
    automake \
    libc-dev \
    musl-dev \
    pcre-dev \
    supervisor \
    python3-dev \
    linux-headers \
    postgresql-dev \
    && rm  -rf /tmp/* /var/cache/apk/*

RUN mkdir -p /run/nginx && touch /run/nginx/nginx.pid

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY docker/supervisord.conf /etc/
COPY docker/nginx-app.conf /etc/nginx/conf.d/default.conf
COPY docker/supervisor-app.conf /etc/supervisor/conf.d/supervisor.conf

RUN echo "daemon off;" >> /etc/nginx/nginx.conf

COPY . /home/docker/code/
WORKDIR /home/docker/code/
RUN mkdir /media
RUN DATABASE_URL=none python3 manage.py collectstatic --noinput

EXPOSE 80

ENTRYPOINT ["supervisord", "--nodaemon", "--configuration", "/etc/supervisord.conf"]
