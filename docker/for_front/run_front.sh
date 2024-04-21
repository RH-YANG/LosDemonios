#!/bin/bash

source ../../.env 


docker run \
    --name $FRONT_CONTAINER \
    --hostname $FRONT_CONTAINER \
    -p $FRONT_PORT:$FRONT_PORT \
    -v $PROJECT_PATH/.env:/.env \
    -v $PROJECT_PATH/front:/front \
    -ti $FRONT_IMAGE \
bin/bash