#!/bin/bash

set -e

sudo swupd bundle-add ansible

ansible-galaxy collection install community.general

if [ -z "$(docker --version 2> /dev/null)" ]; then
    sudo swupd bundle-add cloud-control
    sudo usermod -aG docker $USER
fi

if [ -z "$(docker-compose --version 2> /dev/null)" ]; then
    sudo swupd bundle-add docker-compose
fi

docker ps > /dev/null 2>&1 \
    || { echo "Session must be restarted to run Docker commands" >&2 exit 1; }