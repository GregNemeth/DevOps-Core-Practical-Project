#!/bin/bash

rsync docker-compose.yaml nginx.conf clear-1:

ssh clear-1 << EOF
export MYSQL_DATABASE=$MYSQL_DATABASE, MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD && docker stack deploy --compose-file docker-compose.yaml magic8ball
EOF
