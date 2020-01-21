#!/bin/bash
docker container rm timeservice
docker container rm loggerservice
docker run -d -p 8080:5001 --name timeservice timeservice
docker run -d -p 8081:5002 --name loggerservice loggerservice