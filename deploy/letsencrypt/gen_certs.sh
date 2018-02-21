#!/bin/bash -ae

docker run -it --rm \
      -v `pwd`/deploy/letsencrypt/certs:/etc/letsencrypt \
      -v `pwd`/deploy/letsencrypt/certs-data:/data/letsencrypt \
      deliverous/certbot \
      certonly \
      --webroot --webroot-path=/data/letsencrypt \
      -d arena.siggame.io
