#!/bin/bash

cd ./viroid/cluster
for i in {0..5}; do
  cd "./700$i"
  redis-server "./redis.conf" &
  cd ..
done

redis-cli --cluster create 127.0.0.1:7000 127.0.0.1:7001 127.0.0.1:7002 127.0.0.1:7003 127.0.0.1:7004 127.0.0.1:7005 --cluster-replicas 1 &

wait
echo "Redis nodes stopped."
