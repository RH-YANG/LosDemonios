#!/bin/bash

source ../../.env 

docker run \
    --name $API_CONTAINER \
    --hostname $API_CONTAINER \
    -p $API_PORT:$API_PORT \
    -v $PROJECT_PATH/server:/server \
    -ti $API_IMAGE \
bin/bash