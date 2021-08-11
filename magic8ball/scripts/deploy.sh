#!/bin/bash

rsync docker-compose.yaml swarm-manager:

ssh swarm-manager << EOF
export MYSQL_DATABASE=$MYSQL_DATABASE, MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD && docker stack deploy --compose-file docker-compose.yaml magic8ball
EOF