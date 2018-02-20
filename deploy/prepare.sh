#!/bin/bash -ae

source deploy/.env
envsubst < deploy/docker-compose.yml.template > docker-compose.yml

for env_template in envs/*.template; do
    env=$(echo "$env_template" | cut -d'.' -f 1)
    service=$(echo "$env" | cut -d'/' -f 2)
    test -d "$STORAGE_BASE/$service" || mkdir -p "$STORAGE_BASE/$service"
    envsubst < $env_template > $env
done