#!/bin/bash -ae

echo "removing colisee"
docker-compose down
echo "removing registry"
pushd deploy/registry && docker-compose down && popd