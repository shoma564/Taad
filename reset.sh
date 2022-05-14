#!/bin/bash
rm -rf ./db/data
docker-compose down --rmi all --volumes --remove-orphans
docker-compose down -v
docker-compose build
docker-compose up
