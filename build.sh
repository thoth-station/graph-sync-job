#!/bin/sh

TAG='fridex/thoth-graph-sync-job'

docker login -u $DOCKER_USER -p $DOCKER_PASS
docker build -f Dockerfile -t $TAG .
docker push $TAG
