#!/bin/bash -a -e

source deploy/.env
envsubst < deploy/docker-compose.yml.template > docker-compose.yml

for env_template in envs/*.template; do
    env=$(echo "$env_template" | cut -d'.' -f 1)
    envsubst < $env_template > $env
done