#!/bin/bash

rsync docker-compose.yaml swarm-manager:

ssh swarm-manager << EOF
docker stack deploy --compose-file docker-compose.yaml magic8ball
EOF