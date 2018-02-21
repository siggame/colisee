#!/bin/bash -ae

echo "preparing letsencrypt"
mkdir -p deploy/letsencrypt/certs deploy/letsencrypt/certs-data
echo "(remember to run use letsencrypt/gen_certs.sh)"

echo "generating docker compose resources"
echo "creating colisee docker compose"
source deploy/.env
envsubst < deploy/docker-compose.yml.template > docker-compose.yml

echo "creating service env files"
for env_template in deploy/envs/*.template; do
    env=$(echo "$env_template" | cut -d'.' -f 1)
    service=$(echo "$env" | cut -d'/' -f 3)
    test -d "$STORAGE_BASE/$service" || mkdir -p "$STORAGE_BASE/$service"
    envsubst < $env_template > $env
    echo -e "DB_HOST=$DB_HOST\nDB_PORT=$DB_PORT\nDB_USER=$DB_USER\nDB_PASSWORD=$DB_PASSWORD\nDB_NAME=$DB_NAME" >> $env
done

echo "pulling images"
docker-compose pull
echo "building images"
docker-compose build