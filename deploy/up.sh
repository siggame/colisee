#!/bin/bash -ae

echo "deploying registry"
pushd deploy/registry && docker-compose up -d && popd
echo "deploying colisee"
docker-compose up -d
